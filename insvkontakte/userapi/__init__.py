'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import VKontakteAPI, InsVKontakteError, __version__

from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse
from mimetypes import guess_type
from email.generator import _make_boundary 

from http.client import MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, \
                        SEE_OTHER, TEMPORARY_REDIRECT, OK
import random

REDIRECTS = (MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, 
             SEE_OTHER, TEMPORARY_REDIRECT)

MINID = 0
MAXID = 3000

class UserAPI(VKontakteAPI):
    
    _host = 'userapi.com'
    _auth_host = 'login.userapi.com'
    _version = '0.9'    

    _fromto = {'from_id': 'from', 'to_id': 'to'}
    _widarr = ['author_id', 'message_id']
    _parentarr = ['owner_id', 'photo_id']
        
    def __init__(self, formatter_type, app_id=None, user_agent=None):
        self._user_agent = 'InsVkontakte/' + __version__
        if user_agent is not None:
            self._user_agent +=  ' ' + user_agent 
      
        self._headers = {'User-Agent': self._user_agent}
        self.formatter = formatter_type()
        self._format = self.formatter._format
        self._appid = app_id
  
        self.max_redirects = 100 
        self.captcha_sid = None
        self.captcha_code = None
        self._sid = None     
        self._remixpassword = None

    def _filter_method_params(self, args, delargs=[], exchange_args={}):
        params = dict()
        for key in args:
            if args[key] is not None and key != 'self' and key not in delargs:
                value = args[key]
                if isinstance(value, bool):
                    if value:
                        value = '1'
                    else:
                        value = '0'  
                elif isinstance(value, tuple):
                    value = ','.join(value)
                params[key] = value
            if key in exchange_args:
                params[exchange_args[key]] = value
                del params[key]
        return params
        
    def prepare_captcha_url(self):
        self.captcha_sid = ''.join(random.sample('1234567890123456789', 10))
        return 'http://' + self._host + '/data?act=captcha&csid=' + self.captcha_sid 

    def get_sid(self):
        return self._sid
    
    def set_sid(self, sid):
        self._sid = sid

    def set_captcha_answer(self, code, sid):
        self.captcha_code = code 
        self.captcha_sid = sid
         
    def _process_response(self, response):
        try:
            data = response.read()
            if response.status == 200:
                try:
                    return self.formatter.format(data)
                except:
                    raise InsVKontakteResponseError(response.status, data)
            else:
                raise InsVKontakteResponseError(response.status, data)
        except Exception as e:
            raise InsVKontakteResponseError('Unable to process request with exception: ' + str(e))
        
    def _sign_params(self, params, auth_needed=False):
        if auth_needed and self._sid is not None:
            params['sid'] = self._sid
        if self.captcha_sid is not None:    
            params['fcsid'] = self.captcha_sid
            params['fccode'] = self.captcha_code
            self.captcha_sid = None
            self.captcha_code = None

    def _get_respone(self, host, method, qpath, data, headers):
        conn = StrHTTPConnection(host)
        conn.request('GET', qpath, None, headers)
        return conn.getresponse()
                    
    def _get_request_data(self, action, params={}, auth_needed=True):
        if action is not None:
            params['act'] = action
        self._sign_params(params, auth_needed)
        qpath = '/data' + '?' + urlencode(params)
        response = self._get_respone(self._host, 'GET', qpath, None, self._headers)
        result = self._process_response(response)
        if isinstance(result, dict) and 'ok' in result and result['ok'] < 1:
            raise InsVKontakteResponseError(result['ok'], result) 
        return result
        
    def get_sid_using_email_and_password(self, email, password):
        params = self._filter_method_params(locals(), [], {'password': 'pass'})
        params['login'] = 'force'
        if self._appid is not None:
            params['site'] = self._appid 
        self._sign_params(params)
        qpath = '/auth' + '?' + urlencode(params)
        response = self._get_respone(self._auth_host, 'GET', qpath, None, self._headers)
        if response.status == FOUND:
            redirect = response.getheader('Location')
            sid = redirect.split(';')[1].split('=')[1]
            if sid == '-1':
                raise InsVKontakteAuthError(sid, 'invalid email or password')
            elif sid == '-2': 
                raise InsVKontakteAuthError(sid, 'invalid captcha')
            elif sid == '-3': 
                raise InsVKontakteAuthError(sid, 'invalid email or password, captcha needed')
            elif sid == '-4': 
                raise InsVKontakteAuthError(sid, 'invalid email or password, no captcha needed')
            else:
                try:
                    cookies = response.getheader('Set-Cookie')
                    self._remixpassword = cookies.split(';')[0].split('=')[1]
                except:
                    pass
                self._sid = sid
                return self._sid
        else:
            raise InsVKontakteResponseError(response.status, 'invalid response on login')
    
    def get_sid_using_remixpassword(self, remixpassword):
        params = self._filter_method_params(locals(), ['remixpassword'])
        params['login'] = 'auto'
        if self._appid is not None:
            params['site'] = self._appid 
        self._sign_params(params)
        qpath = '/auth' + '?' + urlencode(params)
        response = self._get_respone(self._auth_host, 'GET', qpath, None, self._headers +
                                    {'Cookie': 'remixpassword=' + remixpassword})
        if response.status == FOUND:
            redirect = response.getheader('Location')
            sid = redirect.split(';')[1].split('=')[1]
            if sid == '-1':
                raise InsVKontakteAuthError(sid, 'invalid remixpassword')
            elif sid == '-2': 
                raise InsVKontakteAuthError(sid, 'invalid captcha')
            elif sid == '-3': 
                raise InsVKontakteAuthError(sid, 'invalid remixpassword, captcha needed')
            elif sid == '-4': 
                raise InsVKontakteAuthError(sid, 'invalid remixpassword, no captcha needed')
            else:
                self._sid = sid
                return self._sid
        else:
            raise InsVKontakteResponseError(response.status, 'invalid response on login')

    def get_sid_using_confirm_cid(self, cid):
        params = self._filter_method_params(locals())
        params['login'] = 'confirm'
        if self._appid is not None:
            params['site'] = self._appid 
        self._sign_params(params)
        qpath = '/auth' + '?' + urlencode(params)
        response = self._get_respone(self._auth_host, 'GET', qpath, None, self._headers)
        if response.status == FOUND:
            redirect = response.getheader('Location')
            sid = redirect.split(';')[1].split('=')[1]
            if sid == '-1':
                raise InsVKontakteAuthError(sid, 'invalid activation cid')
            else:
                self._sid = sid
                return self._sid
        else:
            raise InsVKontakteResponseError(response.status, 'invalid response on confirm')

    def logout(self):
        params = self._filter_method_params(locals())
        params['login'] = 'logout'
        if self._appid is not None:
            params['site'] = self._appid 
        self._sign_params(params)
        qpath = '/auth' + '?' + urlencode(params)
        response = self._get_respone(self._auth_host, 'GET', qpath, None, self._headers)
        if response.status == FOUND:
            redirect = response.getheader('Location')
            sid = redirect.split(';')[1].split('=')[1]
            if sid == '-1':
                raise InsVKontakteAuthError(sid, 'invalid session id')
            else:
                self._remixpassword = None
                self._sid = None
        else:
            raise InsVKontakteResponseError(response.status, 'invalid response on logout')
            
