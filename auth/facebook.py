from urllib import urlencode
import urllib2
import json
import time
from urllib import unquote_plus

#from django.core.cache import cache as memcache


class GetFacebookData(object):
    '''
    get: user id and token
    '''
    last_time = 0.0

    def __init__(self, token):
        #self.uid = uid
        self.token = token

    def call_api(self, method, params):
        '''
        This method formed QUERY with accepted parameter to VK API
        :param cids: for show country/city with id
        :param method: what query we do
        :param fields: what fields we will get
        :return: dict
        '''
        time.sleep(max(0.0, 0.3333 - (time.clock() - self.last_time)))

        if isinstance(params, list):
            params_list = params[:]
        elif isinstance(params, dict):
            params_list = params.items()
        else:
            params_list = [params]

        params_list += [('access_token', self.token)]
        print 'p_list', params_list
        url = 'https://graph.facebook.com/%s?%s' % (method, unquote_plus(urlencode(params_list)))
        print 'facebook_url', url

        response = urllib2.urlopen(url).read()
        self.last_time = time.clock()

        return (json.loads(response))['data']  # If use get method return all item in value
