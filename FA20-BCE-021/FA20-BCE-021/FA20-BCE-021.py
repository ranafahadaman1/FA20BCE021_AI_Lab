#Student data in the form of a List of Dictionaries. We have 5 entries of student data.
student_data = [{
    'student_id':4,
    'course_type':'core', #or 'elective'
    'minimum_credits_required':10,
    'total_credits_taken':8
},
{
    'student_id':21,
    'course_type':'core', #or 'elective'
    'minimum_credits_required':10,
    'total_credits_taken':12
},
{
    'student_id':37,
    'course_type':'elective', #or 'elective'
    'minimum_credits_required':10,
    'total_credits_taken':8
},
{
    'student_id':44,
    'course_type':'core', #or 'elective'
    'minimum_credits_required':15,
    'total_credits_taken':8
},
{
    'student_id':53,
    'course_type':'elective', #or 'elective'
    'minimum_credits_required':18,
    'total_credits_taken':18
}]
#Each course is assumed to be of 2 Credit Hours, so courses_taken = total_credit_taken/2;

#The function defined below will take the dictionary as an argument and return the appropriate fee or discount for the student.
def calculate_fee_or_discount(student_data):
        #Initializing the fee variable
        fee=0
        courses_taken = student_data['total_credits_taken']/2
        courses_required = student_data['minimum_credits_required']/2
        if courses_required > courses_taken:  # If courses taken were less than required by end of semester
            if student_data['course_type'] == 'core': # If course type is 'core'
                fee = 50
                print(f"\nStudent with Registration No.{student_data['student_id']} should pay {fee} as a fee.\n")
            elif student_data['course_type'] == 'elective': #If course type is 'elective'
                fee = 30
                print(f"\nStudent with Registration No.{student_data['student_id']} should pay {fee} as a fee.\n")
        elif courses_taken >= courses_required: #If courses taken were more than required by end of semester
            if student_data['course_type'] == 'core': # If course type is 'core'
                if courses_taken >= 5:
                    print(f"\nStudent with Registration No. {student_data['student_id']} gets 2% discount on the total fee.\n")
            elif student_data['course_type'] == 'elective': # If course type is 'elective'
                if courses_taken >= 3:
                    print(f"\nStudent with Registration No. {student_data['student_id']} gets 3% discount on the total fee.\n")
        return

#Input the index to check the fee of the student on that index.
while(True):
    choice = input("Do you want to check fee?")
    if choice == 'yes' or choice =='y':
        index = int(input("Enter the index to check the fee:"))
        if index <=4:
            calculate_fee_or_discount(student_data[index])
        else:
            print("Index too high, choose from 0-4")
    else:
        print("Bye!")
        break