class StrHTTPResponse(HTTPResponse):
    
    def read(self, amt=None):
        try:
            content_type = self.getheader('Content-Type')
            encoding = content_type.split(';')[1].split('=')[1]
        except:
            encoding = 'utf-8'
        return super().read(amt).decode(encoding)

class StrHTTPConnection(HTTPConnection):
    response_class = StrHTTPResponse


def encode_multipart_formdata(fields, files):
    BOUNDARY = _make_boundary()
    CRLF = ('\r\n').encode()
    L = []
    if fields is not None:
        for key in fields:
            L.append(('--' + BOUNDARY).encode())
            L.append(('Content-Disposition: form-data; name="%s"' % key).encode())
            L.append(('').encode())
            L.append(fields[key].encode())
    for (key, filename, value) in files:
        L.append(('--' + BOUNDARY).encode())
        L.append(('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename)).encode())
        L.append(('Content-Type: %s' % get_content_type(filename)).encode())
        L.append(('').encode())
        L.append(value)
    L.append(('--' + BOUNDARY + '--').encode())
    L.append(('').encode())
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return guess_type(filename)[0] or 'application/octet-stream'


class InsVKontakteProcessError(InsVKontakteError):
    pass

class InsVKontakteAuthError(InsVKontakteError):
    def __init__(self, error_code, msg=None):
        self._error_code = error_code
        self.msg = msg

    def __str__(self):
        return repr(self._error_code) + ': ' + repr(self.msg)    

class InsVKontakteResponseError(InsVKontakteError):
    
    def __init__(self, error_code, formatted_response=None):
        self._error_code = error_code
        self._formatted_response = formatted_response
        
    def __str__(self):
        return repr(self._error_code) + ': ' + repr(self._formatted_response)    
