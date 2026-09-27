print("AI Resume Analyzer")
print("-------------------")

name = input("Enter your name: ")
skills = input("Enter your skills: ")

print("\nResume Analysis")
print("Name:", name)
print("Skills:", skills)

if "python" in skills.lower():
    print("Python skill detected!")
else:
    print("Consider learning Python for AI/ML roles.")

print("\nAnalysis completed successfully.")