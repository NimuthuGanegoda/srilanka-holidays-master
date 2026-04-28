import json
import os
from datetime import datetime, timedelta

def generate_rahu_kalaya(year):
    # Standard Rahu Kalaya mapping (Day: Start Hour, Start Min, End Hour, End Min)
    # This is based on a standard 6 AM sunrise.
    rahu_schedule = {
        0: (16, 30, 18, 0),  # Sunday
        1: (7, 30, 9, 0),    # Monday
        2: (15, 0, 16, 30),  # Tuesday
        3: (12, 0, 13, 30),  # Wednesday
        4: (13, 30, 15, 0),  # Thursday
        5: (10, 30, 12, 0),  # Friday
        6: (9, 0, 10, 30)    # Saturday
    }
    
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    events = []
    current_date = start_date
    while current_date <= end_date:
        weekday = current_date.weekday() # Monday is 0, Sunday is 6
        # Adjusting to match our 0=Sunday mapping
        rahu_weekday = (weekday + 1) % 7
        
        start_h, start_m, end_h, end_m = rahu_schedule[rahu_weekday]
        
        rahu_start = current_date.replace(hour=start_h, minute=start_m)
        rahu_end = current_date.replace(hour=end_h, minute=end_m)
        
        events.append({
            "uid": f"rahu_{year}_{current_date.strftime('%m%d')}",
            "summary": "🔴 Rahu Kalaya",
            "categories": ["Astrology", "Rahu Kalaya"],
            "start": rahu_start.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": rahu_end.strftime("%Y-%m-%dT%H:%M:%S"),
            "description": "Inauspicious time. Avoid starting new ventures."
        })
        current_date += timedelta(days=1)
        
    os.makedirs("json/astrology", exist_ok=True)
    with open(f"json/astrology/rahu_{year}.json", "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2, ensure_ascii=False)
    print(f"Generated Rahu Kalaya for {year}")

if __name__ == "__main__":
    for y in range(2021, 2029):
        generate_rahu_kalaya(y)
