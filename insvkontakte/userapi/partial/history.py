from .. import UserAPI, MINID, MAXID

class HistoryAPI(UserAPI):

    def history(self, wall=None, activity=None, message=None, updates_photos=None,
                updates_tagged_photos=None, updates_friends=None, updates_activity=None,
                photos_comments=None, parent=None,
                from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('history', params)

    def history_preload(self, inbox=None, outbox=None, friends_new=None, fave=None,
                profile=None, us=None, read=None):
        params = self._filter_method_params(locals(), ['read'], self._fromto)
        if isinstance(read, tuple):
            params['read'] = '_'.join(read)
        return self._get_request_data('history', params)