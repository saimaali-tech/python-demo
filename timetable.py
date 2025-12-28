def create_study_timetable():
  
    timetable = {
        'Monday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Coding',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Online Courses',
            '03:00 - 04:00': 'Coding'
        },
        'Tuesday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Coding',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Online Courses',
            '03:00 - 04:00': 'Coding'
        },
        'Wednesday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Coding',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Online Courses',
            '03:00 - 04:00': 'Coding'
        },
        'Thursday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Coding',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Online Courses',
            '03:00 - 04:00': 'Coding'
        },
        'Friday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book Reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Coding',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Online Courses',
            '03:00 - 04:00': 'Coding'
        },
        'Saturday': {
            '09:00 - 10:00': 'Exercises',
            '10:00 - 11:00': 'Book Reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'Project Work',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Free Study',
            '03:00 - 04:00': 'Extracurricular'
        },
        'Sunday': {
            '09:00 - 10:00': 'Exercise',
            '10:00 - 11:00': 'Book Reading',
            '11:00 - 12:00': 'Break',
            '12:00 - 01:00': 'project work',
            '01:00 - 02:00': 'Lunch',
            '02:00 - 03:00': 'Relax',
            '03:00 - 04:00': 'Plan Next Week'
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