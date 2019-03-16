import os
import secrets
# import numpy as np
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, send_file, jsonify
from scoreapp import app, db, bcrypt
from scoreapp.forms import LoginForm
from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser
from flask_login import login_user, current_user, logout_user, login_required
from scoreapp.job_helper import *

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
	image_file = url_for('static', filename='img/paytm_logo.png')
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = teamUser.query.filter_by(username=form.username.data).first()
		print(user)
		if user and user.password == form.password.data:
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form, logo = image_file)


@app.route("/home")
@login_required
def home():
	print("home called")
	jobq = jobs.query.filter_by(job_status='active')
	return render_template('home.html', title='Index', jobs=jobq)

# @app.route("/run/<string:category>")
# def run(category=None):
# 	if category is None:
# 		self.Error(400)
# 	try:
# 		jobq = jobs.query.filter_by(job_status='active')
# 		return render_template('home.html', title='Index', jobs=jobq)
# 	except Exception as e:
# 		self.log.exception(e)
# 		self.Error(400)


@app.route("/run/<string:category>")
def run(category=None):
	if category is None:
		self.Error(400)
	try:
		# run and save job
		job_data = run_job(category)
		if(len(job_data)>0):
			flash("Already Added")

		# redirect to home
		return redirect(url_for('home'))
	except Exception as e:
		self.log.exception(e)
		self.Error(400)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))