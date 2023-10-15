class DashboardData:
    brands = {
        "1": {
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
        },
        "2": {
            "brand_name": "Sushico",
            "polarity_score": 83,
            "subjectivity_score": 6,
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
            "branch_ids": [321, 654, 987],
        },
    }

    branches = {
        "123": {
            "branch_name": "Dubai Mall",
            "branch_id": "123",
            "polarity_score": 76,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 275,
        },
        "456": {
            "branch_name": "Burc Khalifah",
            "branch_id": "456",
            "polarity_score": 72,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 352,
        },
        "789": {
            "branch_name": "Al Hilal Center",
            "branch_id": "789",
            "polarity_score": 85,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 779,
        },
        "321": {
            "branch_name": "Kanyon",
            "branch_id": "321",
            "polarity_score": 76,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 275,
        },
        "654": {
            "branch_name": "Mecidiyeköy",
            "branch_id": "654",
            "polarity_score": 72,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 352,
        },
        "987": {
            "branch_name": "Çeliktepe",
            "branch_id": "987",
            "polarity_score": 85,
            "subjectivity_score": 24,
            "rating_actual": 3.7,
            "rating_rounded": 4.0,
            "rating_count": 779,
        },
    }

    @classmethod
    def get_brand(cls, brand_id: int | str) -> dict:
        return cls.brands.get(str(brand_id), {})

    @classmethod
    def get_branch(cls, branch_id: int | str) -> dict:
        return cls.branches.get(str(branch_id), {})
