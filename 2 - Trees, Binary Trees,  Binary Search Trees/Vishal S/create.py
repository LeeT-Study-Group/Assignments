import os

# Question data
questions = {
    "Easy": [
        ("Binary Tree Inorder Traversal", "https://leetcode.com/problems/binary-tree-inorder-traversal/"),
        ("Binary Tree Preorder Traversal", "https://leetcode.com/problems/binary-tree-preorder-traversal/"),
        ("Binary Tree Postorder Traversal", "https://leetcode.com/problems/binary-tree-postorder-traversal/"),
        ("Convert Sorted Array to Binary Search Tree", "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"),
        ("Search in a Binary Search Tree", "https://leetcode.com/problems/search-in-a-binary-search-tree/"),
        ("Leaf-Similar Trees", "https://leetcode.com/problems/leaf-similar-trees/"),
        ("Increasing Order Search Tree", "https://leetcode.com/problems/increasing-order-search-tree/")
    ],
    "Medium": [
        ("Balance a Binary Search Tree", "https://leetcode.com/problems/balance-a-binary-search-tree/"),
        ("Lowest Common Ancestor of a Binary Search Tree", "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/"),
        ("Insert into a Binary Search Tree", "https://leetcode.com/problems/insert-into-a-binary-search-tree/"),
        ("Even Odd Tree", "https://leetcode.com/problems/even-odd-tree/"),
        ("Reverse Odd Levels of Binary Tree", "https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/")
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
