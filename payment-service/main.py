from fastapi import FastAPI
from pydantic import BaseModel
import os

class Order(BaseModel):
    order_id: int

app = FastAPI()

@app.post("/process-payment")
def process_payment(order: Order):
    # Simulate payment processing logic
    print(order)
    return {"hostname": os.environ.get("HOSTNAME", "DEFAULT_HOSTNAME")}
