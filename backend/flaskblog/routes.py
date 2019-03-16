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
	print("home called")
	jobq = jobs.query.filter_by(job_status='active')
	return render_template('home.html', title='Index', jobs=jobq)

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



@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

