from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    order_id: int

app = FastAPI()

@app.post("/process-payment")
def process_payment(order: Order):
    # Simulate payment processing logic
    print(order)
    return {"message": f"Payment processed for order {order}"}
