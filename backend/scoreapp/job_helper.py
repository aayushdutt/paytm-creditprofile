from scoreapp import app, db, bcrypt
from scoreapp.models import order, shippingData, registrationData, marketing, jobs, teamUser



def run_job(job_category):   #category
    print("reached run_job()")
    active_jobs = jobs.query.filter_by(job_name=job_category).filter_by(job_status='active').all()
#    if len(active_jobs) > 0 :
    return active_jobs
    #print(type(active_jobs))



    #job_to_be_saved = jobs(job_id=job_data.job_id, job_name=job_data.job_name, job_status=job_data.job_status, 		
    #	start_time=job_data.start_time, finish_time=job_data.finish_time, total_records=job_data.total_records,
     #   currently_processed_records=job_data.currently_processed_records)

    # if job_name == 'order':
    #     return run_orders()
    # elif job_name == 'shipping':
    #     return run_shipping()
    # elif job_name == 'registration':
    #     return run_registration()
    # elif job_name == 'marketing':
    #     return marketing()


'''

    0. if 'orders' job is already running, flash screen saying job is already running. then do nothing else. 
    1. fetch orders from last time stamp
    2. process orders
    3. store result
'''

#def run_orders():



#def fetch_records(string job_name):
    