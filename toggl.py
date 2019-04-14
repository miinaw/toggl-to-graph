# coding: UTF-8

import requests
import pprint
import sys
import settings.py
from datetime import date


proj = sys.argv[1]  # 集計したいプロジェクト名 
API_TOKEN = settings.API_TOKEN  # 確認したトークンを設定
W_ID = '3065983'       # 確認したworkspace_idを設定
MAIL = settings.MAIL       # 登録したメールを設定
since = sys.argv[2]  # from date
until = sys.argv[3]

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
            description = data['description']
            print(description)
            time = float(data['dur']) / 3600000
            print(time)
