#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <omp.h>

#define MAX_INTEGERS_TO_SORT 1000000
#define MAX_INTEGER_RANGE 1000000
//#define NUM_THREADS 2
#define NUM_REPETITIONS 100

int NUM_THREADS = 2;
void couting_sort(unsigned int A[], unsigned int B[], unsigned int C[]);
void couting_sort_parallel(unsigned int A[], unsigned int B[], unsigned int C[]);

int main(int argc, char *argv[]) {  
  unsigned int *A, *B, *C;
  short random = 0;
  
  srand(time(NULL));
  for (int i = NUM_THREADS; i <= 256; i*=2) {
    double mean_serial_time = 0.0;
    double mean_parallel_time = 0.0;
    double speed_up = 0.0;

    NUM_THREADS = i;
  
    A = (unsigned int *) calloc(MAX_INTEGERS_TO_SORT, sizeof(unsigned int));
    B = (unsigned int *) calloc(MAX_INTEGERS_TO_SORT, sizeof(unsigned  int)); 
    C = (unsigned int *) calloc(MAX_INTEGER_RANGE + 1, sizeof(unsigned int));

    assert (A != NULL &&
	    B != NULL &&
	    C != NULL);

    printf("Número de Threads - %d \n", NUM_THREADS);
    printf("Número de Repetições - %d \n", NUM_REPETITIONS); 
    printf("Vetor de inteiros %s\n", ((random == 1) ? "Aleatórios " : "com ordenação inversa"));
    printf("Comprimento do vetor - %u\n",   MAX_INTEGERS_TO_SORT);
  
    for (int j = 0; j < NUM_REPETITIONS; j++) {
      if (random) {
	for (int i = 0; i < MAX_INTEGERS_TO_SORT; i++) {
	  A[i] = rand() % (MAX_INTEGER_RANGE + 1);
	}
      }
      else { 
	for (int i = MAX_INTEGERS_TO_SORT-1; i >= 0; i--) {
	  A[i] = i;
	}
      }

      clock_t cpu_time_used = clock();
      couting_sort(A, B, C);
      cpu_time_used = clock() - cpu_time_used;
      double time_taken_serial = ((double) cpu_time_used) / CLOCKS_PER_SEC;
      //printf("%g segundos para executar o couting sort serial\n", time_taken_serial);
      mean_serial_time += time_taken_serial;
    
      for (int i = 0; i < MAX_INTEGER_RANGE + 1; i++) {
	C[i] = 0;
      }

      double start_omp_time = omp_get_wtime();
      couting_sort_parallel(A, B, C);
      double end_omp_time = omp_get_wtime();
      double time_taken_parallel = end_omp_time - start_omp_time;
      //printf("%g segundos para executar o couting sort paralelo\n\n", time_taken_parallel);
      //printf("%g speedup \n", time_taken_serial/time_taken_parallel);
      mean_parallel_time += time_taken_parallel;
    
      for (int i = 0; i < MAX_INTEGER_RANGE + 1; i++) {
	C[i] = 0;
      }
    }
    mean_serial_time /= NUM_REPETITIONS;
    mean_parallel_time /= NUM_REPETITIONS;
    speed_up = mean_serial_time / mean_parallel_time;
    printf("Speed-up %.10g\n\n", speed_up);
  
    free(A);
    free(B);
    free(C);
  }
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

void couting_sort_parallel(unsigned int A[], unsigned int B[], unsigned int C[]) {
  #pragma omp parallel num_threads(NUM_THREADS) shared(A, B, C)
  {
    #pragma omp for
    for (int i = 0; i < MAX_INTEGERS_TO_SORT; i++) {
      C[A[i]] = C[A[i]] + 1;
    }
    #pragma omp for
    for (int i = 1; i < MAX_INTEGER_RANGE + 1; i++) {
      C[i] = C[i] + C[i - 1];
    }
    #pragma omp for
    for (int i = MAX_INTEGERS_TO_SORT - 1; i >= 0; i--) {
      B[C[A[i]] -1] = A[i];
      C[A[i]] =  C[A[i]] - 1;
    }
  }
}

