from fastapi import FastAPI

app = FastAPI()

@app.post("/process-payment/")
def process_payment(order_id: int):
    # Simulate payment processing logic
    return {"message": f"Payment processed for order {order_id}"}
