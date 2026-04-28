import os
import json

def merge_all_ics():
    ics_dir = "ics"
    output_file = os.path.join(ics_dir, "srilanka-holidays.ics")
    
    # Yearly holiday files
    files = [f for f in os.listdir(ics_dir) if f.endswith(".ics") and f != "srilanka-holidays.ics"]
    files.sort()
    
    # Standard VTIMEZONE for Sri Lanka
    vtimezone = [
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Colombo",
        "X-LIC-LOCATION:Asia/Colombo",
        "BEGIN:STANDARD",
        "TZOFFSETFROM:+0530",
        "TZOFFSETTO:+0530",
        "TZNAME:+0530",
        "DTSTART:19700101T000000",
        "END:STANDARD",
        "END:VTIMEZONE"
    ]
    
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
    master_content.extend(vtimezone)
    
    # Process yearly holiday files
    for filename in files:
        filepath = os.path.join(ics_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            in_event = False
            for line in f:
                line = line.strip()
                if line == "BEGIN:VEVENT":
                    in_event = True
                if in_event:
                    # Fix DTSTART/DTEND for Apple compatibility (ensure TZID if needed)
                    if line.startswith("DTSTART") and "VALUE=DATE" not in line:
                        line = line.replace("DTSTART:", "DTSTART;TZID=Asia/Colombo:")
                    if line.startswith("DTEND") and "VALUE=DATE" not in line:
                        line = line.replace("DTEND:", "DTEND;TZID=Asia/Colombo:")
                    master_content.append(line)
                if line == "END:VEVENT":
                    in_event = False

    # Process Astrology (Rahu Kalaya)
    astro_json_dir = os.path.join("json", "astrology")
    if os.path.exists(astro_json_dir):
        astro_files = os.listdir(astro_json_dir)
        astro_files.sort()
        for filename in astro_files:
            if filename.endswith(".json"):
                with open(os.path.join(astro_json_dir, filename), "r") as f:
                    events = json.load(f)
                    for e in events:
                        start = e["start"].replace("-", "").replace(":", "")
                        end = e["end"].replace("-", "").replace(":", "")
                        master_content.extend([
                            "BEGIN:VEVENT",
                            f"UID:{e['uid']}@mommy.internal",
                            f"DTSTART;TZID=Asia/Colombo:{start}",
                            f"DTEND;TZID=Asia/Colombo:{end}",
                            f"SUMMARY:{e['summary']}",
                            f"DESCRIPTION:{e['description']}",
                            "TRANSP:TRANSPARENT",
                            "END:VEVENT"
                        ])
    
    master_content.append("END:VCALENDAR")
    
    # Write with CRLF line endings (mandatory for some clients)
    with open(output_file, "wb") as f:
        f.write("\r\n".join(master_content).encode("utf-8"))
        f.write(b"\r\n")
    print(f"Successfully merged files into {output_file} with CRLF and VTIMEZONE")

if __name__ == "__main__":
    merge_all_ics()
