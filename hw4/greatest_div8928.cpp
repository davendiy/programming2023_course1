#include <iostream>
#include <cmath>
using namespace std; 

int main() {
   long long n; 
   cin >> n; 

   long long res_prod = 1; 
   long long min_mul = 1; 

   long long sqrt_n = (long long) sqrt(n); 
   
   
   for (long long i = 2; i <= sqrt_n; i++) { 
       if ((n % i) == 0) {
            

 
       
       long long i2 = ((long long) sqrt(n)) - i + 2;
       if ((n % i2) == 0)  {
          cout << i2 << endl; 
          return 0; 
       }
   } 

   cout << 1 << endl; 
}
