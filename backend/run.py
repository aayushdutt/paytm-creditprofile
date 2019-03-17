from scoreapp import app

if __name__ == '__main__':
	app.run(debug=True)

# for sqlite run these command on terminal
#
# python
# from scoreapp import db
# db.create_all()
# from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser, masterData, ap
# User.query.all()
# region = Region(name='Over Yonder Thar')
# db.session.add(region)
# db.session.commit()
# job_id= job_data.job_id
# db.session.commit()
# rows = db.session.query(table_name).count()
# u = teamUser(username="A", password="12345")
# >>> db.session.add(u)
# >>> db.session.commit()
#  q = jobs(job_id=7, job_name='marketing', job_status='finish', start_time=1541008354, finish_time=1541319354, total_records=1420, currently_processed_records=422);