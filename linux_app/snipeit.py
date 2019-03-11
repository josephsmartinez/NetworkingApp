import requests, json
from linux_app.fileio import FileIO
#from fileio import FileIO

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU4OWNhMWIwMDFlMDM4NmM4MzJjNmE5M2RiNTI4Yjg5NTFmYTk4MTNiN2ViMDZhZDI0ZWI2NDdlNzlkNDFkMDFhZThkZDAwZmM5NmUwNjgzIn0.eyJhdWQiOiI1IiwianRpIjoiNTg5Y2ExYjAwMWUwMzg2YzgzMmM2YTkzZGI1MjhiODk1MWZhOTgxM2I3ZWIwNmFkMjRlYjY0N2U3OWQ0MWQwMWFlOGRkMDBmYzk2ZTA2ODMiLCJpYXQiOjE1NTIxODMyMzYsIm5iZiI6MTU1MjE4MzIzNiwiZXhwIjoxNTgzODAyMDM2LCJzdWIiOiIxMDA2NCIsInNjb3BlcyI6W119.bu2PhwILihCuvVc0JotE1YVYHLRO8DqXNp36V4F0ufJ11-DJtojtyiBtaxI8-RB_ijh3AKi4F9VWiIcSHZcONZWw8Ay8D24CLXieCOMCZ2PiDVct7UAPPq4CmvTxQhxoUZWCQmhDC31iZ0RjjWG26F1WZNy4d5QzxDTzexy0wjx1676vGcR7BvWKiqsLWn4_-gLwSwve-OzEJ9Qbiswr6v8zHwNi99rvlebrHKkCQTwtJk2EaB878OMqpW5Fhp10eD4d2C2143rnX8LJ-anJivyAz-_SZtkZKuGZToY24ttsEWpbHRQgFIZ2eeKL1Q86Xt6lDdyEzbjFQztvzXADzyknJsnqHuLFt0IQv5qjA-qunMO9JwCSzNTIUM-Ctb6r8pbQ6D3ZE28owd4zFMcjXebxVPGA7q-m9Zm9q0-jeLyWPzo9if1MiHE7RBw41jBvYKLYTtnHckKcDrhMqy_z7tt-2zRfNBalBxpfyCdgfohVsgXrdmdFJTbvR6V9s1Ci50ypOM3IBtUjyWiUdsTDmjyJ2uT6SfOkcJan0aTy7-Pw95bBhnrTX0ah3HUFqWGi-hYgf4p7ZxfPxyrj_YlA7q9LUt_CbrNWxPSlNnY_oaD0WAIhxdSJWKWgOiJxRJBaUax8VtHgM7-6YcU81p8HL5feLElVQryL7BmCl_pfhQE'

server='http://casetest.ad.fiu.edu:81'

# GET methods for API calls

def get_assest_by_ID(id: int) -> dict:
  '''
  Get Assest by ID Number
  '''
  uri_hardware = '/api/v1/hardware/'
  asset_id = str(id)
  request = server + uri_hardware + asset_id
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
  response = requests.get(request, headers=headers)
  assest_json=response.json()
  #print(response.json())

  return assest_json

def get_id_by_mac(mac: str) -> dict:
  '''
  Get Assest by Mac Address 
  '''
  uri = '/api/v1/hardware?search='
  request = server + uri + mac
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
  response = requests.get(request, headers=headers)
  #print(response.json())
  assest_json=response.json()
  FileIO.save_to_file(data, "caseidb.json")
  return assest_json

def get_assest_by_tag(tag: str) -> dict:
  '''
  Get Assest by Mac Address
  '''
  uri = '/api/v1/hardware?search='
  request = server + uri + tag
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
  response = requests.get(request, headers=headers)
  #print(response.json())
  assest_json=response.json()
  FileIO.save_to_file(assest_json, "caseidb.json")
  return assest_json

def get_assest_by_serial(serial: str) -> dict:
  '''
  Get Assest ID by name
  '''
  uri = '/api/v1/hardware?search='
  request = server + uri + serial
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
  response = requests.get(request, headers=headers)
  #print(response.json())
  assest_json=response.json()
  FileIO.save_to_file(assest_json, "caseidb.json")
  return assest_json

if __name__ == "__main__":
  #get_assest_by_ID(81)
  #get_id_by_mac("78:7B:8A:DC:8B:CD")
  #get_assest_by_tag("ATT-0010149")
  pass