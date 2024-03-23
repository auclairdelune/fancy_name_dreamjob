import pyfiglet

# Function to print text in an artistic way
def print_artistic(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

# Main function to collect user information and display it artistically
def main():
    name = input("Enter your name: ")
    dream_job = input("Enter your dream job: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    hometown = input("Enter your home town: ")

    # Print user information in a fancy way
    print("Name:")
    print_artistic(name)
    print("Dream Job:")
    print_artistic(dream_job)
    print("Age:")
    print_artistic(age)
    print("Gender:")
    print_artistic(gender)
    print("Hometown:")
    print_artistic(hometown)



























if __name__ == "__main__":
    main()
