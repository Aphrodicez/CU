#ifndef __STUDENT_H_
#define __STUDENT_H_

template <typename T>
bool CP::vector<T>::block_swap(iterator a, iterator b, size_t m) {
  //write your code here
  int l = a - this->begin();
  int r = b - this->begin();
  if(l > r) {
    std::swap(l, r);
  }
  int mm = m;

  int sz = this->size();

  if(mm == 0 || !(l >= 0 && r >= 0 && l + mm - 1 < sz && r + mm - 1 < sz) || (l + mm - 1 >= r)) {
    return false;
  }
  
  for(int i = 0; i < mm; i++) {
    std::swap(this->mData[l + i], this->mData[r + i]);
  }
  return true;
}

#endif
