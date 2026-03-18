def determine_grade(score):
    """Determines the letter grade based on a numeric score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calc_average(grades):
    """Calculates the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    print("--- Student Grade Analyzer ---")
    try:
        # Taking input as a comma-separated string
        raw_input = input("Enter test scores separated by commas (e.g., 95, 85, 75): ")
        grade_list = [float(score.strip()) for score in raw_input.split(',')]
        
        print("\nIndividual Results:")
        for score in grade_list:
            letter = determine_grade(score)
            print(f"Score: {score:.1f} | Grade: {letter}")
        
        average_score = calc_average(grade_list)
        average_letter = determine_grade(average_score)
        
        print("-" * 30)
        print(f"Final Average: {average_score:.2f}")
        print(f"Average Grade: {average_letter}")
        
    except ValueError:
        print("Error: Please ensure you enter numeric values separated by commas.")

if __name__ == "__main__":
    main()
