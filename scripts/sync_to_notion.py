#!/usr/bin/env python3
"""
Syncs NeetCode auto-commits (from NeetCode's GitHub Sync feature) into the
Notion DSA Log database. Runs inside GitHub Actions — place at scripts/sync_to_notion.py
in your neetcode-submissions repo, alongside .github/workflows/sync-to-notion.yml.

Requires two GitHub Actions secrets (Settings -> Secrets and variables -> Actions):
  NOTION_TOKEN        - Internal integration secret from notion.so/my-integrations
  NOTION_DATABASE_ID  - The DSA Log database ID (already set for you below as a default,
                         override via secret if you ever recreate the database)

stdlib only, no pip install needed.
"""

import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime, timedelta, timezone

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "7971e8ea1d324d9ab5bd333ebc545d9a")
NOTION_VERSION = "2022-06-28"
NOTION_API = "https://api.notion.com/v1"

COMMIT_RE = re.compile(r"^Add:\s+(?P<slug>[a-z0-9\-]+)\s+-\s+submission-\d+", re.IGNORECASE)

# Known slug -> (Problem Name, Topic, Difficulty). Extend this as new problems appear —
# anything not in here still gets logged, just flagged for you to tag manually in Notion.
SLUG_MAP = {
    "is-anagram": ("Valid Anagram", "Arrays & Hashing", "Easy"),
    "two-integer-sum": ("Two Sum", "Arrays & Hashing", "Easy"),
    "anagram-groups": ("Group Anagrams", "Arrays & Hashing", "Medium"),
    "top-k-elements-in-list": ("Top K Frequent Elements", "Arrays & Hashing", "Medium"),
    "duplicate-integer": ("Contains Duplicate", "Arrays & Hashing", "Easy"),
    "string-encode-and-decode": ("Encode and Decode Strings", "Arrays & Hashing", "Medium"),
    "products-of-array-discluding-self": ("Product of Array Except Self", "Arrays & Hashing", "Medium"),
    "valid-sudoku": ("Valid Sudoku", "Arrays & Hashing", "Medium"),
    "longest-consecutive-sequence": ("Longest Consecutive Sequence", "Arrays & Hashing", "Medium"),
    "is-palindrome": ("Valid Palindrome", "Two Pointers", "Easy"),
    "two-integer-sum-ii": ("Two Sum II", "Two Pointers", "Medium"),
    "three-integer-sum": ("3Sum", "Two Pointers", "Medium"),
    "max-water-container": ("Container With Most Water", "Two Pointers", "Medium"),
    "trapping-rain-water": ("Trapping Rain Water", "Two Pointers", "Hard"),
    "buy-and-sell-crypto": ("Best Time to Buy/Sell Stock", "Sliding Window", "Easy"),
    "longest-substring-without-duplicates": ("Longest Substring Without Repeating Characters", "Sliding Window", "Medium"),
    "longest-repeating-substring-with-replacement": ("Longest Repeating Character Replacement", "Sliding Window", "Medium"),
    "permutation-string": ("Permutation in String", "Sliding Window", "Medium"),
    "sliding-window-maximum": ("Sliding Window Maximum", "Sliding Window", "Hard"),
    "minimum-window-with-characters": ("Minimum Window Substring", "Sliding Window", "Hard"),
    "validate-parentheses": ("Valid Parentheses", "Stack", "Easy"),
    "minimum-stack": ("Min Stack", "Stack", "Medium"),
    "evaluate-reverse-polish-notation": ("Evaluate Reverse Polish Notation", "Stack", "Medium"),
    "daily-temperatures": ("Daily Temperatures", "Stack", "Medium"),
    "car-fleet": ("Car Fleet", "Stack", "Medium"),
    "largest-rectangle-in-histogram": ("Largest Rectangle in Histogram", "Stack", "Hard"),
    "binary-search": ("Binary Search", "Binary Search", "Easy"),
    "search-2d-matrix": ("Search a 2D Matrix", "Binary Search", "Medium"),
    "eating-bananas": ("Koko Eating Bananas", "Binary Search", "Medium"),
    "find-minimum-in-rotated-sorted-array": ("Find Minimum in Rotated Sorted Array", "Binary Search", "Medium"),
    "find-target-in-rotated-sorted-array": ("Search in Rotated Sorted Array", "Binary Search", "Medium"),
    "time-based-key-value-store": ("Time Based Key-Value Store", "Binary Search", "Medium"),
    "median-of-two-sorted-arrays": ("Median of Two Sorted Arrays", "Binary Search", "Hard"),
    "reverse-a-linked-list": ("Reverse Linked List", "Linked List", "Easy"),
    "merge-two-sorted-linked-lists": ("Merge Two Sorted Lists", "Linked List", "Easy"),
    "linked-list-cycle-detection": ("Linked List Cycle", "Linked List", "Easy"),
    "reorder-linked-list": ("Reorder List", "Linked List", "Medium"),
    "remove-node-from-end-of-linked-list": ("Remove Nth Node From End of List", "Linked List", "Medium"),
    "add-two-numbers": ("Add Two Numbers", "Linked List", "Medium"),
    "copy-linked-list-with-random-pointer": ("Copy List with Random Pointer", "Linked List", "Medium"),
    "find-duplicate-integer": ("Find the Duplicate Number", "Linked List", "Medium"),
    "lru-cache": ("LRU Cache", "Linked List", "Medium"),
}


