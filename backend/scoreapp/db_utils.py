from scoreapp import app, db, bcrypt
from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()
#
#
# if __name__ == '__main__':
