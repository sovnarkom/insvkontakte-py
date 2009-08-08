__author__ = 'Alexander Chichenin <sovnarkom@somebugs.com>'
__version__ = '0.0.0 Incubation'

class VKontakteAPI(object):
    _host = 'userapi.com'
    _version = '0.9'

    def __init__(self, formatter_type, user_agent=None, sid=None):
        super().__init__()
        self._user_agent = 'InsVkontakte/' + __version__
        if user_agent is not None:
            self._user_agent +=  ' ' + user_agent 
        self._headers = {'User-Agent': self._user_agent}
        self.formatter = formatter_type()
        self._format = self.formatter._format
        self._sid = sid 
           
    def _get_method_path(self, method):
        return '/data/' + method

    def _filter_method_params(self, args, delargs=[], exchange_args={}):
        params = dict()
        for key in args:
            if args[key] is not None and key != 'self' and key not in delargs:
                value = args[key]
                if isinstance(value, bool):
                    value = str(value).lower()
                elif isinstance(value, tuple):
                    value = ','.join(value)
                params[key] = value
            if key in exchange_args:
                params[exchange_args[key]] = value
                del params[key]
        if params != {}:
            return params
        else:
            return None

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
            
            
class InsVKontakteError(Exception):
    pass

class InsVKontakteProcessError(Exception):
    pass

class InsVKontakteResponseError(InsVKontakteError):
    
    def __init__(self, error_code, formatted_response=None):
        self._error_code = error_code
        self._formatted_response = formatted_response
        
    def __str__(self):
        return repr(self._error_code) + ': ' + repr(self._formatted_response)    