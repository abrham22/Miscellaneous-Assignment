#include <ctime>
#include <cstdlib>

int generateRandomNumber(){
    srand(time(0));
    return rand() % 100 * 1;
}