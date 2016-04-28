
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  
  int *vals;
  int  SIZE;
  
  sscanf(argv[1],"%d",&SIZE);
  
  vals = (int *) calloc(SIZE,sizeof(int));
  
  for(int i=0; i<SIZE; i++) {
    for(int j=1; j<=i/2; j++) {
      if(i%j == 0) {
        vals[i] = vals[i] + j;
      }
    }
  }
  
  /*for(int i=0; i<SIZE; i++){
    printf("%d : %d\n",i,vals[i]);
  }*/
  
}
