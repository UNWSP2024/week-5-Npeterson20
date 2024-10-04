# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

# 247

# + 129

import random

# Function to create a quiz and check the answer
def math_quiz():
    # Generate two random numbers between 1 and 500
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    
    # Display the math problem
    print(f"{num1}\n+ {num2}\n------")
    
    # Ask the student to enter the answer
    student_answer = int(input("Enter your answer: "))
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Check if the student's answer is correct
    if student_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

# Main program
def main():
    # Call the math_quiz function
    math_quiz()

# Call the main function
if __name__ == "__main__":
    main()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
