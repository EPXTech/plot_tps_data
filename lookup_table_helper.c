#include "lookup_table.h"

int get_tps1_size(void) {
    return sizeof(avg_tps1) / sizeof(float);
}

int get_tps2_size(void) {
    return sizeof(avg_tps2) / sizeof(float);
}

float get_avg_tps1(int index) {
    if (index >= 0 && index < get_tps1_size()) {
        return avg_tps1[index];
    }
    return -1; // Error: index out of bounds
}

float get_avg_tps2(int index) {
    if (index >= 0 && index < get_tps2_size()) {
        return avg_tps2[index];
    }
    return -1; // Error: index out of bounds
}
