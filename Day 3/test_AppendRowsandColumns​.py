import os
import sys
import pandas as pd


def compute():
    orders = pd.read_csv(os.path.join(sys.path[0], input()))
    delivery = pd.read_csv(os.path.join(sys.path[0], input()))
    new_data = pd.DataFrame(
        {"order_id": ["ORD1968"], "user_id": ["USR145"], "total_amount": [560]}
    )
    orders = pd.concat([orders, new_data], ignore_index=True)
    orders["delivery_partner_pay"] = orders["total_amount"] * 0.07
    data = pd.merge(orders, delivery, how="left")
    data.fillna("", inplace=True)
    print(data.loc[46:51])


if __name__ == "__main__":
    compute()
