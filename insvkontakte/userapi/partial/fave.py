from .. import UserAPI, MINID, MAXID

class FaveAPI(UserAPI):

    def faves(self, from_id=MINID, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('fave', params)
 
    def faves_online(self, from_id=MINID, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('fave_online', params)

    def faved(self, from_id=MINID, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('faved', params)

    def fave_add(self, id):
        params = self._filter_method_params(locals())
        return self._get_request_data('add_fave', params)

    def fave_delete(self, id):
        params = self._filter_method_params(locals())
        return self._get_request_data('del_fave', params)