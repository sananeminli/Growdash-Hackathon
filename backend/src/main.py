from os import environ as env

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .data import DashboardData
from .sentiment import Sentiment


APP_FRONTEND_ORIGINS = env.get("APP_FRONTEND_ORIGINS", "http://157.230.114.105:5173,http://localhost:5173")

app = FastAPI(
    title="Dinamo",
    version="0.2.3",
    description="Compec x Growdash Hackathon - Dinamo Team backend api",
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


@app.get("/brand/{brand_id}", tags=["brand"])
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
    result = DashboardData.get_brand(brand_id)
    return JSONResponse(result)


@app.get("/branch/{branch_id}", tags=["branch"])
def get_branch(branch_id):
    result = {
        "branch_name": f"Nusret {branch_id}",
        "branch_id": branch_id,
        "polarity_score": 72,
        "subjectivity_score": 24,
        "rating_actual": 3.7,
        "rating_rounded": 4.0,
        "rating_count": 1256,
    }
    result = DashboardData.get_branch(branch_id)
    return JSONResponse(result)


@app.get("/branch/{branch_id}/detail", tags=["branch"])
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
        "ratings_chart": [
            4.1,
            4.4,
            4.9,
            4.8,
            4.1,
            3.1,
            3.5,
            4.1,
        ],
    }
    return JSONResponse(result)


@app.get("/branch/{branch_id}/chart", tags=["branch"])
def get_branch_chart(branch_id):
    result = [
        {"date": "2023-10-09T17:48:35Z", "rating": 4.1},
        {"date": "2023-10-10T17:48:35Z", "rating": 4.4},
        {"date": "2023-10-11T17:48:35Z", "rating": 4.9},
        {"date": "2023-10-12T17:48:35Z", "rating": 4.8},
        {"date": "2023-10-13T17:48:35Z", "rating": 4.0},
        {"date": "2023-10-14T17:48:35Z", "rating": 3.1},
        {"date": "2023-10-15T17:48:35Z", "rating": 3.5},
        {"date": "2023-10-16T17:48:35Z", "rating": 4.1},
    ]
    return JSONResponse(result)


@app.post("/sentiment", tags=["sentiment"])
def analyze_input_text(input_text: str):
    return JSONResponse(Sentiment.analyze(input_text))
