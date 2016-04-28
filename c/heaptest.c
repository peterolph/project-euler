
#include <stdio.h>
#include <stdlib.h>
#include "heap.c"

int main(void){
  int numbers[] = {9,3,1,0,27,43,1094,6,19,12};
  print_array(numbers,10);
  heap_sort(numbers,10);
  print_array(numbers,10);
}
