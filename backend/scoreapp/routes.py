import os
import csv
import secrets
import pandas as pd
# import numpy as np
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, send_file, jsonify
from scoreapp import app, db, bcrypt
from scoreapp.forms import LoginForm
from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser, masterData
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
		else:
			pass
		# # refresh page
		#jobq = jobs.query.filter_by(job_status='active')
		return redirect(url_for('home'))
	except Exception as e:
		self.log.exception(e)
		self.Error(400)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route("/dataloader")
def load_data():
	#file = pd.read_csv('scoreapp/data.csv')
	#print(file.head())
	file_name = 'scoreapp/data.csv'
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		flag = 0
		cnt = 0
		for row in csv_reader:
			#print(row)
			#print(type(row))
			#age, id, is_auto_billing_on, is_paytm_first, is_postpaid, postpaid_outstanding, orders_placed_in_6months, \
    #orders_placed_in_6months_via_epay, orders_placed_in_6months_via_cod, orders_placed_in_6months_via_emi, \
    #orders_delivered_in_6months, total_money_on_order_from_mall_6months, total_money_on_order_on_travel_6months, \
    #total_money_on_order_on_movie_6months, total_money_spent, total_money_added_on_wallet, CODorNot, EMIorNot

			if flag:
				md = masterData( id = row[1], age = row[0], is_auto_billing = row[2], is_paytm_first = row[3], 
				is_postpaid = row[4], postpaid_outstanding = row[5], orders_placed_in_6months = row[6], 
				orders_placed_in_6months_via_epay = row[7], orders_placed_in_6months_via_cod = row[8],
				orders_placed_in_6months_via_emi = row[9], orders_delivered_in_6months = row[10], 
				total_money_on_order_from_mall_6months = row[11], total_money_on_order_on_travel_6months = row[12],
				total_money_on_order_on_movie_6months = row[13], total_money_spent = row[14], 
				total_money_added_on_wallet = row[15], CODorNot = row[16], EMIorNot = row[17])
				db.session.add(md)
				db.session.commit()
				cnt += 1
				print(cnt)				
			flag = 1