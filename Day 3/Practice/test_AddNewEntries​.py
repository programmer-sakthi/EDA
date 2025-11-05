import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())

    new_row = {
        "appointment_id": "APT9999",
        "user_id": "USR999",
        "user_name": "Test User",
        "gender": "Other",
        "area": "Koramangala",
        "city": "Bangalore",
        "service_id": "SRV999",
        "provider_id": "PRV999",
        "appointment_date": "15/11/2025",
        "appointment_time": "14:30",
        "status": "Scheduled",
        "payment_id": "PMT9999",
        "amount(INR)": 2000,
        "discount%": 10,
        "tax": 12,
        "discounted_amount(INR)": 1800,
        "tax_amount(INR)": 216,
        "final_amount": 2016,
        "payment_method": "Credit Card",
        "service_rating": 5,
        "service_name": "Test Massage",
        "category": "Massage",
        "price": 2000,
        "name": "Test Provider",
        "specialization": "Relaxation",
        "rating": 4.5,
    }
    df["appointment_month"] = pd.to_datetime(
        df["appointment_date"], dayfirst=True
    ).dt.month_name()
    print(pd.concat([df.head(5), df.tail(5)]))
    df = pd.concat([df, pd.DataFrame([new_row])])


if __name__ == "__main__":
    compute()
