from .. import UserAPI, MINID, MAXID

class WallAPI(UserAPI):

    def wall(self, id=None, from_id=MINID, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('wall', params)

    def wall_add(self, message, id=None, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('add_wall', params)

    def wall_delete(self, author_id, message_id, id=None, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('del_wall', params)
    
    def wall_restore(self, author_id, message_id, id=None, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('restore_wall', params)