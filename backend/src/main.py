from os import environ as env

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


APP_FRONTEND_ORIGINS = env.get("APP_FRONTEND_ORIGINS", "http://localhost:3000,http://localhost")

app = FastAPI(
    middleware=[
        Middleware(CORSMiddleware, allow_origins=APP_FRONTEND_ORIGINS.split(","), allow_credentials=True, allow_methods=["*"], allow_headers=["*"]),
    ],
)


@app.get("/")
def index():
    return f"{app.title} v{app.version}"


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/brand/{brand_id}")
def get_brand(brand_id):
    result = {
        "brand_id": brand_id,
        "brand_status": "OK",
        "brand_result": "SUCCESS",
    }
    result = {
        "brand_name": "Nusret",
        "polarity_score": 57,
        "subjectivity_score": 34,
        "ratings": [
            {
                "platform_name": "Talabat",
                "rating_actual": 4.2,
                "rating_rounded": 4.0,
            },
            {
                "platform_name": "Deliveroo",
                "rating_actual": 4.4,
                "rating_rounded": 4.5,
            },
        ],
        "branch_id": [123, 456, 789],
    }
    return JSONResponse(result)


@app.get("/branch/{branch_id}")
def get_branch(branch_id):
    result = {
        "branch_id": branch_id,
        "branch_status": "OK",
        "branch_result": "SUCCESS",
    }
    return JSONResponse(result)


@app.get("/branch/{branch_id}/detail")
def get_branch_detail(branch_id):
    result = {
        "branch_id": branch_id,
        "detail_status": "OK",
        "detail_result": "SUCCESS",
    }
    result = {
        "branch_name": "Dubai Mall",
        "branch_id": branch_id,
        "polarity_score": 72,
        "subjectivity_score": 24,
        "ratings": [
            {
                "platform_name": "Talabat",
                "rating_actual": 4.8,
                "rating_rounded": 5.0,
            },
            {
                "platform_name": "Deliveroo",
                "rating_actual": 4.4,
                "rating_rounded": 4.5,
            },
        ],
        "meals": [
            {
                "meal_name": "Burger",
                "rating_actual": 4.6,
                "rating_rounded": 4.5,
            },
            {
                "meal_name": "HavucDilim",
                "rating_actual": 4.8,
                "rating_rounded": 5.0,
            },
        ],
    }
    return JSONResponse(result)
