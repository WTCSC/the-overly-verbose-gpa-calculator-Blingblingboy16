number_of_classes = int(input("How many classes are you in?"))
# maybe
grades = []
for i in range(number_of_classes):
    grades.append(float(input(f"Enter your grade for class {i+1} :")))

gpa = sum(grades) / len(grades)

print(gpa)