from os import environ as env

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


APP_FRONTEND_ORIGINS = env.get("APP_FRONTEND_ORIGINS", "http://localhost:3000,http://localhost:5173")

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
        "brand_name": "Nusret",
        "polarity_score": 57,
        "subjectivity_score": 34,
        "rating_actual": 4.2,
        "rating_rounded": 4.0,
        "rating_count": 1729,
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
        "branch_ids": [123, 456, 789],
    }
    return JSONResponse(result)


@app.get("/branch/{branch_id}")
def get_branch(branch_id):
    result = {
        "branch_name": "Dubai Mall",
        "branch_id": branch_id,
        "polarity_score": 72,
        "subjectivity_score": 24,
        "rating_actual": 3.7,
        "rating_rounded": 4.0,
        "rating_count": 1256,
    }
    return JSONResponse(result)


@app.get("/branch/{branch_id}/detail")
def get_branch_detail(branch_id):
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
                "rating_actual": 3.4,
                "rating_rounded": 3.5,
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


@app.get("/branch/{branch_id}/chart")
def get_branch_chart(branch_id):
    result = {
        "chart_rating": [
            {"date": "Date:2023-10-09T17:48:35Z", "rating": "4.1"},
            {"date": "Date:2023-10-10T17:48:35Z", "rating": "4.4"},
            {"date": "Date:2023-10-11T17:48:35Z", "rating": "4.9"},
            {"date": "Date:2023-10-12T17:48:35Z", "rating": "4.8"},
            {"date": "Date:2023-10-13T17:48:35Z", "rating": "4.0"},
            {"date": "Date:2023-10-14T17:48:35Z", "rating": "3.1"},
            {"date": "Date:2023-10-15T17:48:35Z", "rating": "3.5"},
            {"date": "Date:2023-10-16T17:48:35Z", "rating": "4.1"},
        ],
    }
    return JSONResponse(result)
