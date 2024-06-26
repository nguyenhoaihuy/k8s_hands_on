from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    order_id: int

app = FastAPI()

@app.post("/send-notification")
def send_notification(order: Order):
    # Simulate sending notification logic
    print(order)
    return {"message": f"Notification sent for order {order}"}
