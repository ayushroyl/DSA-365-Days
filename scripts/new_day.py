
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
DAYS = ROOT / "Days"

DAYS.mkdir(exist_ok=True)

# Find the latest day folder
existing_days = []

for folder in DAYS.iterdir():
    match = re.fullmatch(r"Day-(\d{3})", folder.name)
    if folder.is_dir() and match:
        existing_days.append(int(match.group(1)))

next_day = max(existing_days, default=0) + 1

if next_day > 365:
    print("Congratulations! All 365 days completed.")
    raise SystemExit

folder = DAYS / f"Day-{next_day:03d}"

if folder.exists():
    print("This day already exists.")
    raise SystemExit

print(f"\nCreating Day {next_day:03d}")

problem = input("Problem name: ").strip() or "To be decided"
topic = input("DSA topic: ").strip() or "To be decided"
difficulty = input("Difficulty: ").strip() or "Medium"

folder.mkdir()

solution = '''"""
Day: {day:03d}
Problem: {problem}
Topic: {topic}
Difficulty: {difficulty}
"""

def solve():
    # Write your solution here
    pass


if __name__ == "__main__":
    solve()
'''.format(
    day=next_day,
    problem=problem,
    topic=topic,
    difficulty=difficulty
)

readme = f"""# Day {next_day:03d} - {problem}

**Topic:** {topic}

**Difficulty:** {difficulty}

## Problem
Write the problem statement here.

## Approach
Explain your logic.

## Time Complexity
O(...)

## Space Complexity
O(...)

## Edge Cases
1.
2.
3.

## What I Learned
Write your learning here.
"""

(folder / "solution.py").write_text(solution)
(folder / "README.md").write_text(readme)

print(f"\nDay {next_day:03d} created successfully!")
print(f"Location: {folder}")
print("Start solving your problem!")
