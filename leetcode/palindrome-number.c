/*
smart_one:

	this solution use a number y to record the low digits reversely of the imput number x. Meanwhile cut x's one low digit.while x>y, repeat this operation.
The procedures is like:
x: 12321	x: 1232		x: 123		x:12
y: 0 		y: 1		y: 12		y:123

when y>=x, stop the operation above and check:
if y == x: then x is palindrome as well as an even number.such as orginally x is 123321.(after these operations x=123, y=123).

if y>x: then cut the lowest digit of y and check:
		if now y ==x, then y is palindrome as well as an odd number.
		else x is not palindrome.

NOTE one special condition: 
	if the original x contain zeros at the end. These zeros will affect the operations above and mistake the result(because zeros affect the value of y). like 10 and 12321000 are not palindrome numbers. 
	Just return false if x end with zeros. It must not be a palindrom number. 


another solution:
	Traverse each digit of x to get the digit's length of x. (the digit length of x=12321 is 5).
	reverse a half digit's length of the lowest digits of x,assign it to a new number y.
	get a half digit's length of the highest digits of x, assign it to x1.

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
