import uuid
from viewed import app
from datetime import datetime
from flask import request, session, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import func

#import views
import viewed.view_job_request
import viewed.view_user

#import models
from viewed.models import User

@app.route('/')
def index():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if checkUserExists(request):
            if checkCredentials(request):
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                error = 'Invalid Login Credentials'
        else:
            error = 'Email address is not on file'
    
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    #flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/home')
def home():
    return render_template('job_match_listing.html')


def checkCredentials(request):
 
    _inputEmail =  request.form['inputEmail']
    
    result = User.query.filter(func.lower(User.email) == func.lower(_inputEmail)).first()
    if not result:
        return False
    else:
        if result.check_password(request.form['inputPassword']):
            session['userid'] = result.id
            return True
        else:
            return False
                
def checkUserExists(request):
    
    _inputEmail = request.form['inputEmail']

    result = User.query.filter(func.lower(User.email) == func.lower(_inputEmail)).first()

    if not result:
        return False
    else:
        return True

#
# determines if a user with the specified email exists
#
def checkEmailAvailable(request):
    
    _inputEmail = request.form['inputEmail']

    result = User.query.filter(func.lower(User.email) == func.lower(_inputEmail)).first()

    if not result:
        return True
    else:
        return False