import os

# Updated question data
questions = {
    "Easy": [
        ("Array Partition", "https://leetcode.com/problems/array-partition/"),
        ("Lemonade Change", "https://leetcode.com/problems/lemonade-change/"),
        ("Assign Cookies", "https://leetcode.com/problems/assign-cookies/"),
        ("DI String Match", "https://leetcode.com/problems/di-string-match/"),
        ("Minimum Cost to Move Chips to The Same Position", "https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/"),
        ("Two Furthest Houses With Different Colors", "https://leetcode.com/problems/two-furthest-houses-with-different-colors/")
    ],
    "Medium": [
        ("Non-overlapping Intervals", "https://leetcode.com/problems/non-overlapping-intervals/"),
        ("Minimum Add to Make Parentheses Valid", "https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/"),
        ("Minimum Suffix Flips", "https://leetcode.com/problems/minimum-suffix-flips/"),
        ("Maximum Ice Cream Bars", "https://leetcode.com/problems/maximum-ice-cream-bars/"),
        ("Score After Flipping Matrix", "https://leetcode.com/problems/score-after-flipping-matrix/"),
        ("Partition Labels", "https://leetcode.com/problems/partition-labels/")
    ]
}

def sanitize_folder_name(name):
    # Replace problematic characters
    replacements = {
        " & ": "_and_",
        "/": "_",
        " ": "_",
        ":": "",
        ",": ""
    }
    for old, new in replacements.items():
        name = name.replace(old, new)
    return name

for difficulty, q_list in questions.items():
    if not os.path.exists(difficulty):
        os.mkdir(difficulty)
    
    for q_name, q_link in q_list:
        q_folder = os.path.join(difficulty, sanitize_folder_name(q_name))
        if not os.path.exists(q_folder):
            os.mkdir(q_folder)
        
        readme_path = os.path.join(q_folder, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# {q_name}\n")
            if q_link:
                f.write(f"Link: [{q_name}]({q_link})\n")

print("Folders and README.md files created successfully.")
