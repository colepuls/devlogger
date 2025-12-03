from datetime import datetime

FILE = "devlog.md"

def dev_entry(project, worked_on, time_spent, notes):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""
## {timestamp}

**Project:** {project}

**Work done:** {worked_on}

**Time spent:** {time_spent}

**Notes:** {notes}
"""

def main():
    project = input("Project name: ").strip()
    worked_on = input("Work done?: ").strip()
    time_spent = input("Time spent: ").strip()
    notes = input("Notes: ").strip()

    entry = dev_entry(project, worked_on, time_spent, notes)

    with open(FILE, "a", encoding="utf-8") as f:
        f.write(entry)
        f.write("\n\n")

    print(f"Entry saved to {FILE}")

if __name__ == "__main__":
    main()