import json

from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View
import requests

from utils.settings import VK_APP_ID, VK_APP_SECRET, VK_APP_SCOPE
from vk_api.models import VkAuthToken
from vk_api.status import update_status


class VkAuthView(View):
    def get(self, request, *args, **kwargs):
        redirect_url = request.build_absolute_uri().split('?')[0].split('&')[0]
        if request.GET.get('code'):
            access_token_url = 'https://oauth.vk.com/access_token?' \
                               'client_id=%(client_id)s&' \
                               'client_secret=%(client_secret)s&' \
                               'redirect_uri=%(redirect_url)s&' \
                               'code=%(code)s' % dict(
                client_id=VK_APP_ID,
                client_secret=VK_APP_SECRET,
                redirect_url=redirect_url,
                code=request.GET.get('code')
            )
            r = requests.get(access_token_url)
            response = json.loads(r.text)
            token = VkAuthToken(user_id=response['user_id'], token=response['access_token'])
            token.save()
            return JsonResponse({'success': 'New access_token was created'}, status=200)
        else:
            code_url = 'https://oauth.vk.com/authorize?' \
                       'client_id=%(client_id)s&' \
                       'redirect_uri=%(redirect_url)s&' \
                       'response_type=token&' \
                       'v=5.64&' \
                       'revoke=1&' \
                       'scope=%(scope)s' % dict(
                client_id=VK_APP_ID,
                redirect_url=redirect_url,
                scope=VK_APP_SCOPE,
            )
            return HttpResponseRedirect(code_url)


class VkAPIStatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        status_response = update_status()
        return JsonResponse({'text': json.loads(status_response.text)})
