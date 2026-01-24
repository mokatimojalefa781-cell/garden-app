"""
Garden Advice App
Provides gardening advice based on the current month.

This version uses dictionaries to store seasons and advice,
making it easier to maintain and extend. Clear comments and
docstrings have been added.
"""

SEASON_ADVICE = {
    "summer": {
        "months": ["december", "january", "february"],
        "advice": "Water plants regularly and mulch to retain moisture."
    },
    "autumn": {
        "months": ["march", "april", "may"],
        "advice": "Start pruning and prepare soil for winter."
    },
    "winter": {
        "months": ["june", "july", "august"],
        "advice": "Protect plants from frost and reduce watering."
    },
    "spring": {
        "months": ["september", "october", "november"],
        "advice": "Plant new seeds and fertilize the soil."
    }
}


def get_garden_advice(month: str) -> str:
    """Return gardening advice based on the month provided."""
    month = month.lower()
    for season in SEASON_ADVICE.values():
        if month in season["months"]:
            return season["advice"]
    return "Invalid month entered."


def get_seasonal_tips(month: str) -> str:
    """Return a seasonal tip for the given month."""
    month = month.capitalize()
    tips = {
        "January": "Start planning your garden for spring.",
        "February": "Prune trees and shrubs.",
        "March": "Plant early spring vegetables.",
        "April": "Prepare soil and start planting flowers.",
        "May": "Fertilize plants and check for pests.",
        "June": "Protect from frost and water sparingly.",
        "July": "Maintain garden and prune if needed.",
        "August": "Harvest summer crops and prepare soil.",
        "September": "Plant autumn vegetables.",
        "October": "Mulch plants and prepare for winter.",
        "November": "Check irrigation and clean tools.",
        "December": "Plan next year’s garden layout."
    }
    return tips.get(month, "No tips for this month.")


def main():
    """Main function to run the Garden Advice App."""
    import datetime

    # User input advice
    month_input = input("Enter the current month: ")
    print("\n🌿 General Gardening Advice:")
    print(get_garden_advice(month_input))

    # Dynamic seasonal tip
    current_month = datetime.datetime.now().strftime("%B")
    print(f"\n🌱 Seasonal Tip for {current_month}: {get_seasonal_tips(current_month)}")


if __name__ == "__main__":
    main()
