from fastapi import FastAPI

app = FastAPI()

@app.post("/send-notification/")
def send_notification(order_id: int):
    # Simulate sending notification logic
    return {"message": f"Notification sent for order {order_id}"}
