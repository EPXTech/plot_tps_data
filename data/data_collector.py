import serial
import re
import sys

def open_serial_port(port, baud_rate=9600, timeout=1):
    """Open serial port with specified parameters."""
    try:
        return serial.Serial(port, baud_rate, timeout=timeout)
    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        sys.exit(1)

def log_data_to_file(ser):
    """Logs data from the serial port to files based on specific triggers."""
    file_number = 1
    file = None
    pattern = r'\[Feed Forward Function\] (.*)'
    initiate_pattern = 'Initiate Positive Test Sweep'

    try:
        while file_number <= 40:
            line = ser.readline().decode('utf-8').strip()
            # Check if the line matches the required start
            if re.match(pattern, line):
                # print(f"Received: {line}")  # Log the line received to the user
                if initiate_pattern in line:
                    # Close the current file if open and start a new file
                    if file:
                        file.close()
                    file_name = f"test{file_number}.txt"
                    file = open(file_name, 'w')
                    file_number += 1
                    print(f"Started new log file: {file_name}")
                elif file:
                    # Write to the current file if it is open
                    file.write(line + '\n')
        
        print("Done Logging, file_number > 40")

    except KeyboardInterrupt:
        # Handle exit gracefully
        if file:
            file.close()
        ser.close()
        print("Stopped logging, closed files and serial connection.")
    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
if __name__ == '__main__':
    # Modify 'COM4' to the serial port connected to your device
    print("Starting Collection")
    ser = open_serial_port('COM4', 115200)
    log_data_to_file(ser)
