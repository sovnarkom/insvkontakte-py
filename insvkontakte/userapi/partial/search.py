from .. import UserAPI, MINID, MAXID

class SearchAPI(UserAPI):

    def search_cities(self, parent, q=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('cities', params, False)

    def search_schools(self, parent, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('schools', params, False)

    def search_users(self, parent=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('search_results', params, False)

    def search_quick(self, q=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('quick_search', params, False)
