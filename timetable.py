def create_study_timetable():
    # Define a simple weekly timetable structure
    # Days as keys, and time slots with subjects as values
    timetable = {
        'Monday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Coding',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Online Courses',
            '15:00 - 16:00': 'Coding'
        },
        'Tuesday': {
            '09:00 - 10:00': 'Physics',
            '10:00 - 11:00': 'Mathematics',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Biology',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Chemistry',
            '15:00 - 16:00': 'History'
        },
        'Wednesday': {
            '09:00 - 10:00': 'Chemistry',
            '10:00 - 11:00': 'Biology',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Mathematics',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Physics',
            '15:00 - 16:00': 'Geography'
        },
        'Thursday': {
            '09:00 - 10:00': 'Biology',
            '10:00 - 11:00': 'Chemistry',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Physics',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Mathematics',
            '15:00 - 16:00': 'English'
        },
        'Friday': {
            '09:00 - 10:00': 'Mathematics',
            '10:00 - 11:00': 'Physics',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Chemistry',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Biology',
            '15:00 - 16:00': 'History'
        },
        'Saturday': {
            '09:00 - 10:00': 'Revision - Math',
            '10:00 - 11:00': 'Revision - Science',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Project Work',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Free Study',
            '15:00 - 16:00': 'Extracurricular'
        },
        'Sunday': {
            '09:00 - 10:00': 'Rest',
            '10:00 - 11:00': 'Light Revision',
            '11:00 - 12:00': 'Break',
            '12:00 - 13:00': 'Weekly Review',
            '13:00 - 14:00': 'Lunch',
            '14:00 - 15:00': 'Relax',
            '15:00 - 16:00': 'Plan Next Week'
        }
    }
    
    # Function to print the timetable
    def print_timetable():
        print("Study Timetable")
        print("-" * 50)
        for day, schedule in timetable.items():
            print(f"\n{day}:")
            for time_slot, subject in schedule.items():
                print(f"  {time_slot}: {subject}")
        print("-" * 50)
    
    # Call to print
    print_timetable()
    
    # You can return the timetable dictionary for further use
    return timetable

if __name__ == "__main__":
    create_study_timetable()