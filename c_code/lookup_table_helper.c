#include "lookup_table.h"

// Simple linear interpolation function
float interpolate(float x0, float y0, float x1, float y1, float x) {
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0);
}

float get_avg_tps1_value(float duty) {
    for (int i = 0; i < duty_cycle_size - 1; i++) {
        if (duty >= duty_cycle_values[i] && duty <= duty_cycle_values[i + 1]) {
            return interpolate(duty_cycle_values[i], avg_tps1_values[i], duty_cycle_values[i + 1], avg_tps1_values[i + 1], duty);
        }
    }
    return -1; // Error or out of range
}

float get_avg_tps2_value(float duty) {
    for (int i = 0; i < duty_cycle_size - 1; i++) {
        if (duty >= duty_cycle_values[i] && duty <= duty_cycle_values[i + 1]) {
            return interpolate(duty_cycle_values[i], avg_tps2_values[i], duty_cycle_values[i + 1], avg_tps2_values[i + 1], duty);
        }
    }
    return -1; // Error or out of range
}
