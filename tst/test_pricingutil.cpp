#include <gtest/gtest.h>
#include "../src/pricingutil.h"

TEST(sampleTest, sample) {
    EXPECT_EQ(4, 4);
}
TEST(PricingUtilTest, invalidInputs) {
    PricingUtil pricingUtil;

    EXPECT_THROW(pricingUtil.calcVal(-1, 0.07, 1), std::runtime_error);
    EXPECT_THROW(pricingUtil.calcVal(1, -0.07, 1), std::runtime_error);
}

TEST(PricingUtilTest, calculationTest) {
    PricingUtil pricingUtil;

    EXPECT_NEAR(pricingUtil.calcVal(1, 0.07, 1), 0.97, 0.001);
    EXPECT_NEAR(pricingUtil.calcVal(2, 0.07, 2.5), 4.85, 0.001);
    EXPECT_NEAR(pricingUtil.calcVal(1.5, 0.01, 3.2), 4.368, 0.001);

    EXPECT_NEAR(pricingUtil.getVal(), 4.368, 0.001);

}
