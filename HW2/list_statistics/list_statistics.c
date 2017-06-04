//
// Computes the minimum of a list using multiple threads
//
// Warning: Return values of calls are not checked for error to keep 
// the code simple.
//
// Compilation command on ADA ($ sign is the shell prompt):
//  $ module load intel/2017A
//  $ icc -o list_minimum.exe list_minimum.c -lpthread -lc -lrt
//
// Sample execution and output ($ sign is the shell prompt):
//  $ ./list_minimum.exe 1000000 9
// Threads = 9, minimum = 148, time (sec) =   0.0013
//
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define MAX_THREADS     65536
#define MAX_LIST_SIZE   268435456


int num_threads;		// Number of threads to create - user input 

int thread_id[MAX_THREADS];	// User defined id for thread
pthread_t p_threads[MAX_THREADS];// Threads
pthread_attr_t attr;		// Thread attributes 

pthread_mutex_t lock_minimum;	// Protects minimum, count
pthread_cond_t cond_barrier;

int count;			// Count of threads that have updated minimum

double mean;
double standard_deviation;

int list[MAX_LIST_SIZE];	// List of values
int list_size;			// List size

// Thread routine to compute minimum of sublist assigned to thread; 
// update global value of minimum if necessary
void *find_minimum (void *s) 
{
    int j;
    int my_thread_id = *((int *)s);

    int block_size = list_size/num_threads;
    int my_start = my_thread_id*block_size;
    int my_end = (my_thread_id+1)*block_size-1;
    if (my_thread_id == num_threads-1) 
    {
        my_end = list_size-1;
    }

    // First start by computing the sum of the sublist.  This will be used to
    // compute the mean once all of the threads are done
    long int local_sum = 0;
    for (j = my_start; j <= my_end; j++) 
    {
        local_sum = local_sum + list[j];   
    }

    // Once the individual thread has computed its own local sum, update the
    // global varuiable to contain the sum.  
    
    pthread_mutex_lock(&lock_minimum);

    // Update the global sum.  For now, this will be contained inside
    // of the mean variable  

    // If you are the first thread to reach this point, then you must 
    // initialize the global sum.  
    if(count == 0)
    {
        mean = local_sum;
    }
    // Otherwise, add the local sum to the global sum
    else
    {
        mean = mean + local_sum;
    }

    // Update count
    count = count + 1;

    // If we are the last thread to run, then finish up the mean calculation
    if(count == num_threads)
    {
        // First, compute the mean!
        // This is done by taking the sum (which is currently stored in the 
        // variable for the mean) and dividing it by the total number of elements
        // in the list.  
        mean = mean / (list_size * 1.00);

        // Reset count to zero so that I can use it again later
        count = 0;

        // Signal all waiting threads to tell them to wake up
        pthread_cond_broadcast(&cond_barrier);

        // Unlock the mutex
        pthread_mutex_unlock(&lock_minimum);      
    }
    else
    {
        pthread_cond_wait(&cond_barrier, &lock_minimum);
        pthread_mutex_unlock(&lock_minimum);
    }

    // Now, we've computed the mean and every thread is at this point.  We can now
    // compute the standard deviation.  
    double local_std_dev = 0.0;    
    for (j = my_start; j <= my_end; j++) 
    {
        local_std_dev = local_std_dev + (list[j] - mean) * (list[j] - mean);
    }
 
    // Update the global standard deviation   
    pthread_mutex_lock(&lock_minimum);

    if(count == 0)
    {
        standard_deviation = local_std_dev;
    }
    else
    {
        standard_deviation = standard_deviation + local_std_dev;
    }

    // Update count
    count = count + 1;

    if(count == num_threads)
    {
        // Finish off the standard deviation calculations and update 
        // update the global standard deviation
        standard_deviation = sqrt(standard_deviation / (list_size * 1.00));

        // Signal all waiting threads to tell them to wake up
        pthread_cond_broadcast(&cond_barrier);

        // Unlock the mutex
        pthread_mutex_unlock(&lock_minimum);
    }
    else
    {
        pthread_cond_wait(&cond_barrier, &lock_minimum);
        pthread_mutex_unlock(&lock_minimum);   
    }

    // Thread exits
    pthread_exit(NULL);
}

