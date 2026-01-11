"""
Garden Advice App
Provides gardening tips based on the month and season.

TODO:
- Create functions instead of using all logic in one block
- Replace hardcoded values with data structures
- Add more detailed documentation and comments
"""

month = input("Enter the current month: ").lower()

if month in ["december", "january", "february"]:
    print("It's summer. Water plants regularly and mulch to retain moisture.")
elif month in ["march", "april", "may"]:
    print("It's autumn. Start pruning and prepare soil for winter.")
elif month in ["june", "july", "august"]:
    print("It's winter. Protect plants from frost and reduce watering.")
elif month in ["september", "october", "november"]:
    print("It's spring. Plant new seeds and fertilize the soil.")
else:
    print("Invalid month entered.")
