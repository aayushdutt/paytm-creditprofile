from scoreapp import app

if __name__ == '__main__':
    app.run(debug=True)

# for sqlite run these command on terminal
#
# python
# from scoreapp import db
# db.create_all()
# from scoreapp.models import Patient, order, shippingData, registrationData, marketing, jobs, teamUser
# User.query.all()
# region = Region(name='Over Yonder Thar')
# db.session.add(region)
# db.session.commit()
# job_id= job_data.job_id
# db.session.commit()