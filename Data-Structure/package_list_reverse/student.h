#ifndef __STUDENT_H_
#define __STUDENT_H_

#include <algorithm>

template <typename T>
typename CP::list<T>::iterator CP::list<T>::reverse(iterator a, iterator b) {
    //write your code here
    if(a == b) {
        return a;
    }

    iterator before_a = a;
    before_a--;

    iterator last = a;

    for(iterator it = a; it != b; it--) {
        std::swap(it.ptr->prev, it.ptr->next);
        last = it;
    }

    before_a.ptr->next = last.ptr;
    last.ptr->prev = before_a.ptr;

    b.ptr->prev = a.ptr;
    a.ptr->next = b.ptr;

    return last;
}

#endif
