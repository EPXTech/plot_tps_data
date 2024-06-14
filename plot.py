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

def plot_data(files):
    plt.figure(figsize=(12, 6))

    # Plot data from multiple files
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Color for each file
    for index, file_path in enumerate(files):
        duty_cycle, tps1_readings, tps2_readings = parse_data(file_path)
        plt.plot(duty_cycle, tps1_readings, marker='o', markersize=1, linestyle='-', color=colors[index % len(colors)], label=f'{file_path} - TPS1')
        plt.plot(duty_cycle, tps2_readings, marker='o', markersize=1, linestyle='-', color=colors[index % len(colors)], label=f'{file_path} - TPS2', alpha=0.5)

    plt.title('Duty Cycle vs TPS Readings Across Files')
    plt.xlabel('Duty Cycle')
    plt.ylabel('ADC Value')
    plt.legend(loc='upper left', fontsize='small')  # Adjust legend position and size
    plt.tight_layout()  # Ensure everything fits without overlapping
    plt.show()

# Main execution block
if __name__ == '__main__':
    files = [f'test{i}.txt' for i in range(1, 8)]  # List files from test1.txt to test7.txt
    plot_data(files)
