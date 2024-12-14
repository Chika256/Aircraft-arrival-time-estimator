# Aircraft-arrival-time-estimator

This Python program estimates the arrival times of aircraft based on the data from a CSV file. It calculates the estimated arrival time for each flight based on its distance from the airport and its speed, then writes the estimated times to an output CSV file.

## Features

- **Flight Timetable**: The program reads flight data from a CSV file (`aircraft_data.csv`) which includes flight numbers, airports, arrival times, distances, and speeds.
- **Estimated Arrival Calculation**: It calculates the estimated arrival time based on the distance and speed.
- **User Interaction**: Users can input flight numbers to get detailed information and the estimated arrival time for that flight.
- **CSV Output**: The program writes the flight number and estimated arrival time to an output CSV file (`estimated_arrival_times.csv`).

## Prerequisites

- Python 3.x
- Basic knowledge of how to use CSV files and datetime in Python.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/aircraft-arrival-estimation.git
    ```

2. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

## How it Works

### Input Data (`aircraft_data.csv`)

The program begins by creating an input CSV file (`aircraft_data.csv`) that contains the following columns:

- **Flight Number**: The flight's identifier (e.g., AA123)
- **Airport**: The destination airport (e.g., Heathrow)
- **Arrival Time**: The scheduled arrival time (e.g., 2023-12-01 10:30:00)
- **Distance**: The distance to the airport in kilometers (e.g., 230)
- **Speed**: The aircraft's speed in meters per second (e.g., 321)

Sample data is automatically written into the `aircraft_data.csv` file when the program runs.

### Estimated Arrival Time Calculation

The program calculates the estimated arrival time using the formula:

```python
estimated_arrival_time = current_time + timedelta(hours=distance / speed)
```

Where:
- `current_time` is the current date and time.
- `distance` is the distance of the aircraft from the destination airport (in kilometers).
- `speed` is the speed of the aircraft (in meters per second).

### User Interaction

- The user can enter a flight number (e.g., `AA123`) to get information about that flight.
- If the flight exists in the timetable, the program will display details such as:
    - Flight Number
    - Airport
    - Timetabled Arrival Time
    - Distance from the airport
    - Speed
    - Estimated Arrival Time
- The estimated arrival time is calculated and written to the `estimated_arrival_times.csv` file.

### Example Usage

1. Start the program by running the script:
    ```bash
    python flight_program.py
    ```

2. The program will display the available flight options (flight numbers). For example:
    ```
    Available Flights:
    AA123
    AA234
    DL789
    EI562
    ```

3. Enter a flight number (e.g., `AA123`):
    ```
    Enter a flight number (or 'exit' to quit): AA123
    ```

4. The program will display the flight information and estimated arrival time:
    ```
    Flight Number: AA123
    Aircraft: AA123 at Heathrow
    Timetabled Arrival Time: 2023-12-01 10:30:00
    Distance from Airport: 230 km
    Aircraft Speed: 321 m/s
    Estimated Arrival Time: 2023-12-01 17:42:00
    ```

5. The estimated arrival time will be added to the `estimated_arrival_times.csv` file.

### Output Data (`estimated_arrival_times.csv`)

The estimated arrival times for the flights will be written to the output CSV file (`estimated_arrival_times.csv`), which will look like this:

Flight Number,Estimated Arrival Time AA123,2023-12-01 17:42:00 AA234,2023-12-01 17:58:00 DL789,2023-12-01 17:43:00 EI562,2023-12-01 19:30:00


