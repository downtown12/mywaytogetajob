#include<iostream>
using namespace std;
int  main(){
        int n[][3] = {10,20,30,40,50,60};
        int (*p)[3];
        p=n;
        cout<<p[0][0]<<","<<*(p[0]+1)<<","<<(*p)[2]<<endl;
        return 0;

}

