#ifndef LIST1_EXCEPTION_H_
#define LIST1_EXCEPTION_H_

#include <string>

class InvalidIndexException {
   public:
    std::string msg = "The index is invalid!";
};

class EmptyListException {
   public:
    std::string msg = "This is an empty list!";
};

class FullListException {
   public:
    std::string msg = "This list is FULL!";
};
#endif