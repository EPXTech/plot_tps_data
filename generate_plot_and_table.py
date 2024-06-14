import matplotlib.pyplot as plt

def parse_data(file_path):
    duty_cycle = []
    tps1_readings = []
    tps2_readings = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(',')
            if len(parts) >= 3:
                duty_cycle.append(float(parts[0].split(':')[-1]))
                tps1_readings.append(int(parts[1].split(':')[-1]))
                tps2_readings.append(int(parts[2].split(':')[-1]))
            else:
                print("Skipping a line due to missing data:", line)
    return duty_cycle, tps1_readings, tps2_readings

def generate_lookup_table(duty_cycle, avg_tps1, avg_tps2, filename='c_code/lookup_table.c'):
    with open(filename, 'w') as file:
        file.write('/* Lookup Table Generated from Average TPS Readings */\n')
        file.write('#include "lookup_table.h"\n\n')
        file.write('float duty_cycle_values[] = {' + ', '.join(f'{x:.2f}' for x in duty_cycle) + '};\n')
        file.write('float avg_tps1_values[] = {' + ', '.join(f'{x:.2f}' for x in avg_tps1) + '};\n')
        file.write('float avg_tps2_values[] = {' + ', '.join(f'{x:.2f}' for x in avg_tps2) + '};\n')
        file.write('int duty_cycle_size = sizeof(duty_cycle_values) / sizeof(float);\n')


def plot_data(files):
    plt.figure(figsize=(12, 6))
    overall_min = float('inf')
    overall_max = float('-inf')
    all_tps1 = []
    all_tps2 = []
    duty_cycle = []  # Initialize duty_cycle list

    for file_path in files:
        duty_cycle_values, tps1_readings, tps2_readings = parse_data(file_path)
        overall_min = min(overall_min, min(tps1_readings + tps2_readings))
        overall_max = max(overall_max, max(tps1_readings + tps2_readings))
        all_tps1.append(tps1_readings)
        all_tps2.append(tps2_readings)
        if not duty_cycle:  # Ensure duty_cycle is only set once if all files are the same
            duty_cycle = duty_cycle_values

    avg_tps1 = [sum(x)/len(x) for x in zip(*all_tps1)]
    avg_tps2 = [sum(x)/len(x) for x in zip(*all_tps2)]
    avg_tps1_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in avg_tps1]
    avg_tps2_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in avg_tps2]

    # Generate C lookup table from averages
    generate_lookup_table(duty_cycle, avg_tps1_percent, avg_tps2_percent)  # Corrected call

    for index, file_path in enumerate(files):
        duty_cycle, tps1_readings, tps2_readings = parse_data(file_path)
        tps1_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in tps1_readings]
        tps2_percent = [(val - overall_min) / (overall_max - overall_min) * 100 for val in tps2_readings]
        plt.plot(duty_cycle, tps1_percent, linestyle='-', color='r', label=f'{file_path} - TPS1' if index == 0 else "")
        plt.plot(duty_cycle, tps2_percent, linestyle='-', color='b', label=f'{file_path} - TPS2' if index == 0 else "", alpha=0.5)

    plt.plot(duty_cycle, avg_tps1_percent, linestyle='-', color='black', label='Average TPS1')
    plt.plot(duty_cycle, avg_tps2_percent, linestyle='-', color='black', label='Average TPS2', alpha=0.7)
    plt.title('Duty Cycle vs TPS Readings Across Files (Percentage)')
    plt.xlabel('Duty Cycle (%)')
    plt.ylabel('ADC Value (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Main execution block
if __name__ == '__main__':
    files = [f'data/test{i}.txt' for i in range(1, 40)]
    plot_data(files)
