from . import UserAPI

class AuthAPI(UserAPI):
    
    _host = 'login.userapi.com'

    def _get_method_path(self, method):
        return '/auth'

    def get_sid_using_email_and_password(self, email, password):
        params = self._filter_method_params(locals())
        params['login'] = 'force'
        return self._get_request_data('friends_mutual', params)
