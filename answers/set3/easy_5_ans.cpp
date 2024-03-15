
#include <iostream>
using namespace std;

int bin_to_dec(int decimal_number){
	if (decimal_number == 0) 
		return 0; 
	else
		return (decimal_number % 2 + 10 * bin_to_dec(decimal_number / 2));
}

// Driver code 
int main(){
    cout<<"Enter 10 decimal numbers to convert into binary:"<<endl;
    int decimal_number;

    for(int i=0;i<10;i++){
        cout<<"\nEnter no:";
        cin>>decimal_number;
        cout<<"Binary Number:"<<bin_to_dec(decimal_number);
    }
	
	return 0;
}


