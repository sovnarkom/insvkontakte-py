from . import UserAPI, MINID, MAXID
from .partial import activity, fave, friend, history, message, \
                    photo, profile, search, wall 

class ClientAPI(activity.ActivityAPI, fave.FaveAPI, friend.FriendAPI,
                history.HistoryAPI, message.MessageAPI, photo.PhotoAPI,
                profile.ProfileAPI, search.SearchAPI, wall.WallAPI, UserAPI):

    def data(self, id, methods=(), from_id=MINID, to_id=MAXID, back=None):
        params = self._filter_method_params(locals(), self._fromto.keys() + 'methods')
        for method in methods:
            params[method] = from_id + '-' + to_id
        return self._get_request_data(None, params)