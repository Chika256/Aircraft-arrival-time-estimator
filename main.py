# Importing the csv module for reading and writing CSV files
import csv
from datetime import datetime, timedelta

# Setting the names of the input and output CSV files
input_csv_file = 'aircraft_data.csv'
output_csv_file = 'estimated_arrival_times.csv'

# Opening the input CSV file for writing
with open(input_csv_file, 'w', newline='') as file:
    # Create a CSV writer
    writer = csv.writer(file)

    # Defining the header row for the CSV file
    field = ["Flight Number", "Airport", "Arrival time", "distance", "speed"]

    # Writing the header row to the CSV file
    writer.writerow(field)

    # Writing sample data to the CSV file
    writer.writerow(["AA123", "Heathrow", "2023-12-01 10:30:00", "230", "321"])
    writer.writerow(["AA234", "Heathrow", "2023-12-01 12:00:00", "310", "305"])
    writer.writerow(["DL789", "Heathrow", "2023-12-01 13:15:00", "741", "278"])
    writer.writerow(["EI562", "Heathrow", "2023-12-01 13:45:00", "567", "259"])


# Defining a class to represent the Aircraft Timetable
class AircraftTimetable:
    def __init__(self, csv_file):
        # Initialize the class with the timetable loaded from the CSV file
        self.timetable = self.load_timetable(csv_file)

    @staticmethod
    def load_timetable(csv_file):
        # Loading the timetable data from the CSV file into a list of dictionaries
        timetable = []
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                # Converting CSV row data to a dictionary
                timetable.append({
                    'flight_number': row[0],
                    'airport': row[1],
                    'arrival_time': datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'),
                    'distance': float(row[3]),
                    'speed': float(row[4])
                })
        return timetable

    def get_flight_numbers(self):
        # function to get  a list of flight numbers from the timetable
        return [entry['flight_number'] for entry in self.timetable]

    def search_timetable(self, flight_number):
        # function to Search for a specific flight in the timetable
        for entry in self.timetable:
            if entry['flight_number'] == flight_number:
                return entry
        return None


# Defining a class to calculate estimated arrival times
class AircraftArrivalEstimate:
    @staticmethod
    def calculate_estimated_arrival(current_time, distance, speed):
        # Calculating the estimated arrival time based on current time, distance, and speed
        estimated_arrival_time = current_time + timedelta(hours=distance / speed)
        return estimated_arrival_time


# Function to display available flight options
def display_flight_options(flight_numbers):
    print("Available Flights:")
    for number in flight_numbers:
        print(number)


# Function to display flight information
def display_flight_info(entry):
    print(f"Flight Number: {entry['flight_number']}")
    print(f"Aircraft: {entry['flight_number']} at {entry['airport']}")
    print(f"Timetabled Arrival Time: {entry['arrival_time']}")
    print(f"Distance from Airport: {entry['distance']} km")
    print(f"Aircraft Speed: {entry['speed']} m/s")


# Function to write estimated arrival time to the output CSV file
def write_estimated_arrival_to_csv(output_csv_file, flight_number, estimated_arrival_time):
    with open(output_csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the flight number and estimated arrival time to the output CSV file
        writer.writerow([flight_number, estimated_arrival_time])


# Main function for the flight program
def flight():
    # Sets the CSV file for the simulation
    csv_file = 'aircraft_data.csv'

    # Creates instances of the timetable and estimator classes
    timetable_system = AircraftTimetable(csv_file)
    estimator = AircraftArrivalEstimate()

    # Gets the list of flight numbers from the timetable
    flight_numbers = timetable_system.get_flight_numbers()

    # Displays available flight options
    display_flight_options(flight_numbers)

    while True:
        # Gets the user input for a flight number or 'exit' to quit
        flight_number = input("Enter a flight number (or 'exit' to quit): ").upper()

        if flight_number == 'EXIT':
            break

        # Searches for the entered flight number in the timetable
        entry = timetable_system.search_timetable(flight_number)

        if entry:
            # Displays information for the selected flight
            display_flight_info(entry)
            distance = entry['distance']
            speed = entry['speed']
            current_time = datetime.now()

            # Calculates and displays the estimated arrival time
            estimated_arrival_time = estimator.calculate_estimated_arrival(current_time, distance, speed)
            print(f"Estimated Arrival Time: {estimated_arrival_time}")

            # Writes the estimated arrival time to the output CSV file
            write_estimated_arrival_to_csv(output_csv_file, flight_number, estimated_arrival_time)
        else:
            print(f"Flight {flight_number} not found in the timetable.")


flight()
