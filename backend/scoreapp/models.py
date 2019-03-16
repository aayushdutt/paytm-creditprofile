from datetime import datetime
from scoreapp import db, login_manager
from flask_login import UserMixin
from sqlalchemy import  *

@login_manager.user_loader
def load_user(user_id):
    return teamUser.query.get(int(user_id))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    age = db.Column(db.String(30), nullable=True)
    gender = db.Column(db.String(6), nullable=True)
    file_t1 = db.Column(db.String(90), nullable=True)
    file_flair = db.Column(db.String(90), nullable=True)
    file_ir = db.Column(db.String(90), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Patient('{self.first_name}', '{self.last_name}', '{self.age}', '{self.gender}', '{self.file_t1}','{self.file_flair}','{self.file_ir}', '{self.date_posted}')"

class order(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    pdt_id = db.Column(db.Integer, nullable=False)
    pdt_amount = db.Column(db.Float, nullable=False)
    is_COD = db.Column(db.Integer, nullable=False, default=0)
    is_EPay = db.Column(db.Integer, nullable=False, default=0)
    is_Travel = db.Column(db.Integer, nullable=False, default=0)
    is_Paytm_Mall = db.Column(db.Integer, nullable=False, default=0)
    is_Movie = db.Column(db.Integer, nullable=False, default=0)
    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"OrderByUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class shippingData(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    pdt_id = db.Column(db.Integer, nullable=False)
    pdt_amount = db.Column(db.Float, nullable=False)
    is_COD = db.Column(db.Integer, nullable=False, default=0)
    is_EPay = db.Column(db.Integer, nullable=False, default=0)
    is_Cancelled = db.Column(db.Integer, nullable=False, default=0)
    is_Delivered = db.Column(db.Integer, nullable=False, default=0)
    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"ShippingForUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class registrationData(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"RegistrationOfUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class marketing(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    is_auto_billing = db.Column(db.Integer, nullable=False, default=0)
    is_paytm_first = db.Column(db.Integer, nullable=False, default=0)
    is_postpaid_given = db.Column(db.Integer, nullable=False, default=0)
    postpaid_amount_given = db.Column(db.Float, nullable=False, default=0)
    postpaid_outstanding = db.Column(db.Float, nullable=False, default=0)
    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"MarketiToUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class jobs(db.Model, UserMixin):
    job_id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(20), nullable=False)
    job_status = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    finish_time = db.Column(db.DateTime, nullable=False)
    total_records = db.Column(db.Integer, nullable=False)
    currently_processed_records = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"Job:('{self.job_id}', '{self.job_name}', '{self.currently_processed_records}', '{self.total_records}')"

class teamUser(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(130), nullable=False)

    def get_id(self):
        return (self.user_id)

    def __repr__(self):
        return f"teamUser:('{self.username}')"
