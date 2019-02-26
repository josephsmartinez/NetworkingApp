from flask import render_template, request, url_for, redirect, flash
from linux_app import app, db, bcrypt
from linux_app.models import User, Host, check_mac
from linux_app.forms import RegistrationForm, LoginForm
from linux_app.netapi import get_host, nslookup_host, ping_host
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
      host_json = get_host(macaddr)
      FileIO.log(str(host_json))

      # If host found check for ICMP, hostname, and add to database
      if host_json['status'] != 404:
        pingable = ping_host(host_json['device']['address'])
        hostname = nslookup_host(host_json['device']['address'])
        FileIO.log(host_json['device']['address'], str(pingable), str(hostname))

        # Check if host is in the database, if not, commit to DB
        host_found = check_mac(host_json['device']['hardware'])

        if not host_found:
          new_host = Host(hardware=host_json['device']['hardware'],parent_name=host_json['device']['parent_name'], parent_type=host_json['device']['parent_type'], parent_port=host_json['device']['parent_port'], fingerprint=host_json['device']['fingerprint'], address=host_json['device']['address'])
          db.session.add(new_host)
          db.session.commit()

        return render_template('entermac.html', host=host_json, pingable=pingable, hostname=hostname)

      return render_template('entermac.html', host=host_json)
    else:
      host_json = ""
      flash('Nothing entered', 'danger')
      return render_template('entermac.html', host=host_json)
      
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

@app.route("/register", methods=['GET', 'POST'])
def register():
  
  '''
  Example route for registering new users
  '''
  # if not current_user.is_authenticated:
  #     return redirect(url_for('login'))

  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)
