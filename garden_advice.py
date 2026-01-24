"""
Garden Advice App
Provides gardening tips based on the current month.
"""

MONTHLY_TIPS = {
    "january": "Plan your garden layout and order seeds.",
    "february": "Prune trees and prepare compost.",
    "march": "Plant early vegetables and herbs.",
    "april": "Prepare soil and plant flowers.",
    "may": "Mulch beds and control weeds.",
    "june": "Protect plants from frost.",
    "july": "Minimal watering and maintenance.",
    "august": "Start seedlings indoors.",
    "september": "Plant spring vegetables.",
    "october": "Fertilize soil and plant flowers.",
    "november": "Water regularly and monitor pests.",
    "december": "Harvest crops and water consistently."
}


def get_monthly_tip(month: str) -> str:
    """
    Return a gardening tip for the given month.

    Args:
        month (str): Month name in lowercase.

    Returns:
        str: Gardening tip.
    """
    return MONTHLY_TIPS.get(month, "Invalid month entered.")


def main():
    """Run the garden advice application."""
    month = input("Enter the current month: ").lower()
    print(get_monthly_tip(month))


if __name__ == "__main__":
    main()

