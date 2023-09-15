#include <iostream>

int main(){
    double temperature;
    double conversion;
    char unit;

    std::cout << "Enter temperature: ";
    std::cin >> temperature;
    std::cout << "Enter unit (C or F): ";
    std::cin >> unit;

    if(unit == 'C'){
        conversion = temperature * 9/5 + 32;
        std::cout << "The temperature is " << conversion << " F";
    }
    else if(unit = 'F'){
        conversion = (temperature - 32) * 5/9;
        std::cout << "The temperature is " << conversion << " C";
    }
    else{
        std::cout << "You have entered an invalid unit";
    }

    return 0;
}