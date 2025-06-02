def read_heart_rates(file_path):
    """Reads heart rate values from a file and returns them as a list of integers."""
    with open(file_path, 'r') as file:
        heart_rates = [int(line.strip()) for line in file if line.strip().isdigit()]
    return heart_rates

def calculate_average(heart_rates):
    """Calculates the average from the listed heart rates."""
    return sum(heart_rates) / len(heart_rates)

def main():
    file_path = "sample_heart_rate.txt"
    heart_rates = read_heart_rates(file_path)

    if not heart_rates:
        print("No heart rate data found.")
        return

    avg = calculate_average(heart_rates)
    print(f" Average Heart Rate: {avg:.2f} BPM")

if __name__ == "__main__":
    main()
