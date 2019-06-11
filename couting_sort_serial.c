#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <omp.h>

#define MAX_INTEGERS_TO_SORT 10000
#define MAX_INTEGER_RANGE 10000 - 1
#define NUM_REPETITIONS 10

void couting_sort(unsigned int A[], unsigned int B[], unsigned int C[]);

int main(int argc, char *argv[]) {  
  unsigned int *A, *B, *C;
  double mean = 0.0;
  short random = 1;
  
  A = (unsigned int *) calloc(MAX_INTEGERS_TO_SORT, sizeof(unsigned int));
  B = (unsigned int *) calloc(MAX_INTEGERS_TO_SORT, sizeof(unsigned  int)); 
  C = (unsigned int *) calloc(MAX_INTEGER_RANGE + 1, sizeof(unsigned int));

  assert (A != NULL &&
	  B != NULL &&
	  C != NULL);
  srand(time(NULL));
  
   for (int j = 0; j < NUM_REPETITIONS; j++) {
    if (random) {
      for (int i  = 0; i < MAX_INTEGERS_TO_SORT; i++) {
	A[i] = rand() % (MAX_INTEGER_RANGE + 1);
      }
    }
    else {
      for (int i = MAX_INTEGERS_TO_SORT-1; i >= 0; i--) {
	A[i] = MAX_INTEGERS_TO_SORT - i;
      }
    }
    
    clock_t cpu_time_used = clock();
    couting_sort(A, B, C);
    cpu_time_used = clock() - cpu_time_used;
    double time_taken_serial = ((double) cpu_time_used) / CLOCKS_PER_SEC;
    printf("%g segundos para executar o couting sort serial\n", time_taken_serial);
    mean += time_taken_serial;
   
    for (int i = 0; i < MAX_INTEGER_RANGE + 1; i++) {
      C[i] = 0;
    }
   }
   mean /= NUM_REPETITIONS;
   printf("Tempo médio %g\n", mean);

   free(A);
   free(B);
   free(C);
   return 0;
}

void couting_sort(unsigned int A[], unsigned int B[], unsigned int C[]) {
  for (int i = 0; i < MAX_INTEGERS_TO_SORT; i++) {
    C[A[i]] = C[A[i]] + 1;
  }
  for (int i = 1; i < MAX_INTEGER_RANGE + 1; i++) {
    C[i] = C[i] + C[i - 1];
  }
  for (int i = MAX_INTEGERS_TO_SORT - 1; i >= 0; i--) {
    B[C[A[i]] -1] = A[i];
    C[A[i]] =  C[A[i]] - 1;
  }
}
