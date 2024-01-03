//
// Created by Ethan on 9/13/2023.
//

#include <vector>
#include "action.h"

#ifndef LEARNSOMETHING_HACKATHONBOT_H
#define LEARNSOMETHING_HACKATHONBOT_H

class HackathonBot {
public:
    HackathonBot();
    void takeAction(float price);
    double getBalance();
    bool isHolding();
    double percentageChange(double a, double b);
    bool checkSeriesConditionOne(double currPrice);
    bool checkSeriesConditionTwo(double currPrice);

private:
    double balance;
    bool holding;
    int upWindows;
    int downWindows;
    int totalWindows;
    int flatWindows;
    double purchasePrice;
    std::vector<double> prices;
};

#endif //LEARNSOMETHING_HACKATHONBOT_H
