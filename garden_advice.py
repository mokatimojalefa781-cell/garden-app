"""
Garden Advice App
Provides gardening advice based on the current month.

This version uses a dictionary to store seasons and advice,
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
    """
    Return gardening advice based on the month provided.

    Args:
        month (str): Name of the month (lowercase)

    Returns:
        str: Advice for gardening
    """
    for season in SEASON_ADVICE.values():
        if month in season["months"]:
            return season["advice"]
    return "Invalid month entered."


def main():
    """Main function to run the app."""
    month = input("Enter the current month: ").lower()
    print(get_garden_advice(month))


if __name__ == "__main__":
    main()


print("🌱 Tip: Water your garden early in the morning.")