// Main program - set up list of randon integers and use threads to find
// the minimum value; assign minimum value to global variable called minimum
int main(int argc, char *argv[]) {

    struct timespec start, stop;
    double total_time, time_res;
    double true_mean = 0.00;
    double true_std_dev = 0.00;
    int i, j; 

    if (argc != 3) {
	printf("Need two integers as input \n"); 
	printf("Use: <executable_name> <list_size> <num_threads>\n"); 
	exit(0);
    }
    if ((list_size = atoi(argv[argc-2])) > MAX_LIST_SIZE) {
	printf("Maximum list size allowed: %d.\n", MAX_LIST_SIZE);
	exit(0);
    }; 
    if ((num_threads = atoi(argv[argc-1])) > MAX_THREADS) {
	printf("Maximum number of threads allowed: %d.\n", MAX_THREADS);
	exit(0);
    }; 
    if (num_threads > list_size) {
	printf("Number of threads (%d) < list_size (%d) not allowed.\n", num_threads, list_size);
	exit(0);
    }; 

    // Initialize mutex and attribute structures
    pthread_mutex_init(&lock_minimum, NULL); 
    pthread_cond_init(&cond_barrier, NULL);
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    /* --------------------------------------------------------------------- */
    /* Initialize List and Compute True Values                               */
    /* --------------------------------------------------------------------- */

    srand48(time(0)); 	
    list[0] = lrand48(); 
    true_mean = list[0];    
    for (j = 1; j < list_size; j++) 
    {
        list[j] = lrand48();

        true_mean = true_mean + list[j];
    }

    // Calculate the true mean
    true_mean = true_mean/(list_size * 1.00);

    // Calculate the true standard deviation 
    for(j = 0; j<list_size; j++)
    {
        true_std_dev = true_std_dev + (list[j] - true_mean) * (list[j] - true_mean) * 1.00;
    }

    true_std_dev = sqrt(true_std_dev/(list_size * 1.00));

    // Initialize count
    count = 0;

    // Create threads; each thread executes find_minimum
    clock_gettime(CLOCK_REALTIME, &start);
    for (i = 0; i < num_threads; i++) {
	thread_id[i] = i; 
	pthread_create(&p_threads[i], &attr, find_minimum, (void *) &thread_id[i]); 
    }
    // Join threads
    for (i = 0; i < num_threads; i++) {
	pthread_join(p_threads[i], NULL);
    }

    // Compute time taken
    clock_gettime(CLOCK_REALTIME, &stop);
    total_time = (stop.tv_sec-start.tv_sec)
	+0.000000001*(stop.tv_nsec-start.tv_nsec);

    // Every once and a while, there are floating point rounding errors that cause minute
    // differences between the values calculated in the main program and the values calculated
    // here.  By experimentation, the errors were usually after the thousandth decimal point.  
    // In order to become less sensitive to these errors, I'll take the floor of the values
    // before doing the comparison.  That way, tiny changes past the decimal place will not
    // ruin my calculations.  
    if(floor(true_mean) != floor(mean))
    {
        printf("Mean calculation was incorrect!\n");
    }

    if(floor(true_std_dev) != floor(standard_deviation))
    {
        printf("Standard deviation calculation was incorrect! True = %f\n", true_std_dev);
    }

    // Print time taken
    printf("Threads = %d, mean = %f, std_dev = %f time (sec) = %8.4f\n", 
	    num_threads, mean, standard_deviation, total_time);

    // Destroy mutex and attribute structures
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&lock_minimum);
    pthread_cond_destroy(&cond_barrier);
}

