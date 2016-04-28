
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  
  int SIZE;
  sscanf(argv[1],"%d",&SIZE);
  int sqrtSIZE = sqrt(SIZE);
  
  printf("%d %d\n",SIZE,sqrtSIZE);
  
  char *vals;
  int *primes;
  vals = (char *) calloc(SIZE,sizeof(char));
  
  for(int j=4; j < SIZE; j+=2) {
    vals[j] = 1;
  }
  for(int i=3; i < sqrtSIZE; i+=2) {
    if(vals[i] == 0) {
      for(int j=i*i; j < SIZE; j+=2*i) {
        vals[j] = 1;
      }
    }
  }
  
  int count = 0;
  for(int i=2; i<SIZE; i++) {
    if(vals[i] == 0) count ++;
  }
  
  primes = (int *) malloc(count*sizeof(int));
  
  int index = 0;
  for(int i=2; i<SIZE; i++) {
    if(vals[i] == 0) {
      primes[index] = i;
      //printf("%d, ",i);
      index++;
    }
  }
  
  return 0;
}
