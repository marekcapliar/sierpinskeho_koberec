#include <iostream>

int main(){
    int array[10];
    int rep = 10;
    int temp;
    for(int i = 0; i < 10; i++){
        srand(i * 485);
        int rand_num = rand() % 30 + 1;
        array[i] = rand_num;
        std::cout << array[i] << ' ';
    }

    for(int i = 0; i < sizeof(array)/sizeof(array[0]); i++){
        rep -= 1;
        for(int j = 0; j < rep; j++){
            if (array[j] > array[j+1]){
                temp = array[j+1];
                array[j+1] = array[j];
                array[j] = temp;
            }
        }
    }
    std::cout << '\n';
    for(int i: array){
        std::cout << i << ' ';
    }

    return 0;
}