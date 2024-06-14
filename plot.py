import matplotlib.pyplot as plt

# Function to parse the data from the file
def parse_data(file_path):
    duty_cycle = []
    tps1_readings = []
    tps2_readings = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(',')
            if len(parts) >= 3:  # Make sure there are at least three parts
                duty_cycle.append(float(parts[0].split(':')[-1]))
                tps1_readings.append(int(parts[1].split(':')[-1]))
                tps2_readings.append(int(parts[2].split(':')[-1]))
            else:
                print("Skipping a line due to missing data:", line)
            
    return duty_cycle, tps1_readings, tps2_readings


def plot_data(duty_cycle, tps1_readings, tps2_readings):
    plt.figure(figsize=(12, 6))

    # Plotting TPS1 and TPS2 readings on the same plot
    plt.plot(duty_cycle, tps1_readings, marker='o', markersize=1, linestyle='-', color='b', label='TPS1 Readings')
    plt.plot(duty_cycle, tps2_readings, marker='o', markersize=1, linestyle='-', color='r', label='TPS2 Readings')
    
    plt.title('Duty Cycle vs TPS Readings')
    plt.xlabel('Duty Cycle')
    plt.ylabel('ADC Value')
    plt.legend()  # This adds a legend to differentiate the lines

    plt.tight_layout()  # Ensure everything fits without overlapping
    plt.show()


# Main execution block
if __name__ == '__main__':
    # Assume the file is located in the current working directory
    file_path = 'test1.txt'
    duty_cycle, tps1_readings, tps2_readings = parse_data(file_path)
    plot_data(duty_cycle, tps1_readings, tps2_readings)
