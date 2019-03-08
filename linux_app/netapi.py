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
  Calls Network Security API
  Return  JSON object
  '''
  try:
    if mac == None:
      err_message="{'error': 'Missing mac address or malformed'}"
      FileIO.log(str(err_message))
      return err_message
    else: 
      host = json.loads(subprocess.Popen('php linux_app/apis/api.php ' + mac.lower(),
      shell=True, stdout=subprocess.PIPE, 
      universal_newlines=True).communicate()[0])
      return host
  except Exception as err:
    FileIO.log(str(err))

def ping_host(ip: str) -> bool:
  '''
  Ping host using ip address or hostname
  Return True or False
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
  NSlookup host using ip address
  Return String or None
  Regex: egrep -o "([A-Za-z ])\w+\.\w+\.\w+\.\w+"
  '''
  # FIXME: Check all returns from nslookup check regex 
  # ** server can't find 93.35.100.10.in-addr.arpa: NXDOMAIN
  #  name = rho.fiu.edu.

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
       return hostname
    else:
      return None
  except Exception as err:
    FileIO.log("response error for nslookup_host function")


