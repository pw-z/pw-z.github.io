// usestock0.cpp -- the client program
// compile with stock00.cpp
#include <iostream>
#include "stock00.h"

int main(int argc, char const *argv[])
{
    Stock test_stock;
    test_stock.acquire("pwz.cc", 100, 12.34);
    test_stock.show();
    test_stock.buy(20000, 23.11);
    test_stock.show();
    test_stock.sell(100000, 315.65);
    test_stock.show();
    test_stock.buy(7820000, 423.11);
    test_stock.show();
    test_stock.sell(7710000, 7315.65);
    test_stock.show();
    return 0;
}
