import os
import json

def merge_all_ics():
    ics_dir = "ics"
    output_file = os.path.join(ics_dir, "srilanka-holidays.ics")
    
    # Yearly holiday files
    files = [f for f in os.listdir(ics_dir) if f.endswith(".ics") and f != "srilanka-holidays.ics"]
    files.sort()
    
    master_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Mommy//SL Holidays Master//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Sri Lanka Master Calendar",
        "X-WR-TIMEZONE:Asia/Colombo",
        "X-WR-CALDESC:Holidays, Poya Days, and Rahu Kalaya (2021-2028)."
    ]
    
    # Process yearly holiday files
    for filename in files:
        filepath = os.path.join(ics_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            in_event = False
            for line in f:
                if line.startswith("BEGIN:VEVENT"): in_event = True
                if in_event: master_content.append(line.strip())
                if line.startswith("END:VEVENT"): in_event = False

    # Process Astrology (Rahu Kalaya)
    astro_json_dir = "json/astrology"
    if os.path.exists(astro_json_dir):
        for filename in os.listdir(astro_json_dir):
            if filename.endswith(".json"):
                with open(os.path.join(astro_json_dir, filename), "r") as f:
                    events = json.load(f)
                    for e in events:
                        # Convert ISO timestamp to ICS format
                        start = e["start"].replace("-", "").replace(":", "")
                        end = e["end"].replace("-", "").replace(":", "")
                        master_content.extend([
                            "BEGIN:VEVENT",
                            f"UID:{e['uid']}@mommy.internal",
                            f"DTSTART:{start}",
                            f"DTEND:{end}",
                            f"SUMMARY:{e['summary']}",
                            f"DESCRIPTION:{e['description']}",
                            "TRANSP:TRANSPARENT",
                            "END:VEVENT"
                        ])
    
    master_content.append("END:VCALENDAR")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(master_content))
    print(f"Successfully merged {len(files)} files into {output_file}")

if __name__ == "__main__":
    merge_all_ics()
