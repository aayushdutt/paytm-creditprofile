
from scoreapp import db, login_manager
from flask_login import UserMixin
from sqlalchemy import  *

@login_manager.user_loader
def load_user(user_id):
    return teamUser.query.get(int(user_id))

class order(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    pdt_id = db.Column(db.Integer, nullable=False)
    pdt_amount = db.Column(db.Float, nullable=False)
    is_COD = db.Column(db.Integer, nullable=False, default=0)
    is_EPay = db.Column(db.Integer, nullable=False, default=0)
    is_Travel = db.Column(db.Integer, nullable=False, default=0)
    is_Paytm_Mall = db.Column(db.Integer, nullable=False, default=0)
    is_Movie = db.Column(db.Integer, nullable=False, default=0)
    timeStamp = db.Column(db.Integer, default=0)    #
    def __repr__(self):
        return f"OrderByUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class shippingData(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    pdt_id = db.Column(db.Integer, nullable=False)
    pdt_amount = db.Column(db.Float, nullable=False)
    is_COD = db.Column(db.Integer, nullable=False, default=0)
    is_EPay = db.Column(db.Integer, nullable=False, default=0)
    is_Cancelled = db.Column(db.Integer, nullable=False, default=0)
    is_Delivered = db.Column(db.Integer, nullable=False, default=0)
#    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    timeStamp = db.Column(db.Integer, default=0)  #
    def __repr__(self):
        return f"ShippingForUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class registrationData(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
#    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    timeStamp = db.Column(db.Integer, default=0)  #
    def __repr__(self):
        return f"RegistrationOfUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class marketing(db.Model, UserMixin):
    sr_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    is_auto_billing = db.Column(db.Integer, nullable=False, default=0)
    is_paytm_first = db.Column(db.Integer, nullable=False, default=0)
    is_postpaid_given = db.Column(db.Integer, nullable=False, default=0)
    postpaid_amount_given = db.Column(db.Float, nullable=False, default=0)
    postpaid_outstanding = db.Column(db.Float, nullable=False, default=0)
#    timeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    timeStamp = db.Column(db.Integer, default=0)  #
    def __repr__(self):
        return f"MarketiToUser('{self.sr_no}', '{self.customer_id}', '{self.customer_name}')"

class jobs(db.Model, UserMixin):
    job_id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(20), nullable=False)
    job_status = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.Integer, nullable=False)
    finish_time = db.Column(db.Integer, nullable=False)
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

class masterData(db.Model, UserMixin):
    id = db.Column(db.String(20), primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    is_auto_billing = db.Column(db.Integer, nullable=False, default=0)
    is_paytm_first = db.Column(db.Integer, nullable=False, default=0)
    is_postpaid = db.Column(db.Integer, nullable=False, default=0)
    postpaid_outstanding = db.Column(db.Integer, nullable=False, default=0)
    orders_placed_in_6months = db.Column(db.Integer, nullable=False)
    orders_placed_in_6months_via_epay = db.Column(db.Integer, nullable=False)
    orders_placed_in_6months_via_cod = db.Column(db.Integer, nullable=False)
    orders_placed_in_6months_via_emi = db.Column(db.Integer, nullable=False)
    orders_delivered_in_6months = db.Column(db.Integer, nullable=False)
    total_money_on_order_from_mall_6months = db.Column(db.Integer, nullable=False)
    total_money_on_order_on_travel_6months = db.Column(db.Integer, nullable=False)
    total_money_on_order_on_movie_6months = db.Column(db.Integer, nullable=False)
    total_money_spent = db.Column(db.Integer, nullable=False)
    total_money_added_on_wallet = db.Column(db.Integer, nullable=False)
    CODorNot = db.Column(db.Integer, nullable=False)
    EMIorNot = db.Column(db.Integer, nullable=False)
    RatioDvP = db.Column(db.Float, nullable=False)

