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

    overall_min = float('inf')
    overall_max = float('-inf')

    # First, determine the overall min and max from all files to set the range
    for file_path in files:
        _, tps1_readings, tps2_readings = parse_data(file_path)
        overall_min = min(overall_min, min(tps1_readings))
        overall_max = max(overall_max, max(tps1_readings))

    # Now plot the data, scaling ADC values to percentage of the min-max range
    for index, file_path in enumerate(files):
        duty_cycle, tps1_readings, tps2_readings = parse_data(file_path)
        # Convert readings to percentage
        tps1_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in tps1_readings]
        tps2_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in tps2_readings]

        plt.plot(duty_cycle, tps1_percent, linestyle='-', color='r', label=f'{file_path} - TPS1' if index == 0 else "")
        plt.plot(duty_cycle, tps2_percent, linestyle='-', color='b', label=f'{file_path} - TPS2' if index == 0 else "", alpha=0.5)

    plt.title('Duty Cycle vs TPS Readings Across Files (Percentage)')
    plt.xlabel('Duty Cycle (%)')
    plt.ylabel('ADC Value (%)')
    plt.grid(True)
    plt.tight_layout()  # Ensure everything fits without overlapping
    plt.show()

# Main execution block
if __name__ == '__main__':
    files = [f'test{i}.txt' for i in range(1, 40)]  # List files from test1.txt to test40.txt
    plot_data(files)
