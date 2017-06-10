// Header file for orb.c 
//
// *** THIS HEADER FILE SHOULD NOT BE MODIFIED ***
// *** except to set _orb_radius = 1.0e-6 as  ***
// *** required in the assignment             ***
//
// Contains data structure for the orb
//
// Contains following routines 
//
//    query_orb(unsigned int x, unsigned int y)
//	- check location (x,y) to determine distance from orb
//
//    initialize_orb(unsigned int seed, unsigned int nanosleep_ntime)
//	- initialize orb to a random location 
//        and initialize delay for each query_orb() calls
//
//    get_orb_radius()
//      - return orb radius
//
//    get_annulus_width()
//      - return annulus width
//
//    get_domain_size() 
//      - return domain size
//
//   print_orb_location() 
//      - print orb location for information purpose
//
#include <stdlib.h>
#include <math.h>
#include <time.h>

// -------------------------------------------------------------------------
// Data structures for orb and domain

struct orb_struct {
    double x;  	// x-coordinate of orb
    double y;  	// y-coordinate of orb
};
struct orb_struct orb;	       	// Orb

double _domain_size = 1.0e4;	// Size of domain where the orb is placed
double _annulus_radius = 1.0e2;	// Radius of annular region where d is non-negative
double _annulus_width = 2.0;	// Thickness of annular region where d is non-negative

double _orb_radius = 1e-6;	// Radius of orb
				// Radius set to 20 for testing serial sample code in orb.c
				// HW requires working with _orb_radius = 1.0e-6 



struct timespec delay;	       	// forced delay in each query_orb() call

// -------------------------------------------------------------------------
// Routines

// Compute distance d between (x,y) and orb
// - Returns d if d < _orb_radius
// - Returns d if d between _annulus_radius-_annulus_width/2 
//   and _annulus_radius+_annulus_width/2
// - Returns -1 otherwise
//
double query_orb(double x, double y) {
    nanosleep(&delay, NULL);
    double d = sqrt((x-orb.x)*(x-orb.x) + (y-orb.y)*(y-orb.y)); 
    if ((d < _orb_radius) || 
        ((d > _annulus_radius-_annulus_width/2) && 
	 (d < _annulus_radius+_annulus_width/2))) {
	return d; 
    } else {
	return -1.0; 
    }
}

// Initialize orb location and delay for each query_orb call
void initialize_orb(unsigned int seed, int delay_nsecs) {
    // Initialize location of orb to random grid location
    srand48(seed); 
    orb.x = drand48() * (_domain_size - (_annulus_radius+_annulus_width/2)); 
    orb.y = drand48() * (_domain_size - (_annulus_radius+_annulus_width/2)); 
    // Intialize delay
    delay.tv_sec = delay_nsecs/1000000000;
    delay.tv_nsec = 0;
}

// Determine orb radius 
double get_orb_radius() {
    return _orb_radius;
}

// Determine annulus width 
double get_annulus_width() {
    return _annulus_width;
}

// Determine grid size 
double get_domain_size() {
    return _domain_size;
}

// Print orb location 
void print_orb_location() {
    printf("True Orb Location = (%f, %f)\n", orb.x, orb.y); 
}
