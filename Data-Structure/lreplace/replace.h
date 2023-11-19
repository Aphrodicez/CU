void replace(const T& x, list<T>& y) {
    //write your code here
    for(auto it = begin(); it != end();) {
        if(*it == x) {
            for(auto e : y) {
                insert(it, e);
            }
            erase(it);
        }
        else {
            it++;
        }
    }
}
