from pydantic import BaseModel, computed_field,Field


class product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class bookingRoom(BaseModel):
    room_id: int
    user_id: int
    nights: int = Field(..., gt=0, description="Nights must be greater than 0")
    rate_per_night: float = Field(..., gt=0, description="Rate per night must be greater than 0")


    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night


booking = bookingRoom(
    room_id=101,
    user_id=1,
    nights=3,
    rate_per_night=153.67
)

print(f"Room ID: {booking.room_id}, User ID: {booking.user_id}, Nights: {booking.nights}, Rate per Night: {booking.rate_per_night}, Total Cost: {booking.total_cost}")