def notion_request(method, path, body=None):
    req = urllib.request.Request(
        f"{NOTION_API}{path}",
        data=json.dumps(body).encode() if body is not None else None,
        method=method,
        headers={
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def problem_exists(name: str) -> bool:
    result = notion_request(
        "POST",
        f"/databases/{NOTION_DATABASE_ID}/query",
        {"filter": {"property": "Problem", "title": {"equals": name}}},
    )
    return len(result.get("results", [])) > 0


def create_problem_page(name, topic, difficulty, date_solved, flagged=False):
    notes = "Auto-synced from GitHub commit."
    if flagged:
        notes += " Topic/difficulty unconfirmed — new slug, please verify in Notion."
    properties = {
        "Problem": {"title": [{"text": {"content": name}}]},
        "Status": {"select": {"name": "Solved"}},
        "Review Stage": {"select": {"name": "New"}},
        "Date Solved": {"date": {"start": date_solved}},
        "Next Review": {"date": {"start": (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y-%m-%d")}},
        "Notes": {"rich_text": [{"text": {"content": notes}}]},
    }
    if topic:
        properties["Topic"] = {"select": {"name": topic}}
    if difficulty:
        properties["Difficulty"] = {"select": {"name": difficulty}}

    notion_request("POST", "/pages", {"parent": {"database_id": NOTION_DATABASE_ID}, "properties": properties})


def get_recent_commits(limit=100):
    out = subprocess.run(
        ["git", "log", f"-{limit}", "--pretty=format:%H|%ad|%s", "--date=short"],
        capture_output=True, text=True, check=True,
    ).stdout
    commits = []
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, date, msg = line.split("|", 2)
        commits.append({"sha": sha, "date": date, "message": msg})
    return commits


def main():
    commits = get_recent_commits()
    seen_slugs = set()
    created = 0
    flagged_slugs = []

    for c in commits:
        m = COMMIT_RE.match(c["message"])
        if not m:
            continue
        slug = m.group("slug").lower()
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        if slug in SLUG_MAP:
            name, topic, difficulty = SLUG_MAP[slug]
            flagged = False
        else:
            name, topic, difficulty = slug.replace("-", " ").title(), None, None
            flagged = True
            flagged_slugs.append(slug)

        if problem_exists(name):
            continue

        create_problem_page(name, topic, difficulty, c["date"], flagged=flagged)
        created += 1
        print(f"Created: {name}" + (" [FLAGGED: unknown slug, needs tagging]" if flagged else ""))

    print(f"\nDone. {created} new problem(s) added to Notion.")
    if flagged_slugs:
        print(f"Unknown slugs needing a manual SLUG_MAP entry: {flagged_slugs}")


if __name__ == "__main__":
    main()
