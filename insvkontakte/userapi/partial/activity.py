from .. import UserAPI, MINID, MAXID

class ActivityAPI(UserAPI):

    def activity(self, id, from_id=MINID, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('activity', params)
     
    def activity_set(self, text, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('set_activity', params)
    
    def activity_clear(self, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('clear_activity', params)
    
    def activity_delete(self, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('del_activity', params)
    
    def activity_updates(self, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_activity', params)       