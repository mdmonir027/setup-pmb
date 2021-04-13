import json
# from replit import db

def jadu(number, amount):
  # db["data"] = []
  # d = db["data"]
  # d.append({"number": number, "count": amount})
  # db["data"] = d
  with open('data.json', 'r', encoding='utf-8') as f:
    j = json.load(f)
    j.append({"phone": number, "count": amount})
  with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(j, f, sort_keys=True, indent=2)