
from fastapi import APIRouter
from app.holidays.checker import check_holiday
from app.holidays.holidays_models import HolidayBatchRequest

router = APIRouter()


@router.post("/check-holiday")
def api_check_holiday(req: HolidayBatchRequest):
    results = []

   
    for r in req.rows:
        try:
            is_holiday = check_holiday(r.market, r.date)
            results.append({
                "market": r.market,
                "date": r.date,
                "is_holiday": is_holiday,
                "error": None
            })
        except Exception as e:
            results.append({
                "market": r.market,
                "date": r.date,
                "is_holiday": None,
                "error": str(e)
            })

    return results

