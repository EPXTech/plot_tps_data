#ifndef LOOKUP_TABLE_H
#define LOOKUP_TABLE_H

extern float duty_cycle_values[];
extern float avg_tps1_values[];
extern float avg_tps2_values[];
extern int duty_cycle_size;

float get_avg_tps1_value(float duty);
float get_avg_tps2_value(float duty);

#endif // LOOKUP_TABLE_H
