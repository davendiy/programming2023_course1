
#include <iostream>


int main() { 
  long long n; 
  std::cin >> n; 
  std::cout << n; 
  int i = 1; 
  while (n > 1){ 
    n = n / i; 
    i += 1;
  }

  if (i == 1) std::cout << 1 << std::endl; 
  else std::cout << (i - 1) << std::endl;
  return 0; 
}

