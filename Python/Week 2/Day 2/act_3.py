def calculate_average(marks, total_marks):
    average = sum(marks) / total_marks
    return average


marks = []
total_marks = 0

while True:
    mark = int(input("Enter a mark (or 0 to finish): "))

    if mark == 0:
        break

    marks.append(mark)
    total_marks += 1

average = calculate_average(marks, total_marks)

previous_average = float(
    input("Enter the student's average for the previous term: "))

if previous_average > average:
    print("Student average down!")
else:
    print("Average mark:", average)

    if average < 60:
        print("Student failed (average lower than 60%)")
    elif average >= 60 and average <= 80:
        print("Student passed without distinction (between 60 and 80)")
    else:
        print("Student passed with distinction (equal to or over 80)")
