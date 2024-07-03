import os

# Question data
questions = {
    "Easy": [
        ("Two Sum", "https://leetcode.com/problems/two-sum"),
        ("Maximum Depth of Binary Tree", "https://leetcode.com/problems/maximum-depth-of-binary-tree"),
        ("Middle of the Linked List", "https://leetcode.com/problems/middle-of-the-linked-list"),
        ("Linked List Cycle", "https://leetcode.com/problems/linked-list-cycle"),
        ("Keyboard Row", "https://leetcode.com/problems/keyboard-row/"),
        ("Valid Parentheses", "https://leetcode.com/problems/valid-parentheses/"),
        ("Invert Binary Tree", "https://leetcode.com/problems/invert-binary-tree/"),
        ("Plus One", "https://leetcode.com/problems/plus-one/"),
        ("Implement Stack using Queues", "https://leetcode.com/problems/implement-stack-using-queues/"),
        ("Implement Queue using Stacks", "https://leetcode.com/problems/implement-queue-using-stacks/description/"),
        ("Find Pivot Index & Find the Middle Index in Array", "https://leetcode.com/problems/find-pivot-index/")
    ],
    "Medium": [
        ("Rotate List", "https://leetcode.com/problems/rotate-list"),
        ("Flatten Binary Tree to Linked List", "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"),
        ("Linked List Cycle II", "https://leetcode.com/problems/linked-list-cycle-ii/"),
        ("Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        ("Find All Anagrams in a String", "https://leetcode.com/problems/find-all-anagrams-in-a-string/"),
        ("Daily Temperatures", "https://leetcode.com/problems/daily-temperatures/"),
        ("Number of Islands", "https://leetcode.com/problems/number-of-islands/"),
        ("Rotate Array", "https://leetcode.com/problems/rotate-array/"),
        ("Construct Binary Tree from Preorder and Inorder Traversal", "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"),
        ("Sort List", "https://leetcode.com/problems/sort-list/"),
        ("Top K Frequent Words", "https://leetcode.com/problems/top-k-frequent-words/")
    ],
    "Hard": [
        ("Reverse Nodes in k-Group", "https://leetcode.com/problems/reverse-nodes-in-k-group"),
        ("Text Justification", "https://leetcode.com/problems/text-justification/"),
        ("Parsing A Boolean Expression", "https://leetcode.com/problems/parsing-a-boolean-expression/")
    ],
    "Bonus": [
        ("Implement MinHeap and MaxHeap", "")
    ]
}

for difficulty, q_list in questions.items():
    if not os.path.exists(difficulty):
        os.mkdir(difficulty)
    
    for q_name, q_link in q_list:
        q_folder = os.path.join(difficulty, q_name.replace(" & ", "_").replace("/", "_"))
        if not os.path.exists(q_folder):
            os.mkdir(q_folder)
        
        readme_path = os.path.join(q_folder, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# {q_name}\n")
            if q_link:
                f.write(f"Link: [{q_name}]({q_link})\n")

print("Folders and README.md files created successfully.")
