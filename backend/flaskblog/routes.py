import os
import secrets
# import numpy as np
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, send_file
from flaskblog import app, db, bcrypt
from flaskblog.forms import LoginForm
from flaskblog.models import order, shippingData, registrationData, marketing, jobs, teamUser
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    image_file = url_for('static', filename='img/paytm_logo.png')
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    #print("Line 18")
    if form.validate_on_submit():
        user = teamUser.query.filter_by(username=form.username.data).first()
        print(user)
        if user and user.password == form.password.data:
            #print("Line 23")
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            #print(next_page)
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            #print("Line 27")
            flash('Login Unsuccessful. Please check email and password', 'danger')
    #print("Line 29")
    return render_template('login.html', title='Login', form=form, logo = image_file)


@app.route("/home")
@login_required
def home():
    #print("home called")
    return render_template('home.html', title='Index')

@app.route("/ml/<string:category>")
def ml(category=None):
    if category is None:
        self.Error(400)
    try:
        jobq = jobs.query.filter_by(job_status='active').first()
        return render_template('ml.html', title='Prediction', job=jobq)
    except Exception as e:
        self.log.exception(e)
        self.Error(400)


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


'''
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
'''

'''
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)
'''

'''
def save_file_T1(form_picture,last_name, first_name):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = last_name + first_name + f_ext
    picture_path = os.path.join(app.root_path, 'static/mri/T1', picture_fn)
    f = request.files.getlist('file_T1')[0]
    f.save(picture_path)
    return picture_fn

def save_file_FLAIR(form_picture,last_name, first_name):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = last_name + first_name + f_ext
    picture_path = os.path.join(app.root_path, 'static/mri/FLAIR', picture_fn)
    f = request.files.getlist('file_FLAIR')[0]
    f.save(picture_path)
    return picture_fn

def save_file_IR(form_picture,last_name, first_name):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = last_name + first_name + f_ext
    picture_path = os.path.join(app.root_path, 'static/mri/IR', picture_fn)
    f = request.files.getlist('file_IR')[0]
    f.save(picture_path)
    return picture_fn

@app.route("/addPatient", methods=['GET', 'POST'])
@login_required
def addPatient():
    form = AddPatient()
    if form.validate_on_submit():
        picture_fn_T1 = save_file_T1(form.file_T1.data, form.lastName.data, form.firstName.data)
        picture_fn_FLAIR = save_file_FLAIR(form.file_FLAIR.data, form.lastName.data, form.firstName.data)
        picture_fn_IR = save_file_IR(form.file_IR.data, form.lastName.data, form.firstName.data)
        patient = Patient(first_name=form.firstName.data, last_name=form.lastName.data, age=form.age.data,
                          gender=form.gender.data, file_t1=picture_fn_T1, file_flair=picture_fn_FLAIR,
                          file_ir=picture_fn_IR, author=current_user)
        db.session.add(patient)
        db.session.commit()
        flash('Patient information is successfully entered', 'success')
        return redirect(url_for('home'))
    return render_template('addPatient.html', title='Add Patient', form=form)


@app.route("/viewPatient")
@login_required
def viewPatient():
    patient = current_user.patient
    return render_template('viewPatient.html', title='View Patient', patients=patient)


@app.route("/patient/<int:patient_id>")
@login_required
def patient(patient_id):
    print("lineno139")
    patient = Patient.query.get_or_404(patient_id)
    return render_template('patient.html', title='Patient', patient=patient)


@app.route("/downloadfile/<string:path>")
def DownloadFile (path = None):
    if path is None:
        self.Error(400)
    try:
        picture_path = os.path.join(app.root_path, 'static/mri', path)
        return send_file(picture_path, as_attachment=True)
    except Exception as e:
        self.log.exception(e)
        self.Error(400)

# pragma table_info(patient)
@app.route("/classML/<int:class_no>", methods=['GET', 'POST'])
def classML (class_no):
    if request.method == 'POST':
        file = request.form.get('files_dropdown')
        print(file)
        print(app.config["UPLOAD_FOLDER"])
        try:
            make_gif(f'{app.config["UPLOAD_FOLDER"]}/{file}')
            success = True
            error = None
        except Exception as e:
            success = False
            error = str(e)

        return render_template('analyze.html', title='Results', success=success,
                               error=error, folder=app.config["UPLOAD_FOLDER"])
    return render_template('analysis.html')
'''