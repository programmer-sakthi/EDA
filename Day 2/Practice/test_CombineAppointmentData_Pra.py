import os 
import sys 

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)

def compute():
    appointments=get_csv(input())
    payments=get_csv(input())
    services=get_csv(input())
    services=services[['service_id','service_name','category']]
    service_providers=get_csv(input())
    appointments_payments=pd.merge(appointments,payments , on=['appointment_id'] , how='left')
    appointments_payments_service=pd.merge(appointments_payments,services , on=['service_id'], how='left')
    appointments_payments_service_provider=pd.merge(appointments_payments_service,service_providers , on='provider_id', how='left'  )
    print("Final Merged Data (first 5 rows):")
    print(appointments_payments_service_provider.head())

if __name__=='__main__':
    compute()


