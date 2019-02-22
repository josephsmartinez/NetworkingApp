from flask import render_template, request, url_for, redirect, flash
from linux_application.forms import RegistrationForm, LoginForm
from linux_application import app
from linux_application.netapi import get_host
from linux_application.fileio import FileIO

# ALL routes should have auth tokens
@app.route("/", methods=['GET', 'POST'])
def login():
  '''
  FRONT PAGE
  '''
  form = LoginForm()
  if form.validate_on_submit():
      if form.username.data == 'castic' and form.password.data == 'password':
          flash('You have been logged in!', 'success')
          return redirect(url_for('home'))
      else:
          flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@app.route("/entermac", methods=['GET', 'POST'])
def home():
  '''
  ENTER MAC PAGE
  '''
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

@app.route("/cmbd")
def ansible_cmbd():
  return render_template('ansible_cmbd.html')

@app.route("/cadvisor")
def cadvisor():
  return render_template('dblisting.html')

@app.route("/db")
def db():
  return render_template('dblisting.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/useraccount")
def useraccount():
  return render_template('useraccount.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
  '''
  Example route for registering new users
  '''
  form = RegistrationForm()
  if form.validate_on_submit():
      # Using f-string
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

# @app.route("/login")
# def login():
#   form = LoginForm()
#   return render_template('register.html', title='Login', form=form)