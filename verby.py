import time

number_of_classes = int(input("At present, how many individual learning environments—classes, lectures, or academic engagements—are you actively participating in?"))

grades = []
for i in range(number_of_classes):
    grades.append(float(input(f"At this time, you are requested to record the specific performance indicator—be it a percentage or GPA value— that accurately reflects your standing within {i+1} :")))

print("\nPlease hold momentarily while your cumulative academic standing (GPA) is being meticulously calculated...")
time.sleep(2)

gpa = sum(grades) / len(grades)
print(f"\nAfter thorough computation and reflection, your current GPA is: {gpa:.2f}")