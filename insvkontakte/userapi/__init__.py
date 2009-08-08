'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import InsVKontakteError, InsVKontakteProcessError, InsVKontakteResponseError
from .. import VKontakteAPI

from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse
from mimetypes import guess_type
from email.generator import _make_boundary 

from http.client import MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, \
                        SEE_OTHER, TEMPORARY_REDIRECT

REDIRECTS = (MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, 
             SEE_OTHER, TEMPORARY_REDIRECT)

class UserAPI(VKontakteAPI):
    
    def __init__(self, app_id, formatter_type, user_agent=None):
        super().__init__(app_id, formatter_type, user_agent)
        self.max_redirects = 100 
        self.captcha_sid = None
        self.captcha_code = None
        
        
    def _get_request_data_solving_redirects(self, method, path, data, headers):
        conn = StrHTTPConnection(self._host)
        r = 0
        while r < self.max_redirects:
            conn.request(method, path, data, headers)
            response = conn.getresponse()
            if response.status in REDIRECTS:
                path = response.getheader('Location', path)
                r += 1
            else:
                break
        if r == self.max_redirects:
            raise InsVKontakteResponseError('Redirects exceeded!')
        return response
    
    def _get_request_data(self, action, params, auth_needed=True):
        if auth_needed and self._sid is not None:
            params['sid'] = self._sid
        if self.captcha_sid is not None:    
            params['fcsid'] = self.captcha_sid
            params['fccode'] = self.captcha_code
            self.captcha_sid = None
            self.captcha_code = None
        qpath = '/data' + '?' + urlencode(params)
        return self._process_response(
            self._get_request_data_solving_redirects('GET', qpath, None, self._headers)
        )


class StrHTTPResponse(HTTPResponse):
    
    def read(self, amt=None):
        return super().read(amt).decode()


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
