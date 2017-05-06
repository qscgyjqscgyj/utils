import schedule
import time
import vk
import datetime

from utils.settings import VK_ADMIN_USER_ID
from vk_api.models import VkAuthToken


TRAIN_FINISH_TIME = datetime.datetime(2017, 5, 16, 16, 30)


def update_status():
    session = vk.Session(access_token=VkAuthToken.objects.token(VK_ADMIN_USER_ID))
    vk_api = vk.API(session)

    now = datetime.datetime.now()
    new_status = str(TRAIN_FINISH_TIME - now).split('.')[0]

    vk_api.status.set(text=new_status)


schedule.every().hour.do(update_status)

print('In working...')

while True:
    schedule.run_pending()
    time.sleep(1)
