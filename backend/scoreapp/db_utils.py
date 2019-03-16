from scoreapp import app, db, bcrypt
from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

def load_data(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cnt = 0
        for row in csv_reader:
            print(row)
            print(type(row))
            cnt += 1
            if cnt > 10: 
                break


# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()
#
#
if __name__ == '__main__':
    load_data('ml/data.csv')