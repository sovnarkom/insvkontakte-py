from .. import UserAPI, MINID, MAXID

class PhotoAPI(UserAPI):

    def photos(self, id, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos', params)

    def photos_with(self, id, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_with', params)

    def photos_new(self, id, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_new', params)
    
    def photos_comments(self, id, parents=None, from_id=MINID, to_id=MAXID,
                        ts=None, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('photos_comments', params)
    
    def photos_updates(self, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_photos', params)

    def photos_updates_tagged(self, from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), [], self._fromto)
        return self._get_request_data('updates_tagged_photos', params)
    
    def photo_comment_add(self, id, message, owner_id, photo_id, pts=None):
        params = self._filter_method_params(locals(), self._parentarr)
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('add_photos_comments', params)

    def photo_comment_delete(self, id, author_id, message_id,
                              owner_id, photo_id, ts=None):
        params = self._filter_method_params(locals(), 
            self._parentarr + self._widarr)
        params['wid'] = author_id + '_' + message_id
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('del_photos_comments', params)
    
    def photo_comment_restore(self, id, author_id, message_id,
                              owner_id, photo_id, ts=None):
        params = self._filter_method_params(locals(),
            self._parentarr + self._widarr)
        params['wid'] = author_id + '_' + message_id
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('restore_photos_comments', params)

    def photo_delete_profile(self):
        return self._get_request_data('delete_page_photo')

    def photo_delete(self, owner_id, photo_id):
        params = self._filter_method_params(locals(), self._parentarr)
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('delete_photo')
    
    def photo_tag_put(self, id, name, owner_id, photo_id, 
                      x1=None, x2=None, y1=None, y2=None):
        params = self._filter_method_params(locals(), self._parentarr)
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('put_tag', params)

    def photo_tag_delete(self, tid, owner_id, photo_id):
        params = self._filter_method_params(locals(), self._parentarr)
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('delete_tag', params)

    def photo_tag_confirm(self, tid, owner_id, photo_id):
        params = self._filter_method_params(locals(), self._parentarr)
        params['parent'] = owner_id + '_' + photo_id
        return self._get_request_data('confirm_tag', params)
