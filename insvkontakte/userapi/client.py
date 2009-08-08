from . import UserAPI
import random

MAXID = 999999

class ClientAPI(UserAPI):

    _fromto = {'from_id': 'from', 'to_id': 'to'}
    
    def friends(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends', params)

    def friends_mutual(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_mutual', params)

    def friends_online(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_online', params)

    def friends_new(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('friends_new', params)

    def photos(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos', params)

    def photos_with(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_with', params)

    def photos_new(self, id, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_new', params)
    
    def photos_comments(self, id, parents=None, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_comments', params)

    def wall(self, id, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('wall', params)

    def activity(self, id, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('activity', params)
 
    def fave(self, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('fave', params)
 
    def fave_online(self, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('fave_online', params)

    def faved(self, from_id=1, to_id=MAXID, ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('faved', params)
 
    def updates_activity(self, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_activity', params)
    
    def updates_friends(self, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_friends', params)

    def updates_photos(self, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_photos', params)

    def updates_tagged_photos(self, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_tagged_photos', params)

    def message(self, id=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('message', params)

    def message_inbox(self, id=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('inbox', params)

    def message_outbox(self, id=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('outbox', params)

    def cities(self, parent, q=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('cities', params, False)

    def schools(self, parent, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('schools', params, False)

    def search_results(self, q=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('search_results', params, False)

    def quick_search(self, q=None, from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('quick_search', params, False)

    def profile(self, id, back=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('profile', params)

    def data(self, id, methods=(), from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), self._fromto.keys() + 'methods')
        for method in methods:
            params[method] = from_id + '-' + to_id
        return self._get_request_data('profile', params)
        
    def history(self, wall=None, activity=None, message=None, updates_photos=None,
                # basic
                updates_​tagged_photos=None, updates_friends=None, updates_activity=None,
                photos_comments=None, parent=None,
                # preload
                inbox=None, outbox=None, friends_new=None, fave=None, profile=None,
                us=None, read=None,
                from_id=1, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('quick_search', params, False)

    #-----------------------------------------------------------------------
    
    def get_captcha_url(self):
        self.captcha_sid = random.sample(range(9), 60)
        return 'http://' + self._host + '/data?act=captcha&csid=' + self.captcha_sid 
    
   
    def set_activity(self, text, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('set_activity', params)
    
    def clear_activity(self, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('clear_activity', params)
    
    def del_activity(self, ts=None):
        params = self._filter_method_params(locals())
        return self._get_request_data('del_activity', params)