from flask import Flask, render_template, request, url_for
from netapi import get_host

app = Flask(__name__)



@app.route('/', methods=['GET'])
def login():
  return render_template('login.html')

@app.route('/entermac', methods=['GET', 'POST'])
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
      return render_template('entermac.html', host=host)
    else:
      host = ""
      return render_template('entermac.html', host=host)
      
  return render_template('entermac.html')


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/account')
def account():
  return render_template('account.html')


if __name__== '__main__':
  app.run(debug=True)