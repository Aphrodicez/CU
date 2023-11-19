#ifndef __STACK_STUDENT_H__
#define __STACK_STUDENT_H__
#include "stack.h"

template <typename T>
void CP::stack<T>::mitosis(int a, int b)
{
    CP::stack <T> tmp;
    int size = this->size();
    for(int i = 0; i < size; i++) {
        if(i <= size - 1 - a && size - 1 - b <= i) {
            tmp.push(mData[i]);
        }
        tmp.push(mData[i]);
    }

    this->mData = new T[1]();
    this->mCap = 1;
    this->mSize = 0;

    size = tmp.mSize;
    for(int i = 0; i < size; i++) {
        this->push(tmp.mData[i]);
    }
}

#endif