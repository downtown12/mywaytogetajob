/*
another solution
*/

bool smart_one(int x){
    int y=0;
    
    //an extreme condition
    if(x<0){
        return false;
    }
    
    //extreme condition: x=0
    //consider of x=1,..,9 btw
    if(x<10)
        return true;
    
    //this if-statement is for any input numbers end with 0, like 10 or 12321000
    //input numbers end with 0 will mistake the modulo-10 and multiply-10 operation in the below while-statement
    if(x%10 == 0)
        return false;
    
    while(x>y){
        y = 10*y + x%10;
        x/=10;
    }
    
    //an even input
    if(x==y)
        return true;
    else{
        //either x is palindrome but odd,
        //or x is not palindrom at all
        if(y/10 ==x)
            return true;
        else
            return false;
    }
}

bool another_solution(int x){
    int n_digits=0;
    int x1=x;
    int i=0;
    int end=0; //front=x,
    
    
    if(x<0)
        return false;
    //extreme condition: x=0
    //consider of x=1,..,9 btw
    if(x<10)
        return true;
    //calculate how many digits x has.
    while(x1>0){
        x1/=10;
        n_digits++;
    }
    
    x1=x;
    for(i=n_digits/2;i>0;i--){
        end = end*10 + x1%10;
        x1/=10;
        //front = front / 10;
    }
    if(n_digits%2)
        x1/=10;
        //front = front/10;
    
    
    if (end==x1)
        return true;
    else
        return false;
}

bool isPalindrome(int x) {
    return smart_one(x);
}
