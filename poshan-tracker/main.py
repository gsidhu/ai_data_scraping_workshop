# POSHAN Tracker Dashboard: https://www.poshantracker.in/statistics

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.poshantracker.in/statistics',
    'Origin': 'https://www.poshantracker.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-GPC': '1',
}

def get_HCM_data():
  # fetch the response
  response = requests.get('https://cdn.poshantracker.in/pt_dashboard/2022/10/19/HCM_given_last_30Days.json?v10', headers=headers)
  # read the response as json
  response = json.loads(response.content.decode('utf-8'))
  values = response['data']['registered_beneficiaries_given_hcm_last_thirty_days']['series'][0]['data']
  keys = response['data']['registered_beneficiaries_given_hcm_last_thirty_days']['dates']
  # convert keys, values to csv
  csv = "date,HCM_given_last_30_days\n"
  for i in range(len(keys)):
    csv += f"{keys[i]},{values[i]}" + "\n"
  # write to file
  with open("./poshan-tracker/HCM_given_last_30_days.csv", 'w') as f:
    f.write(csv)

def get_THR_data():
  response = requests.get('https://cdn.poshantracker.in/pt_dashboard/2023/2/19/THR_given_last_30Days.json?v13', headers=headers)
  response = json.loads(response.content.decode('utf-8'))
  values = response['data']['registered_beneficiaries_given_thr_last_thirty_days']['series'][0]['data']
  keys = response['data']['registered_beneficiaries_given_thr_last_thirty_days']['dates']
  # convert keys, values to csv
  csv = "date,THR_given_last_30_days\n"
  for i in range(len(keys)):
    csv += f"{keys[i]},{values[i]}" + "\n"

  # write to file
  with open("./poshan-tracker/THR_given_last_30_days.csv", 'w') as f:
    f.write(csv)

if __name__ == "__main__":
  get_HCM_data()
  get_THR_data()