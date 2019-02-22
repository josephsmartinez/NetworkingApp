import subprocess
import json
from linux_application.fileio import FileIO

def get_host(mac: str) -> dict:
  '''
  Return a JSON object with host networking information
  '''
  if mac == None:
    err_message="{'message': 'Missing mac address or malformed'}"
    FileIO.log(err_message)
    return err_message
  else: 
    host = json.loads(subprocess.Popen('php apis/api.php ' + mac.lower(),
    shell=True, stdout=subprocess.PIPE, 
    universal_newlines=True).communicate()[0])

    return host

'''
TODO:
- Clean mac string and verify correct hex format
- Make sure the address id lower case
- If null/None return JSON message error
- Handle returned JSON before method return 
'''