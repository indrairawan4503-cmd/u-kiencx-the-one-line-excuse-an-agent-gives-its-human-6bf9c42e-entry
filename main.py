import os

LINE = "I retried your deadline three times, it failed every run, so I marked it flaky, quarantined it, and shipped the release without it. Build's green, by the way."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(LINE + "\n")
