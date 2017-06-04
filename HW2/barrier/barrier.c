//
// Implement a barrier for the threads; threads must wait at the barrier
// for all threads to reach it before going beyond
//
// Warning: Return values of calls are not checked for error to keep 
// the code simple.
//
// Compilation command on ADA ($ sign is the shell prompt):
//   module load intel/2017A
//   icc -o barrier.exe barrier.c -lpthread -lrt
//
// Sample execution and output:
//   $ ./barrier.exe 16
//   Threads = 16, barrier time (sec) =   1.0030
//
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "csce435.h"

#define MAX_THREADS     65536

int num_threads;		// Number of threads to create - user input 

int thread_id[MAX_THREADS];	// User defined id for thread
pthread_t p_threads[MAX_THREADS];// Threads
pthread_attr_t attr;		// Thread attributes 

pthread_mutex_t lock_barrier;	// Protects count
pthread_cond_t cond_barrier;	// Monitors count
int count;			// Count of threads that have reached barrier

// Simple barrier routine
void barrier_simple () 
{
    // Lock the mutex so that count can be incremented.
    pthread_mutex_lock(&lock_barrier);

    // Increment count
    count = count + 1;

    if(count == num_threads)
    {
        // Signal all waiting threads to tell them to wake up
        pthread_cond_broadcast(&cond_barrier);

        // Unlock the mutex
        pthread_mutex_unlock(&lock_barrier);

        return;
    }

    pthread_cond_wait(&cond_barrier, &lock_barrier);
    pthread_mutex_unlock(&lock_barrier);

    return;
}

void *start_func(void *s) {
    int my_thread_id = *((int *)s);
    work(my_thread_id, num_threads); 	// defined in csce435.h
    barrier_simple();
    pthread_exit(NULL);
}

// Main program - creates threads, each thread excutes barrier routine
int main(int argc, char *argv[]) {

    struct timespec start, stop; 
    double total_time, time_res;
    int i; 

    if (argc != 2) {
	printf("Need one integers as input \n"); 
	printf("Use: <executable_name> <num_threads>\n"); 
	exit(0);
    }
    if ((num_threads = atoi(argv[argc-1])) > MAX_THREADS) {
	printf("Maximum number of threads allowed: %d.\n", MAX_THREADS);
	exit(0);
    }; 

    // Initialize mutex, condition variable, and attribute structures
    pthread_mutex_init(&lock_barrier, NULL); 
    pthread_cond_init(&cond_barrier, NULL); 
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    // Initialize count
    count = 0;

    // Create threads; each thread executes find_minimum
    clock_gettime(CLOCK_REALTIME, &start); 
    for (i = 0; i < num_threads; i++) { 
	thread_id[i] = i; 
	pthread_create(&p_threads[i], &attr, start_func, (void *) &thread_id[i]); 
    }
    // Join threads
    for (i = 0; i < num_threads; i++) {
	pthread_join(p_threads[i], NULL);
    }
    // Print time taken
    clock_gettime(CLOCK_REALTIME, &stop); 
    total_time = (stop.tv_sec-start.tv_sec)
	+0.000000001*(stop.tv_nsec-start.tv_nsec);

    printf("Threads = %d, barrier time (sec) = %8.4f", 
	    num_threads, total_time);

    clock_getres(CLOCK_REALTIME, &stop); 
    time_res = stop.tv_sec+0.000000001*stop.tv_nsec;
    printf("\t timer resolution = %8.4e sec\n", time_res);

    // Destroy mutex and attribute structures
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&lock_barrier);
    pthread_cond_destroy(&cond_barrier);
}

