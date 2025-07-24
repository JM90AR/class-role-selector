# Class Role Selector - Mini Project
# This script selects a professor and an assistant based on the classmates' ages.

def get_classmates(classmate_count):
    classmates = []

    for i in range(classmate_count):
        name = input(f"Enter the name of classmate {i + 1}: ")
        
        while True:
            try:
                age = int(input(f"Enter the age of {name}: "))
                break
            except ValueError:
                print("Please enter a valid age (integer only).")
        
        classmates.append((name, age))

    # Sort classmates by age (ascending)
    classmates.sort(key=lambda x: x[1])

    assistant = classmates[0][0]  # Youngest
    professor = classmates[-1][0]  # Oldest

    return assistant, professor

# Main execution
if __name__ == "__main__":
    print("=== Class Role Selector ===")
    assistant, professor = get_classmates(5)
    print(f"\nThe professor is: {professor} and the assistant is: {assistant}")