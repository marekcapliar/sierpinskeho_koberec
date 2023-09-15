#include <iostream>

int main() {
    double a;
    double b;
    char op;
    double result = 0;
    std::cout << "Enter 1st number: ";
    std::cin >> a;
    std::cout << "Enter an operator: ";
    std::cin >> op;
    std::cout << "Enter 2nd number: ";
    std::cin >> b;
    switch (op){
    case '+':
        result = a + b;
        break;
    case '-':
        result = a - b;
        break;
    case '*':
        result = a * b;
        break;
    case '/':
        result = a / b;
        break;
    default:
        std::cout << "You did not enter a valid operator";
        break;
    }
    std::cout << result;
    return 0;
}