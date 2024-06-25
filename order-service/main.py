from fastapi import FastAPI, HTTPException
import requests

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
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send notification: {str(e)}")

    # Call payment service
    try:
        payment_response = requests.post(payment_service_url, json={"order_id": order_id})
        payment_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to process payment: {str(e)}")

    return {"message": "Order created, notification sent, and payment processed"}
