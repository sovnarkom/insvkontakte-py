from .. import UserAPI, MINID, MAXID

class FriendAPI(UserAPI):

    def friends(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends', params)

    def friends_mutual(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_mutual', params)

    def friends_online(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_online', params)

    def friends_updates(self, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_friends', params)

    def friends_new(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_new', params)

    def friend_add(self, id):
        params = self._filter_method_params(locals())
        return self._get_request_data('add_friend', params)

    def friend_delete(self, id):
        params = self._filter_method_params(locals())
        return self._get_request_data('del_friend', params)
