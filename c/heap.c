
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *tree;
  int size;
  int alloc;
} heap_t;

void init(heap_t* h){
  h->tree = NULL;
  h->size = 0;
  h->alloc = 0;
}

void delete(heap_t* h){
  free(h->tree);
}

void heap_alloc(heap_t* h){
  if(h->alloc == 0) h->alloc  = 4;
  else              h->alloc *= 2;
  h->tree = (int*) realloc(h->tree, (h->alloc)*sizeof(int));
}

void push(heap_t* h, int in){
  int k = ++(h->size);
  if( h->size >= h->alloc ){
    heap_alloc(h);
  }
  for( ; k > 1 && in > h->tree[k/2]; k = k/2){
    h->tree[k] = h->tree[k/2];
  }
  h->tree[k] = in;
}

void pop(heap_t* h, int* out){

  *out = h->tree[1];
  int n = h->tree[h->size--];
  
  int a,b;
  for(int k = 1; k <= h->size ; ){
    
    a = k*2;
    b = k*2 + 1;
    
    if( a <= h->size && n < h->tree[a]){
      if( b <= h->size && n < h->tree[b] && h->tree[b] > h->tree[a]){
        h->tree[k] = h->tree[b];
        k = b;
      }
      else{
        h->tree[k] = h->tree[a];
        k = a;
      }
    }
    else if( b <= h->size && n < h->tree[b]){
      h->tree[k] = h->tree[b];
      k = b;
    }
    else{
      h->tree[k] = n;
      break;
    }
  }
}

void print_array(int* array,int size){
  for(int i = 0; i < size; i++) printf("%d ", array[i]);
  printf("\n");
}

void print(heap_t* h){
  printf("(%d/%d) ", h->size, h->alloc);
  print_array(h->tree+1, h->size);
}

void heap_sort(int* array, int size){
  heap_t heap;
  init(&heap);
  for(int i = 0; i < size; i++) push(&heap, array[i]);
  for(int i = 0; i < size; i++) pop(&heap, &array[i]);
  delete(&heap);
}
