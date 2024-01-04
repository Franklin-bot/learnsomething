#include <chrono>
#include <iostream>
#include <cmath>
void disasterCode(){

    std::vector<int> prime_numbers;
    prime_numbers.push_back(2);

    for (int i =0; i<2500; i++){
        std::vector<int> uniquePrimes;
        for (int j = 0; j < prime_numbers.size(); j++){  
            if (i%prime_numbers[j] == 0){
                uniquePrimes.push_back(prime_numbers[j]);
            }
        }

        if (uniquePrimes.size() == 0){
            prime_numbers.push_back(i);
        }
    }
}

int main(){

    double totalTime = 0;

    for (int i = 0; i<5; i++){
        auto start = std::chrono::high_resolution_clock::now();
        disasterCode();

        auto end = std::chrono::high_resolution_clock::now();

        totalTime += std::chrono::duration_cast<std::chrono::microseconds>(end-start).count();

    }
    std::cout << totalTime / 5;
}


