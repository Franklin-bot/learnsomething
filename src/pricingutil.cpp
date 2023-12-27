#include "pricingutil.h"
#include "stdexcept"

PricingUtil::PricingUtil() {
    this->val = 0;
}

float PricingUtil::getVal() {
    return this->val;
}

float PricingUtil::calcVal(float prevPrice, float interest, float oleoConstant){
    if (prevPrice < 0 || interest < 0){
        throw std::runtime_error("invalid input");
    }else{
        this->val =  prevPrice * (0.9 + interest) * oleoConstant;
        return this-> val;
    }
}


