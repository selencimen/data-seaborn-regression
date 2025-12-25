import pandas as pd
from data import Olist


class Order:
    def __init__(self):
        self.data_loader = Olist()
        self.data = self.data_loader.get_data()

    def get_training_data(self, with_distance_seller_customer=False):
        orders = self.data["orders"]
        reviews = self.data["order_reviews"]

        orders["order_purchase_timestamp"] = pd.to_datetime(
            orders["order_purchase_timestamp"]
        )
        orders["order_delivered_customer_date"] = pd.to_datetime(
            orders["order_delivered_customer_date"]
        )
        orders["order_estimated_delivery_date"] = pd.to_datetime(
            orders["order_estimated_delivery_date"]
        )

        orders["wait_time"] = (
            orders["order_delivered_customer_date"]
            - orders["order_purchase_timestamp"]
        ).dt.days

        orders["delay_vs_expected"] = (
            orders["order_delivered_customer_date"]
            - orders["order_estimated_delivery_date"]
        ).dt.days

        df = orders.merge(
            reviews[["order_id", "review_score"]],
            on="order_id",
            how="left"
        )

        return df
