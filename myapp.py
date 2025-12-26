def create_result_sheet():
    total_marks = 500  # Assuming total possible marks are 500; you can change this
    students = []
    
    print("Enter details for 20 students:")
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ").strip()
        try:
            obtained = float(input(f"Enter obtained marks for {name} (out of {total_marks}): "))
            if obtained > total_marks or obtained < 0:
                print("Invalid marks. Marks should be between 0 and total marks.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number for marks.")
            continue
        
        percentage = (obtained / total_marks) * 100
        
        if percentage >= 90:
            grade = 'A'
        elif percentage >= 80:
            grade = 'B'
        elif percentage >= 70:
            grade = 'C'
        elif percentage >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        students.append({
            'name': name,
            'obtained': obtained,
            'total': total_marks,
            'percentage': percentage,
            'grade': grade
        })
    
    # Print the result sheet
    print("\nResult Sheet")
    print("-" * 70)
    print(f"{'Name':20} {'Obtained Marks':15} {'Total Marks':15} {'Percentage':12} {'Grade':5}")
    print("-" * 70)
    
    for student in students:
        print(f"{student['name']:20} {student['obtained']:15.2f} {student['total']:15} {student['percentage']:10.2f}% {student['grade']:5}")
    
    print("-" * 70)

if __name__ == "__main__":
    create_result_sheet()