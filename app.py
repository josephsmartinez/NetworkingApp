from flask import Flask, render_template, request
from netapi import get_host

app = Flask(__name__)



@app.route('/netapi', methods=['GET', 'POST'])
def home():

  if request.method == 'POST': #this block is only entered when the form is submitted
    
    macaddr = request.form.get('macaddr')
    
    if macaddr != None:
     
      # Parse host information 
      host = get_host(macaddr)
      print(host)
      for k, v in host.items():
        if isinstance(v, dict):
          for k1, v1 in v.items():
            print(k1, v1)
        else:
          print(k, v)
      return render_template('index.html', host=host)
    else:
      host = ""
      return render_template('index.html', host=host)
      
  return render_template('index.html')


@app.route('/about')
def about():
  pass


@app.route('/login', methods=['GET', 'POST'])
def login():
  pass


if __name__== '__main__':
  app.run(debug=True)