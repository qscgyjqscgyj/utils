import requests
import schedule
import time

M = [2552, 2552, 3062, 2552, 2552, 2807, 2552]
A = [1482, 1186, 1779, 1482, 1334, 1631, 1482]

DAY_PARTS = [0.2, 0.125, 0.27, 0.125, 0.27]

SMS_RU_MISHA = '784aa849-b2b0-8c34-05c6-87faf1c24abf'
SMS_RU_ALINA = '030a7549-9e0f-ada4-39f4-5918e3f81d0c'

BREAKFAST_TIME = '12:00'
FIRST_SNACK_TIME = '14:30'
LUNCH_TIME = '17:00'
SECOND_SNACK_TIME = '19:30'
DINNER_TIME = '22:00'


def send_sms(day, day_part):
    data = {'api_id': SMS_RU_MISHA, 'to': '79233694898', 'text': str(int(M[day] * DAY_PARTS[day_part]))}
    requests.post('http://sms.ru/sms/send', data=data)
    data = {'api_id': SMS_RU_ALINA, 'to': '79233724258', 'text': str(int(A[day] * DAY_PARTS[day_part]))}
    requests.post('http://sms.ru/sms/send', data=data)


schedule.every().monday.at(BREAKFAST_TIME).do(send_sms, 0, 0)
schedule.every().monday.at(FIRST_SNACK_TIME).do(send_sms, 0, 1)
schedule.every().monday.at(LUNCH_TIME).do(send_sms, 0, 2)
schedule.every().monday.at(SECOND_SNACK_TIME).do(send_sms, 0, 3)
schedule.every().monday.at(DINNER_TIME).do(send_sms, 0, 4)

schedule.every().tuesday.at(BREAKFAST_TIME).do(send_sms, 1, 0)
schedule.every().tuesday.at(FIRST_SNACK_TIME).do(send_sms, 1, 1)
schedule.every().tuesday.at(LUNCH_TIME).do(send_sms, 1, 2)
schedule.every().tuesday.at(SECOND_SNACK_TIME).do(send_sms, 1, 3)
schedule.every().tuesday.at(DINNER_TIME).do(send_sms, 1, 4)

schedule.every().wednesday.at(BREAKFAST_TIME).do(send_sms, 2, 0)
schedule.every().wednesday.at(FIRST_SNACK_TIME).do(send_sms, 2, 1)
schedule.every().wednesday.at(LUNCH_TIME).do(send_sms, 2, 2)
schedule.every().wednesday.at(SECOND_SNACK_TIME).do(send_sms, 2, 3)
schedule.every().wednesday.at(DINNER_TIME).do(send_sms, 2, 4)

schedule.every().thursday.at(BREAKFAST_TIME).do(send_sms, 3, 0)
schedule.every().thursday.at(FIRST_SNACK_TIME).do(send_sms, 3, 1)
schedule.every().thursday.at(LUNCH_TIME).do(send_sms, 3, 2)
schedule.every().thursday.at(SECOND_SNACK_TIME).do(send_sms, 3, 3)
schedule.every().thursday.at(DINNER_TIME).do(send_sms, 3, 4)

schedule.every().friday.at(BREAKFAST_TIME).do(send_sms, 4, 0)
schedule.every().friday.at(FIRST_SNACK_TIME).do(send_sms, 4, 1)
schedule.every().friday.at(LUNCH_TIME).do(send_sms, 4, 2)
schedule.every().friday.at(SECOND_SNACK_TIME).do(send_sms, 4, 3)
schedule.every().friday.at(DINNER_TIME).do(send_sms, 4, 4)

schedule.every().saturday.at(BREAKFAST_TIME).do(send_sms, 5, 0)
schedule.every().saturday.at(FIRST_SNACK_TIME).do(send_sms, 5, 1)
schedule.every().saturday.at(LUNCH_TIME).do(send_sms, 5, 2)
schedule.every().saturday.at(SECOND_SNACK_TIME).do(send_sms, 5, 3)
schedule.every().saturday.at(DINNER_TIME).do(send_sms, 5, 4)

schedule.every().sunday.at(BREAKFAST_TIME).do(send_sms, 6, 0)
schedule.every().sunday.at(FIRST_SNACK_TIME).do(send_sms, 6, 1)
schedule.every().sunday.at(LUNCH_TIME).do(send_sms, 6, 2)
schedule.every().sunday.at(SECOND_SNACK_TIME).do(send_sms, 6, 3)
schedule.every().sunday.at(DINNER_TIME).do(send_sms, 6, 4)

print('In working...')

while True:
    schedule.run_pending()
    time.sleep(1)
