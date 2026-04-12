def accept(order_id, retries=3):
    return {"order": order_id, "state": "accepted", "retries": retries}
