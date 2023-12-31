//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"
#include <vector>

HackathonBot::HackathonBot(){
    this->balance = 100;
    this->holding = false;
    this->upWindows = 0;
    this->downWindows = 0;
    this->purchasePrice = 0;
    this->flatWindows = 0;
}

double HackathonBot::getBalance(){
    return this->balance;
}

bool HackathonBot::isHolding(){
    return this->holding;
}

void HackathonBot::takeAction(float price){
    
    if (price > this->prices.back()){
        this->upWindows++;
        this->downWindows = 0;
    }
    else if (price < this->prices.back()){
        this->downWindows++;
        this->upWindows = 0; 
    }

    if (percentageChange(this->prices.back(), price) <= 5 && percentageChange(this->prices.back(), price) >= -5){
        this->flatWindows++;
    }

    // if we are looking to buy
    if (!this->holding && this->balance >= price && (price < 52 || this->downWindows >= 5)){
        this->balance -= price;
        this->holding = true;
        this->purchasePrice = price;

    // if we are looking to sell
    } else if (this->upWindows >= 52 ||
                this->downWindows >= 47 ||
                price <= 0.38*this->purchasePrice ||
                price >= 1.89*this->purchasePrice ||
                checkSeriesConditionOne(price) ||
                checkSeriesConditionTwo(price) ||
                this->flatWindows >= 10){
        this->balance += price;
        this->holding = false; 

    }
    
    this->prices.push_back(price);
}

double HackathonBot::percentageChange(double a, double b){
    
    return (b-a)/a * 100;
}

bool HackathonBot::checkSeriesConditionOne(double currPrice){

    if (prices.size() >= 3 &&
        percentageChange(this->prices[this->prices.size()-3], this->prices[this->prices.size()-2]) >= 20 &&
        percentageChange(this->prices[this->prices.size()-2], this->prices[this->prices.size()-1]) >= -15 &&
        percentageChange(this->prices[this->prices.size()-1], currPrice) >= 30 &&
        percentageChange(this->prices[this->prices.size()-3], currPrice) >= 50){
        return true;
    }
    return false;
}

bool HackathonBot::checkSeriesConditionTwo(double currPrice){
    
    if (prices.size() >= 3 &&
        percentageChange(this->prices[this->prices.size()-3], this->prices[this->prices.size()-2]) >= -15 &&
        percentageChange(this->prices[this->prices.size()-2], this->prices[this->prices.size()-1]) >= 15 &&
        percentageChange(this->prices[this->prices.size()-1], currPrice) <= -25 &&
        percentageChange(this->prices[this->prices.size()-2], currPrice) <= -45){
        return true;
    }
    return false;
}
