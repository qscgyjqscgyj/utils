import requests
import datetime

from utils.settings import VK_ADMIN_USER_ID, VK_API_CALL_URL
from vk_api.models import VkAuthToken


TRAIN_FINISH_TIME = datetime.datetime(2017, 5, 16, 16, 30)


def update_status():
    access_token = VkAuthToken.objects.token(VK_ADMIN_USER_ID)
    new_status = str(TRAIN_FINISH_TIME - datetime.datetime.now()).split('.')[0]
    return requests.get(VK_API_CALL_URL, params=dict(access_token=access_token, text=new_status, v='5.64'))


# schedule.every().hour.do(update_status)
#
# print('In working...')
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
