# TODO:
# - Clean mac string and verify correct hex format
# - Make sure the address id lower case
# - If null/None return JSON message error
# - Handle returned JSON before method return 

import subprocess
import json
import os
import time
from linux_app.fileio import FileIO

def get_host(mac: str) -> dict:
  '''
  Return a JSON object with host networking information
  '''
  if mac == None:
    err_message="{'message': 'Missing mac address or malformed'}"
    FileIO.log(err_message)
    return err_message
  else: 
    host = json.loads(subprocess.Popen('php linux_app/apis/api.php ' + mac.lower(),
    shell=True, stdout=subprocess.PIPE, 
    universal_newlines=True).communicate()[0])

    return host

def ping_host(ip: str) -> bool:
  '''
  Ping host using ip address or hostname
  '''
  try:
    if ip:
      response = os.system("ping -W 1 -c 1 " + ip)
  except Exception as err:
    FileIO.log("ping command error")

  try:
    # Check the response success
    if response == 0:
      print(ip, 'is up!')
      return True
    else:
      print(ip, 'is down!')
      return False
  except Exception as err:
    FileIO.log("response error for post_host function")

  return False

def nslookup_host(ip: str) -> str:
  '''
  NSlookup host using ip address or hostname
  Examples:
  nslookup 10.100.36.47 | egrep -o "([A-Za-z ])\w+\.\w+\.\w+\.\w+"
  '''
  
  try:
    if ip:
     proc = subprocess.Popen('nslookup ' + ip + ' | egrep -o "([A-Za-z ])\w+\.\w+\.\w+\.\w+"',
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
    universal_newlines=True)

    # Clean the return string
    hostname = proc.communicate()[0].rstrip().strip()

  except Exception as err:
    FileIO.log("nslookup command error")

  try:
    # Check the response success
    if hostname:
       print(hostname)
    else:
      print('could not process host name')
  except Exception as err:
    FileIO.log("response error for nslookup_host function")


