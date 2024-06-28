from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

notification_service_url = "http://notification-service:80/send-notification"
payment_service_url = "http://payment-service:80/process-payment"

@app.post("/create-order/{order_id}")
def create_order(order_id: int):
    # Simulate order creation logic

    # Call notification service
    try:
        notification_response = requests.post(notification_service_url, json={"order_id": order_id})
        notification_response.raise_for_status()
        print(notification_response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send notification: {str(e)}")

    # Call payment service
    try:
        payment_response = requests.post(payment_service_url, json={"order_id": order_id})
        payment_response.raise_for_status()
        print(payment_response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to process payment: {str(e)}")

    order_hostname = os.environ.get("HOSTNAME", "DEFAULT_HOSTNAME")
    print(order_hostname)
    return {"order_hostname": order_hostname,
            "notification_hostname": notification_response.json()["hostname"],
            "payment_hostname": payment_response.json()["hostname"]}
