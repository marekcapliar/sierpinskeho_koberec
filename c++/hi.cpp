#include <iostream>
#include <cmath>

using namespace std;    // we don't have to write std

// int main() {        // creating int and changing its value
//     int file_size = 100;
//     int counter = 0;
//     int temp = counter;
//     counter = file_size;
//     file_size = temp;
//     double sales = 9.99;
//     std::cout << file_size;
//     return 0;
// }

// int constant() {        // creating a constant
//     const double pi = 3.14;
//     return 0;
// }

// int main() {
//     int x = 10;
//     double y = 3;
//     double z = x / y;
//     // if i want to use division, int / int = int (10/3 = 3), at least 1 of variables must be double
//     x = x + 5;
//     int a = x++;    // a = 15 but x = 16
//     int b = ++x;    // x and b are increased by 1
//     std::cout << x;
//     return 0;
// }

// int main() {
//     double x = 10;
//     int y = 5;
//     double z = (x+10)/(3*y);
//     std::cout << z; 
//     return 0;
// }

// int main() {
//     int x = 10;
//     int y = 20;
//     cout << "x = " << x << endl;  //endl = \n
//     cout << "y = " << y;
//     return 0;
// }
//
// int main() {
//     int sales = 95000;
//     const double state_tax = 0.04;
//     const double county_tax = 0.02;
//     cout << "sales: " << sales << "$" << "\n"
//          << "state tax: " << sales * state_tax << "$" << "\n"
//          << "county tax: " << sales * county_tax << "$" << "\n"
//          << "total tax: " << sales * state_tax + sales * county_tax << "$";
// }

// int main() {
//     cout << "Enter temperature in F: ";
//     float Fahrenheit;
//     cin >> Fahrenheit;
//     cout << (Fahrenheit - 32) * 5/9;
//     return 0;
// }

int main() {
    double results = floor(1.2);    // floor rounds down, ceil rounds up
    cout << results << "\n";
    double x = pow(2, 3);           // pow = power of 2^3
    cout << x << "\n";
    /*
    this is a multi-line comment
    we are going to calculate the area of circle
    */
    float radius;
    const float pi = 3.14;
    cout << "radius: ";
    cin >> radius;
    float area = pi * pow(radius, 2);
    cout << area;
    return 0;
}