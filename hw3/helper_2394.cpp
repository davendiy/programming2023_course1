#include <iostream>
using namespace std; 


int main() {
    
    long long n = 1000000000; 
    long long cur_dec = 1; 

    for (long long x = 1; x <= n; x++) { 
    	if (x > cur_dec) cur_dec *= 10; 
	if ((x * x) % (cur_dec) == x) {
		cout << x << endl;
	}
    }
    return 0;
}

