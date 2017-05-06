import requests
import schedule
import time
import vk
import datetime

from utils.settings import VK_ADMIN_USER_ID
from vk_api.models import VkAuthToken


TRAIN_FINISH_TIME = datetime.datetime(2017, 5, 16, 16, 30)


def update_status():
    access_token = VkAuthToken.objects.token(VK_ADMIN_USER_ID)
    now = datetime.datetime.now()
    new_status = str(TRAIN_FINISH_TIME - now).split('.')[0]

    new_status_url = 'https://api.vk.com/method/status.set?' \
                     'access_token=%(access_token)s&' \
                     'text=%(text)s&v=5.52'\
                     % dict(
                            access_token=access_token,
                            text=new_status
                        )
    r = requests.get(new_status_url)


# schedule.every().hour.do(update_status)
#
# print('In working...')
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
