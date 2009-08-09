from .. import UserAPI

class ProfileAPI(UserAPI):

    def profile(self, id=None, back=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('profile', params)
    
    def profile_register(self, fn, ln, email, password, sex, school, year, back=None):
        params = self._filter_method_params(locals(), [], {'password': 'pass'})
        return self._get_request_data('register', params, False)
    
    def profile_edit(self, sx=None, fs=None, ln=None, pv=None, bd=None, bm=None, by=None, 
                     cii=None, mo=None, nf=None, nm=None, back=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('edit_page', params, False)
    
    def profile_school_add(self, school, year):
        params = self._filter_method_params(locals())
        return self._get_request_data('add_school', params)

    def profile_school_delete(self, school, year):
        params = self._filter_method_params(locals())
        return self._get_request_data('del_school', params)

