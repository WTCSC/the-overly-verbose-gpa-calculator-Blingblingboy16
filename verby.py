import time

# Ask how many classes
number_of_classes = int(input("At present, how many individual learning environments—classes, lectures, or academic engagements—are you actively participating in? "))

# Create a grades list with input validation
grades = []
for i in range(number_of_classes):
    while True:
        try:
            grade = float(input(f"At this time, you are requested to record the specific performance indicator—be it a number on a 4.0 scale—that accurately reflects your standing within class {i+1}: "))
            if 0.0 <= grade <= 4.0:
                grades.append(grade)
                break
            else:
                print("Please ensure your grade is between 0.0 and 4.0 on the academic scale of enlightenment.")
        except ValueError:
            print("That input appears to be non-numerical. Kindly provide a valid number between 0.0 and 4.0.")

# Calculate GPA
print("\nPlease hold momentarily while your cumulative academic standing (GPA) is being meticulously calculated...")
time.sleep(2)

gpa = sum(grades) / len(grades)
print(f"\nBased on {len(grades)} classes, your GPA is currently sitting at: {gpa:.2f}")

# Semester GPA Analysis (Slicing)
print("\nFor further introspection into your academic saga, would you like to analyze your:")
print("1. First half of classes\n2. Second half of classes")
choice = input("Please enter 1 or 2: ")

if choice == "1":
    semester_grades = grades[:len(grades)//2]
    semester_name = "first"
else:
    semester_grades = grades[len(grades)//2:]
    semester_name = "second"

semester_gpa = sum(semester_grades) / len(semester_grades)
print(f"\nYour GPA for the {semester_name} half of your classes is: {semester_gpa:.2f}")

# Compare semester GPA to overall GPA
if semester_gpa > gpa:
    print("Splendid! Your academic vigor appears to have improved in this half of the semester!")
elif semester_gpa < gpa:
    print("Alas, your scholarly radiance has dimmed slightly this term—but perseverance shall restore it!")
else:
    print("Steady as she goes! Your GPA remains a model of consistency.")

# Goal GPA Analysis
while True:
    try:
        goal_gpa = float(input("\nPray tell, what is your aspirational GPA goal (between 0.0 and 4.0)? "))
        if 0.0 <= goal_gpa <= 4.0:
            break
        else:
            print("Your goal GPA must lie within the sacred bounds of 0.0 and 4.0.")
    except ValueError:
        print("That input was not numeric. Kindly provide a valid goal GPA.")

if gpa >= goal_gpa:
    print(f"Bravo! Your current GPA of {gpa:.2f} already meets or surpasses your noble goal of {goal_gpa:.2f}!")
else:
    achievable = []
    for i, grade in enumerate(grades):
        temp_grades = grades.copy()
        temp_grades[i] = 4.0  # raise one grade to perfect
        new_gpa = sum(temp_grades) / len(temp_grades)
        if new_gpa >= goal_gpa:
            achievable.append(i + 1)

    if achievable:
        print(f"\nIf you elevate any of these classes to a shining 4.0, your goal GPA of {goal_gpa:.2f} shall be within reach:")
        for idx in achievable:
            print(f" - Class {idx}")
    else:
        print(f"\nIt appears that to reach your lofty goal of {goal_gpa:.2f}, you must raise more than one grade.")
