#ifndef __STUDENT_H_
#define __STUDENT_H_


template <typename T>
void CP::vector<T>::erase_many(const std::vector<int> &pos) {
  //write your code here
  int sz = this->size();
  vector <bool> mark(sz);
  for(int i : pos) {
    mark[i] = true;
  }
  vector <T> tmp;
  for(int i = 0; i < sz; i++) {
    if(!mark[i]) {
      tmp.push_back(this->mData[i]);
    }
  }
  this->operator=(tmp);
}

#endif
