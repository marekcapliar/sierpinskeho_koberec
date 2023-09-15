#include <iostream>
#include <cstdlib>      // rand()
#include <ctime>

using namespace std;

// int main() {
//     double price = 99.99;
//     float interest_rate = 4.67F;    // type F or it will store a double inside the float as float
//     long File_size = 90000L;
//     char letter = 'a';
//     bool is_valid = false;
//     auto x = 5;                     // auto assing any data type
//     /*using {} instead of = returns error if data type is different
//       fe. int number = 1.2; returns 1, but int number {1.2}; returns error
//       int number {} returns 0 instead of random number*/
//     int number {1.2};
//     return 0;
// }

// int main() {
//     int number = 0b11111111;    // number is written in binary
// //  int number = 0xff;             number is written in base 16 (0-9 a-f), a = 10
//     cout << number;
//     return 0;
// }

// rng
int main() {
    long elapsed_seconds = time(nullptr);
    srand(elapsed_seconds);
    int number = rand() % 10;   // number can be only 0-9
    cout << number << "\n";
    int roll_1 = rand() % 6 + 1;
    int roll_2 = rand() % 6 + 1;
    cout << roll_1 << " " << roll_2;
    return 0;
}