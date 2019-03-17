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
from sqlalchemy import desc
import time

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
		print("line59")
		job_data = jobs.query.filter_by(job_name=category).filter_by(job_status='active').all()
		print("line61")
		if(len(job_data)>0):
			flash("Already Added")
			print("line64")
		else:
			print("line66")
			job_data = jobs.query.filter_by(job_name=category).filter_by(job_status='finish').order_by(desc(jobs.finish_time)).first()
			print("line68")
			new_job_start_time = job_data.finish_time
			new_job_id= db.session.query(jobs).count()+1
			new_job_name = category
			new_job_status = 'active'
			new_job_finish_time = -1
			new_job_currently_processed_records = 0
			# run the actual job
			# calling async function
			new_job_total_records = recordCounter(category, new_job_start_time)
			new_job = jobs(job_id=new_job_id, job_name=new_job_name, job_status=new_job_status, start_time=new_job_start_time, finish_time=new_job_finish_time, total_records= new_job_total_records, currently_processed_records=new_job_currently_processed_records);
			db.session.add(new_job)
			db.session.commit()
			print("line73")
		job_active = jobs.query.filter_by(job_status='active')
		print("line75")
		return render_template('home.html', title='Index', jobs=job_active)
	except Exception as e:
		self.log.exception(e)
		self.Error(400)

def runJob(category, totalRecord):
	if category=='shipping':
		shippingData.query.filter(shippingData.timeStamp>=startTime).count()
	elif category=='orders':
		return order.query.filter(order.timeStamp >= startTime).count()
	elif category=='registration':
		return registrationData.query.filter(registrationData.timeStamp >= startTime).count()
	else:

def recordCounter(category, startTime):
	if category=='shipping':
		return shippingData.query.filter(shippingData.timeStamp>=startTime).count()
	elif category=='orders':
		return order.query.filter(order.timeStamp >= startTime).count()
	elif category=='registration':
		return registrationData.query.filter(registrationData.timeStamp >= startTime).count()
	else:
		return marketing.query.filter(marketing.timeStamp>=startTime).count()

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))


# later is the csv to database

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
			cntt = 0
			if flag:
				md = masterData(id=row[1], age=int(row[0]), is_auto_billing=int(row[2]), is_paytm_first=int(row[3]),
								is_postpaid=int(row[4]), postpaid_outstanding=int(row[5]),
								orders_placed_in_6months=int(row[6]),
								orders_placed_in_6months_via_epay=int(row[7]),
								orders_placed_in_6months_via_cod=int(row[8]),
								orders_placed_in_6months_via_emi=int(row[9]), orders_delivered_in_6months=int(row[10]),
								total_money_on_order_from_mall_6months=int(row[11]),
								total_money_on_order_on_travel_6months=int(row[12]),
								total_money_on_order_on_movie_6months=int(row[13]), total_money_spent=int(row[14]),
								total_money_added_on_wallet=int(row[15]), CODorNot=int(row[16]), EMIorNot=int(row[17]),
								RatioDvP=float(row[18]))
				db.session.add(md)
				db.session.commit()
				cnt += 1
				print(cnt)				
			flag = 1

@app.route("/orderData")
def orderData():
	file_name = 'scoreapp/ml/order.csv'
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		flag = 0
		cnt = 0
		for row in csv_reader:
			cntt = 0
			if flag:
				md = order(sr_no=int(row[0]), customer_id=row[1], customer_name=row[2], pdt_id=int(row[3]),
								pdt_amount=int(row[4]), is_COD=int(row[5]),
								is_EPay=int(row[6]),
								is_Travel=int(row[7]),
								is_Paytm_Mall=int(row[8]),
								is_Movie=int(row[9]), timeStamp=int(float(row[10])))
				db.session.add(md)
				db.session.commit()
				cnt += 1
				print(cnt)
			flag = 1

@app.route("/marketingData")
def marketingData():
	file_name = 'scoreapp/ml/market.csv'
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		flag = 0
		cnt = 0
		for row in csv_reader:
			cntt = 0
			if flag:
				md = marketing(sr_no=int(row[0]), customer_id=row[1], customer_name=row[2], is_auto_billing=int(row[3]),
								is_paytm_first=int(row[4]), is_postpaid_given=int(row[5]),
								postpaid_amount_given=float(row[6]),
								postpaid_outstanding=float(row[7]),
						   		timeStamp=int(float(row[8])))
				db.session.add(md)
				db.session.commit()
				cnt += 1
				print(cnt)
			flag = 1

@app.route("/shipData")
def shipData():
	file_name = 'scoreapp/ml/shippingData.csv'
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		flag = 0
		cnt = 0
		for row in csv_reader:
			cntt = 0
			if flag:
				md = shippingData(sr_no=int(row[0]), customer_id=row[1], customer_name=row[2], pdt_id=int(row[3]),
								pdt_amount=int(row[4]), is_COD=int(row[5]),
								is_EPay=int(row[6]),
								is_Cancelled=int(row[7]),
						   		is_Delivered=int(row[8]),
						   		timeStamp=int(float(row[9])))

				db.session.add(md)
				db.session.commit()
				cnt = cnt + 1
				print(cnt)
			flag = 1

@app.route("/regData")
def regData():
	file_name = 'scoreapp/ml/reg.csv'
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		flag = 0
		cnt = 0
		for row in csv_reader:
			cntt = 0
			if flag:
				md = registrationData(sr_no=int(row[0]), customer_id=row[1], customer_name=row[2], email=row[3],
								age=int(row[4]),
						   		timeStamp=int(float(row[5])))

				db.session.add(md)
				db.session.commit()
				cnt = cnt + 1
				print(cnt)
			flag = 1