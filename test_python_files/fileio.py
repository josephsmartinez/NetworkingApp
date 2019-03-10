# File handler class for JSON and XML
# V 1.0.2
# Add more error handling and logs messages 
import json
import os.path
import lxml.etree as etree
from datetime import datetime

templates_dir="templates/"

class FileIO:

  @staticmethod
  def json2file(data: dict,file_name: str) -> None:
    with open(file_name,'w') as write_file:
      json.dump(data,write_file,indent=4)
      write_file.close()

  @staticmethod
  def append_json2file(data: dict,file_name: str) -> None:
    with open(file_name,'a') as write_file:
      json.dump(data,write_file,indent=4)
      write_file.close()

  @staticmethod              
  def read_jsonfile(file_name: str) -> str:
    with open(file_name,'r') as read_file:
        data=json.load(read_file)
        read_file.close()
        return data

  @staticmethod
  def xml2file(data: dict,file_name: str) -> None:
    with open(templates_dir + file_name,'w') as write_file:
      write_file.write(data)
      write_file.close()
  
  @staticmethod
  def append_xml2file(data: dict,file_name: str) -> None:
    with open(templates_dir + file_name,'a') as write_file:
       write_file.write(data)
       write_file.close()
  
  @staticmethod
  def read_xmlfile(file_name: str) -> str:
    with open(templates_dir + file_name,'r') as read_file:
      data= read_file.read()
      read_file.close()
      return data
    
  @staticmethod
  def log(*argv: str) -> None:
    file_name= "app.log"
    try: 
      # Timestamp log and add content
      with open(file_name,'a+',) as write_file:
        write_file.write(str(datetime.now()) + " ")
        for arg in argv:  
          write_file.write(arg + " ")
        write_file.write("\n")
    except Exception as e:
      print("log file error, check event!", e)
    finally:
      write_file.close()
