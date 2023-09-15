#include <iostream>
#include <cmath>

using std::string;

int main() {
    double a;
    double b;
    double c;
    std::cout << "Side a = ";
    std::cin >> a;
    std::cout << "Side b = ";
    std::cin >> b;
    c = sqrt(pow(a, 2) + pow(b, 2));
    std::cout << "Hypotenuse is " << c;
    string hi = "Hello";
    std::cout << hi;
    return 0;
}