# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    # WRITE YOUR CODE HERE
    # Function to convert kilometers to miles
def kilometers_to_miles(km):
    return km * 0.6214

# Main program
def main():
    # Ask the user to input distance in kilometers
    kilometers = float(input("Enter distance in kilometers: "))
    
    # Call the function to convert kilometers to miles
    miles = kilometers_to_miles(kilometers)
    
    # Display the result
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

# Call the main function
if __name__ == "__main__":
    main()  


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion
    
    # Display the miles
