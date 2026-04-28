import os

def merge_all_ics():
    ics_dir = "ics"
    output_file = os.path.join(ics_dir, "srilanka-holidays.ics")
    
    # Get all yearly ICS files and sort them
    files = [f for f in os.listdir(ics_dir) if f.endswith(".ics") and f != "srilanka-holidays.ics"]
    files.sort()
    
    master_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Mommy//SL Holidays Master//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Sri Lanka Holidays Master",
        "X-WR-TIMEZONE:Asia/Colombo",
        "X-WR-CALDESC:Official Sri Lankan Public, Bank, and Mercantile Holidays (2021-2028). Upgraded with markers (*†‡) and alarms."
    ]
    
    for filename in files:
        filepath = os.path.join(ics_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            in_event = False
            for line in f:
                if line.startswith("BEGIN:VEVENT"):
                    in_event = True
                if in_event:
                    master_content.append(line.strip())
                if line.startswith("END:VEVENT"):
                    in_event = False
                    
    master_content.append("END:VCALENDAR")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(master_content))
    print(f"Successfully merged {len(files)} files into {output_file}")

if __name__ == "__main__":
    merge_all_ics()
