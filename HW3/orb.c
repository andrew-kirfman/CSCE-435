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


/* ------------------------------------------------------------------------- */
/* Global Variables                                                          */
/* ------------------------------------------------------------------------- */

struct timespec start, stop; 	// Do not remove
double total_time;		// Do not remove
double domain_size;		// Do not remove
double annulus_width;		// Do not remove
double orb_radius;		// Do not remove
double orb_x, orb_y; 		//Coordinates of orb (to be found)

// Variables to contain the range of acceptable random values to generate over
// This will narrow as the guesses of my program grow closer to the orb.  
double range_x, range_y;

// Thread and synchronization variables
// Thread count was chosen through experimentation to be optimal on ADA
#define NUM_THREADS 125
pthread_t pthreads[NUM_THREADS];
pthread_attr_t attr;
pthread_mutex_t range_lock;

// Global data variables
double point_1_x;
double point_1_y;
double point_2_x;
double point_2_y;
double distance1;
double distance2;
double distance3;
double current_distance;

struct thread_args
{
    int random_seed;
    short int thread_id;
};

/* ------------------------------------------------------------------------- */
/* Thread Function                                                           */
/* ------------------------------------------------------------------------- */

void *find_orb(void *arg)
{
    struct thread_args *args = (struct thread_args*) arg;

    double x_pos = 0.0;
    double y_pos = 0.0;
    double distance = 0.0;
    unsigned int seed = args->random_seed + args->thread_id;

    for(;;)
    {
        x_pos = (double)rand_r(&seed)/(double)(range_x);
        y_pos = (double)rand_r(&seed)/(double)(range_y);

        if(rand_r(&seed) % 2 == 0 && orb_x - x_pos >= 0)
        {
            x_pos = orb_x - x_pos;
        }
        else
        {
            x_pos = orb_x + x_pos;
        }

        if(rand_r(&seed) % 2 == 0 && orb_y - y_pos >= 0)
        {
            y_pos = orb_y - y_pos;
        }
        else
        {
            y_pos = orb_y + y_pos;
        }

        distance = query_orb(x_pos, y_pos);

        if(distance != -1)
        {
            pthread_mutex_lock(&range_lock);

            if(point_1_x == 0.00 && point_1_y == 0.00)
            {
                point_1_x = x_pos;
                point_1_y = y_pos;
                distance2 = distance;

                // If we've found a point that is closer to the orb than any other, 
                // start generating points closer to it.  
                if(distance < current_distance)
                {   
                    current_distance = distance;
                
                    // This is an abstraction of RAND_MAX/1 which will result in the production
                    // of a random number between 0.0 and 1.0
                    range_x = RAND_MAX;
                    range_y = RAND_MAX;

                    orb_x = x_pos;
                    orb_y = y_pos;
                }
            }
            else if(point_2_x == 0.00 && point_2_y == 0.00)
            {
                point_2_x = x_pos;
                point_2_y = y_pos;
                distance3 = distance;

                // Third distance is the distance between the two poitns
                distance1 = sqrt( pow(point_2_x - point_1_x, 2.0) + pow(point_2_y - point_1_y, 2.0) );

                // Funky trig equations sourced here: https://stackoverflow.com/questions/24970605/
                // finding-third-points-of-triangle-using-other-two-points-with-known-distances
                double cos_phi = (pow(distance1, 2.0) + pow(distance2, 2.0) - pow(distance3, 2.0)) / (2 * distance1 * distance2);
                double sin_phi = sqrt(1 - pow(cos_phi, 2.0));

                // There are two possible solutions to this equation depending on the location
                // of the various data points.  Test each one.  
                double orbx1 = point_1_x + distance2/distance1 * (cos_phi * (point_2_x - point_1_x) - sin_phi * (point_2_y - point_1_y));
                double orby1 = point_1_y + distance2/distance1 * (sin_phi * (point_2_x - point_1_x) + cos_phi * (point_2_y - point_1_y));
                
                double final_1 = query_orb(orbx1, orby1);

                if(final_1 < 1e-6 && final_1 >= 0.0)
                {
                    orb_x = orbx1;
                    orb_y = orby1;   

                    current_distance = 0.0;
                }
                else
                {
                    double orbx2 = point_1_x + distance2/distance1 * (cos_phi * (point_2_x - point_1_x) + sin_phi * (point_2_y - point_1_y));    
                    double orby2 = point_1_y + distance2/distance1 * (-1 * sin_phi * (point_2_x - point_1_x) + cos_phi * (point_2_y - point_1_y));

                    double final_2 = query_orb(orbx2, orby2); 
                                    
                    if(final_2 < 1e-6 && final_2 >= 0.0)
                    {
                        orb_x = orbx2;
                        orb_y = orby2;
                        
                        current_distance = 0.0;
                    }
                    // If we get here, we need to start over!
                    else
                    {
                        point_1_x = 0.0;
                        point_1_y = 0.0;

                        point_2_x = 0.0;
                        point_2_y = 0.0;                 

                        distance1 = 0.0;
                        distance2 = 0.0;
                        distance3 = 0.0;

                        range_x = RAND_MAX/domain_size;
                        range_y = RAND_MAX/domain_size;
                        
                        current_distance = 2 * domain_size * domain_size;
                    }   
                }
            }

            pthread_mutex_unlock(&range_lock);
        }

        if(current_distance < 0.000001)
        {
             pthread_exit(NULL);
        }
    }

    pthread_exit(NULL);
}


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


    // Initialize all of my stuff here along with the global variables
    int i = 0;
    int status = 0;
    int random_seed;
    struct thread_args args[NUM_THREADS];
    
    // Initialize pthreads variables
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
    pthread_mutex_init(&range_lock, NULL);

    // Initialize the two range variables 
    range_x = RAND_MAX/domain_size;
    range_y = RAND_MAX/domain_size;
    
    orb_x = 0.0;
    orb_y = 0.0;

    point_1_x = 0.00;
    point_1_y = 0.00;

    point_2_x = 0.00;
    point_2_y = 0.00;
    
    distance1 = 0.0;
    distance2 = 0.0;

    current_distance = 2 * domain_size * domain_size;


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
    printf("[DEBUG]: Range: %f, %f.  Distance: %f", range_x, range_y, current_distance);

    clock_gettime(CLOCK_REALTIME, &start); 	// Do not remove

    // Create all of the threads
    // Generate a random seed so that I can use it for other random seeds
    srand48(time(NULL));
    random_seed = lrand48();

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

    // Compute time taken
    clock_gettime(CLOCK_REALTIME, &stop);			// Do not remove
    total_time = (stop.tv_sec-start.tv_sec)			// Do not remove
	+0.000000001*(stop.tv_nsec-start.tv_nsec);		// Do not remove

    // Check if orb found, print time taken		
    printf("Orb = (%f,%f), distance = %e, time (sec) = %8.4f\n", // Do not remove
    orb_x, orb_y, query_orb(orb_x, orb_y), total_time);		// Do not remove

    print_orb_location(); 

    // Clean Up!
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&range_lock);
}

