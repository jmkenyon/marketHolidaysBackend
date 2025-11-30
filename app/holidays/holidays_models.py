from pydantic import BaseModel


class SingleHoliday(BaseModel):
    market: str
    date: str

class HolidayBatchRequest(BaseModel):
    rows: list[SingleHoliday]