#include <time.h>
int work (int thread_id, int num_threads) {
    struct timespec sleeptime;
    sleeptime.tv_sec = 0.0; sleeptime.tv_nsec = 0;
    nanosleep(&sleeptime, NULL);
    return 0;
}


