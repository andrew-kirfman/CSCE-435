// Mystery Orb
//
// Find the orb in a square domain 
//
// *** Lines marked "Do not remove" should be retained in your code ***
//
// Warning: Return values of calls are not checked for error to keep 
// the code simple.
//
// Requires orb.h to be in the same directory
// 
// Compilation command on ADA:
//
//   module load intel/2017A
//   icc -o orb.exe orb.c -lpthread -lrt
//
#include <pthread.h>
#include <stdio.h>
#include <time.h>

#include "orb.h"		// Do not remove


#define NUM_THREADS 50
pthread_t pthreads[NUM_THREADS];
pthread_attr_t attr;

pthread_mutex_t range_lock;


double current_distance;


struct timespec start, stop; 	// Do not remove
//clock_t start, stop;

double total_time;		// Do not remove

double domain_size;		// Do not remove
double annulus_width;		// Do not remove
double orb_radius;		// Do not remove

double orb_x, orb_y; 		//Coordinates of orb (to be found)

// Variables to contain the range of acceptable random values to generate over
// This will narrow as the guesses of my program grow closer to the orb.  
double range_x, range_y;

// -------------------------------------------------------------------------
// Data structures and multithreaded code to find orb
// ...
// ...
// ...
// ...
// ...
// ...

struct thread_args
{
    int random_seed;
    short int thread_id;
};


void *find_orb(void *arg)
{
    struct thread_args *args = (struct thread_args*) arg;

    double x_pos = 0.0;
    double y_pos = 0.0;
    double distance = 0.0;
    unsigned int seed = args->random_seed + args->thread_id;
    short int x_sign = 0;
    short int y_sign = 0;
    int status = 0;

    double test_x = 0.0;
    double test_y = 0.0;

    for(;;)
    {
        x_pos = (double)rand_r(&seed)/(double)(RAND_MAX/range_x);
        y_pos = (double)rand_r(&seed)/(double)(RAND_MAX/range_y);

        // There has to be a much better way of doing this!
        if(rand_r(&seed) % 2 == 0 && orb_x - x_pos >= 0)
        {
            x_sign = -1;   
        }
        else
        {
            x_sign = 1;
        }

        if(rand_r(&seed) % 2 == 0 && orb_y - y_pos >= 0)
        {
            y_sign = -1;
        }
        else
        {
            y_sign = 1;
        }

        test_x = orb_x + x_sign * x_pos;
        test_y = orb_y + y_sign * y_pos;

        //pthread_mutex_lock(&range_lock);

        distance = query_orb(test_x, test_y);

        //pthread_mutex_unlock(&range_lock);
 

        pthread_mutex_lock(&range_lock);

        if(distance != -1)
        {

            // If we've found a point that is closer to the orb than any other, 
            // start generating points closer to it.  
            if(distance < current_distance)
            {
                printf("Distance: %f, Current Distance: %f\n", distance, current_distance);
                printf("Orb Position: (%f, %f)\n\n", orb_x + x_sign * x_pos, orb_y + y_sign * y_pos);

                current_distance = distance;
                
                range_x = distance;
                range_y = distance;

                orb_x = test_x;
                orb_y = test_y;
            } 

        }

        pthread_mutex_unlock(&range_lock);

        if(current_distance < 0.000001)
        {
            pthread_exit(NULL);
        }
    }


    pthread_exit(NULL);
}


// -------------------------------------------------------------------------
// Main program to find orb 
int main(int argc, char *argv[]) {

    if (argc != 3) {
	printf("Need two integers as input \n"); 
	printf("Use: <executable_name> <random_seed> <delay_nanosecs>\n"); 
	exit(0);
    }
    // Initialize orb location
    int seed = (int) atoi(argv[argc-2]); 		// Do not remove
    int delay_nsecs = abs((int) atoi(argv[argc-1]));// Do not remove

    initialize_orb(seed, delay_nsecs); 			// Do not remove

    domain_size = get_domain_size();	 		// Do not remove
    annulus_width = get_annulus_width();	 	// Do not remove
    orb_radius = get_orb_radius();	 		// Do not remove

    printf("\n"); 
    printf("domain_size = %8.2f, annulus_width = %8.2f, orb_radius = %12.6f\n", domain_size, annulus_width, orb_radius); 
    printf("\n"); 
    printf("-----------------------------------------------------------------------------\n"); 
    printf("* IMPORTANT: orb_radius set to %f to ensure sample serial \n", orb_radius); 
    printf("* code in orb.c finishes in reasonable time. Make sure your \n"); 
    printf("* code works well for _orb_radius = 1.0e-6 before submitting \n"); 
    printf("* your assignement. _orb_radius can be set in orb.h.\n"); 
    printf("-----------------------------------------------------------------------------\n"); 
    printf("\n"); 

    clock_gettime(CLOCK_REALTIME, &start); 	// Do not remove

    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    pthread_mutex_init(&range_lock, NULL);

    // Initialize the two range variables 
    range_x = domain_size;
    range_y = domain_size;
    
    orb_x = 0.0;
    orb_y = 0.0;

    current_distance = 2 * domain_size * domain_size;

    printf("[DEBUG]: Range: %f, %f.  Distance: %f", range_x, range_y, current_distance);
    

    // Create all of the threads
    int i, status;

    // Generate a random seed so that I can use it for other random seeds
    srand48(time(NULL));
    int random_seed = lrand48();
    struct thread_args args[NUM_THREADS];

    for(i = 0; i<NUM_THREADS; i++)
    {
        args[i].random_seed = random_seed;
        args[i].thread_id = i;

        status = pthread_create(&pthreads[i], &attr, find_orb, (void*) &args[i]);

        

        if(status != 0)
        {
            printf("Non-zero status when creating thread #%d\n", i);
        }
    }

    // Join all of the threads
    for(i = 0; i<NUM_THREADS; i++)
    {
        pthread_join(pthreads[i], NULL);
    }




    // Multithreaded code to find orb
    // ...
    // ...
    // ... sample serial code shown below ...
    // ... extremely inefficient, executes in reasonable time 
    // ... ONLY for large orb radius (set in orb.h)
    // ... you must set _orb_radius = 1.0e-6 in orb.h to 
    // ... test your final code
    


    /* 
    double x1, y1, distance;
    int count = 0; 
    orb_x = 0.0; orb_y = 0.0; 
    for (x1 = 0.0; x1 < domain_size; x1 += orb_radius) { 
        for (y1 = 0.0; y1 < domain_size; y1 += orb_radius) { 
	    distance = query_orb(x1, y1); 
	    if ((distance > 0.0) && (distance < orb_radius)) {
		orb_x = x1; 
		orb_y = y1; 
	    } 
	}
    }
    // ...
    // ...
    // ...

    */

    // Compute time taken
    clock_gettime(CLOCK_REALTIME, &stop);			// Do not remove
    total_time = (stop.tv_sec-start.tv_sec)			// Do not remove
	+0.000000001*(stop.tv_nsec-start.tv_nsec);		// Do not remove

    // Check if orb found, print time taken		
    printf("Orb = (%f,%f), distance = %e, time (sec) = %8.4f\n", // Do not remove
    orb_x, orb_y, query_orb(orb_x, orb_y), total_time);		// Do not remove

    print_orb_location(); 

    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&range_lock);

    // Other code to wrap up things
    // ...
    // ...
    // ...

}

