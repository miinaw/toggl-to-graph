# coding: UTF-8
import pandas as pd
import requests
import pprint
import sys
import settings
import pickle
from datetime import date


proj = sys.argv[1]  # 集計したいプロジェクト名 
API_TOKEN = settings.API_TOKEN  # 確認したトークンを設定
W_ID = settings.W_ID       # 確認したworkspace_idを設定
MAIL = settings.MAIL       # 登録したメールを設定
since = sys.argv[2]  # from date
until = sys.argv[3]  # to date
time_list = []
date_list = []
# toggl_data = {}


def get_toggl():
    headers = {'content-type': 'application/json'}
    today = date.today().isoformat()
    params = {
        'user_agent': MAIL,
        'workspace_id': W_ID,
        'since': since,
        'until': until
    }
    auth = requests.auth.HTTPBasicAuth(API_TOKEN, 'api_token')
    return requests.get('https://toggl.com/reports/api/v2/details', auth=auth, headers=headers, params=params)


if __name__ == '__main__':
    details = get_toggl().json()['data']

    for data in details:
        project = data['project']
        if project == proj:
            time = (round(float(data['dur']) / 3600000, 2) * 60)
            date = data['start'].split('T')[0]
            time_list.append(time)
            date_list.append(date)
            # toggl_data.update(zip(date_list, time_list))

df = pd.DataFrame({'date': date_list, 'time': time_list})
df.to_csv('toggl_data.csv', index=False)

