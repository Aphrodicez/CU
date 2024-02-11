#ifndef __STUDENT_H_
#define __STUDENT_H_

#include "map_bst.h"

template <typename KeyT,
          typename MappedT,
          typename CompareT>
int CP::map_bst<KeyT, MappedT, CompareT>::my_recur(node* n, int &aux){
	// You MAY use this function
    if(n == NULL) {
        return 0;
    }

    int longestLeft = my_recur(n->left, aux);
    int longestRight = my_recur(n->right, aux);
    
    int longestLine = 1 + std::max(longestLeft, longestRight);
    
    aux = std::max(aux, longestLeft + longestRight);
    return longestLine;
}

template <typename KeyT,
          typename MappedT,
          typename CompareT>
int CP::map_bst<KeyT, MappedT, CompareT>::furthest_distance() {
	// write your code here
    if(empty()) {
        return -1;
    }
	int aux = 0;
    my_recur(mRoot, aux);
    return aux;
}

#endif