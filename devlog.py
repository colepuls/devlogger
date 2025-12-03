from datetime import datetime
import subprocess

FILE = "devlog.md"
REPO_PATH = "/Users/colepuls/Desktop/projects/devlogger"

def dev_entry(project, worked_on, time_spent, notes):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""
## {timestamp}

**Project:** {project}

**Work done:** {worked_on}

**Time spent:** {time_spent}

**Notes:** {notes}
"""

def git_push_devlogmd(repo_path, commit_message):
    subprocess.run(["git", "-C", repo_path, "add", "."])
    subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message])
    subprocess.run(["git", "-C", repo_path, "push"])

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

    try:
        git_push_devlogmd(REPO_PATH, "DEVLOG: New log added.")
    except Exception as error:
        print(error)
        return
    
    print("Entry commited successfully.")
    return

if __name__ == "__main__":
    main()