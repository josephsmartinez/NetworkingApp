# File handler class
# V 0.0.1
# Add more error handling and logs messages 
import json
from datetime import datetime

class FileIO:

  @staticmethod
  def save_to_file(data: dict,file_name: str) -> None:
    with open(file_name,'w') as write_file:
      json.dump(data,write_file,indent=4)
      
  @staticmethod              
  def read_from_file(file_name: str) -> None:
    with open(file_name,'r') as read_file:
        file=json.load(read_file)
        return file
  
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
