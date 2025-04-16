print("🎉 Welcome to the Mad Libs Game! 🎉\n")

# Getting user input
name = input("👤 Give me a name: ")
place = input("📍 Give a place: ")
adjective = input("😂 Give me a funny adjective: ")
noun = input("📦 Enter a noun: ")
verb = input("🏃 Enter a verb: ")

# Story template
story = f"""
📖 Here’s your Mad Libs story:

Once upon a time, there was someone named {name} who lived in {place}.
One day, {name} found a very {adjective} {noun}.
Excited, {name} decided to {verb} it immediately.
And that’s how the adventure began! 🌟
"""

# Outputting the result
print(story)
