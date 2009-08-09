from .. import UserAPI, MINID, MAXID

class MessageAPI(UserAPI):

    def messages(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('message', params)

    def messages_inbox(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('inbox', params)

    def messages_outbox(self, id=None, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('outbox', params)

    def message_add(self, id, message, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('add_message', params)

    def message_delete(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('del_message', params)

    def message_inbox_delete(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('del_inbox', params)

    def message_outbox_delete(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('del_outbox', params)

    def message_restore(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('restore_message', params)

    def message_inbox_restore(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('restore_inbox', params)

    def message_outbox_restore(self, id, author_id, message_id, ts=None):
        params = self._filter_method_params(locals(), self._widarr)
        params['wid'] = author_id + '_' + message_id
        return self._get_request_data('restore_outbox', params)
