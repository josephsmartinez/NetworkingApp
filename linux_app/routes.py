from flask import render_template, request, url_for, redirect, flash
from linux_app import app, db, bcrypt
from linux_app.models import User, Host
from linux_app.forms import RegistrationForm, LoginForm
from linux_app.netapi import get_host
from linux_app.fileio import FileIO
from flask_login import login_user, current_user, login_required, logout_user


# ALL routes should have auth tokens
@app.route("/", methods=['GET', 'POST'])
def login():
  '''
  FRONT PAGE
  '''
  if current_user.is_authenticated:
        return redirect(url_for('home'))

  form = LoginForm()
  if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
          login_user(user, remember=form.remember.data)
          next_page = request.args.get('next')
          flash('Welcome!', 'success')
          return redirect(next_page) if next_page else redirect(url_for('home'))
      else:
          flash('Login Unsuccessful. Please check email and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/home")
@login_required
def home():
  return render_template('home.html')

@app.route("/entermac", methods=['GET', 'POST'])
@login_required
def entermac():
  '''
  ENTER MAC PAGE
  - Set up cache
  http://flask.pocoo.org/docs/1.0/patterns/caching/
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

@app.route("/ansiblecmdb")
@login_required
def ansiblecmdb():

  return render_template('ansiblecmdb.html')

@app.route("/cadvisor")
@login_required
def cadvisor():

  return render_template('dblisting.html')

@app.route("/dblisting")
@login_required
def dblisting():
  
  return render_template('dblisting.html')

@app.route("/about")
@login_required
def about():
 
  return render_template('about.html')

@app.route("/useraccount")
@login_required
def useraccount():
 
  return render_template('useraccount.html')

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
  
  '''
  Example route for registering new users
  '''
  if not current_user.is_authenticated:
      return redirect(url_for('login'))

  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('login'))
  return render_template('account.html', title='Register', form=form)
