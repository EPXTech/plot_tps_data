#ifndef LOOKUP_TABLE_H
#define LOOKUP_TABLE_H

extern float avg_tps1[];
extern float avg_tps2[];

int get_tps1_size(void);
int get_tps2_size(void);
float get_avg_tps1(int index);
float get_avg_tps2(int index);

#endif // LOOKUP_TABLE_H
