# Lookup Table Generator and Plotting Tool

This project includes Python and C code, which were developed with the assistance of ChatGPT. It provides tools for processing and visualizing TPS (Throttle Position Sensor) data and generating a C lookup table used for embedded applications where interpolated values based on duty cycle measurements are needed.

## Overview

The code consists of several parts:

- **Python Scripts** - For parsing data, computing averages, and plotting results.
- **C Source Files** - This stores interpolated lookup tables and access them through defined functions.

## Python Components

### `plot.py`

#### Functionality:

- Parses TPS data from multiple text files.
- Calculates and plots the average readings alongside individual runs.
- Generates a C file `lookup_table.c` that includes arrays of average TPS readings indexed by duty cycle values.

#### Usage:

- Run the script using the command: `python plot.py`

## Data Handling

- Data files should be formatted in CSV-style with columns for duty cycle, TPS1, and TPS2 readings.
- Assumes data files named `test1.txt`, `test2.txt`, ..., `testN.txt` are under a `data/` directory.

## C Components

### `lookup_table.c`

- Contains static arrays for duty cycle values and TPS readings.

### `lookup_table_helper.c`

- Provides functions to access interpolated values from the lookup tables based on a given duty cycle.

### `lookup_table.h`

- The header file declares external arrays and functions to access lookup table values.

## Building and Running

To compile the C code, ensure you have a C compiler installed and use the following command:

```bash
gcc -o lookup_app lookup_table.c lookup_table_helper.c -I

./lookup_app # unix
```
## Contributions and License
- Feel free to fork, modify, or use the software in your projects.
- No license is applied to this code, and it is available for educational and commercial quiet.

## Acknowledgements
This project was facilitated by interactions with ChatGPT, providing code design and problem-solving strategies.
