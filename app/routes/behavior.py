from fastapi import APIRouter

from app.analytics import (
    detect_revenge_trading,
    detect_overtrading
)

router = APIRouter(prefix="/behavior", tags=["Behavior"])


@router.get("/revenge-trading")
def revenge_trading():
    return {
        "status": "success",
        "data": detect_revenge_trading()
    }


@router.get("/overtrading")
def overtrading():
    return {
        "status": "success",
        "data": detect_overtrading()
    }