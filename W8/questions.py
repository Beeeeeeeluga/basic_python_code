def create_student_dictionary(student_names, assign_scores):
    """
    This function creates a dictionary of student names and scores.
    The student names are used as keys.
    The assignment scores are used as values.
    """

    # Create an empty dictionary
    student_dictionary = {}

    # Go through each student
    for i in range(len(student_names)):

        # Add the student name and score to the dictionary
        student_dictionary[student_names[i]] = assign_scores[i]

    # Return the dictionary
    return student_dictionary


# Define the student names and assignment scores
Student_name = ["Alan", "Bob", "Marco"]
assign_score = [43, 60, 100]

# Create the dictionary
D = create_student_dictionary(Student_name, assign_score)

# Display the dictionary
print(D)


def add_student(student_dictionary, name, score):
    """
    This function adds a student and score to a dictionary.
    If the name already exists, it adds a number to the name.
    """

    # Start with the original name
    new_name = name

    # Start the number at 1
    number = 1

    # Check whether the name already exists
    while new_name in student_dictionary:

        # Add a number to the name
        new_name = name + "-" + str(number)

        # Increase the number
        number = number + 1

    # Add the student to the dictionary
    student_dictionary[new_name] = score


# Create the original dictionary
D = {
    "Alan": 43,
    "Bob": 60,
    "Marco": 100
}

# Add another Bob with score 99
add_student(D, "Bob", 99)

# Display the dictionary
print(D)


def count_students_above_60(student_dictionary):
    """
    This function counts the students whose scores are greater than 60.
    It returns the number of students found.
    """

    # Set the counter to zero
    count = 0

    # Go through each student's score
    for score in student_dictionary.values():

        # Check whether the score is greater than 60
        if score > 60:

            # Increase the counter
            count = count + 1

    # Return the total number of students
    return count


# Create the dictionary
D = {
    "Alan": 43,
    "Bob": 60,
    "Marco": 100,
    "Bob-1": 99
}

# Count students with scores greater than 60
result = count_students_above_60(D)

# Display the result
print("Number of students with scores greater than 60:", result)



def add_student(student_dictionary, name, score):
    """
    This function adds a student and score to a dictionary.
    If the name already exists, it adds a number to the name.
    """

    # Start with the original name
    new_name = name

    # Start the number at 1
    number = 1

    # Find a name that does not exist in the dictionary
    while new_name in student_dictionary:
        new_name = name + "-" + str(number)
        number = number + 1

    # Add the student to the dictionary
    student_dictionary[new_name] = score


# Create the dictionary before adding the third Bob
D = {
    "Alan": 43,
    "Bob-1": 60,
    "Marco": 100,
    "Bob-2": 99
}

# Add the third Bob with score 60
add_student(D, "Bob", 60)

# Display the updated dictionary
print(D)



