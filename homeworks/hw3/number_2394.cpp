

#include <iostream>
using namespace std; 


int main() {
    
    long long x; 
    cin >> x; 

    long long cur_dec = 1; 
    while (cur_dec < x) cur_dec *= 10; 
    while (1) { 
    	if (x < cur_dec) cur_dec /= 10; 
	if ((x * x) % (cur_dec * 10) == x) {
		cout << x << endl;
		break;
	}
	x -= 1;
    }
    return 0;
}
