/*
https://leetcode.com/problems/jump-game/



*/

bool canJump(int A[], int n) {
    
    //极端情况
    if (n == 0 || n == 1)
        return true;
    //farest: 在当前下标处，仍能到达的最远距离
    //初始化
    int farest = A[0];
    int faresttmp;
    int i;
    for(i = 1; i<n; i++ ){
        if(farest >= n)
            return true;
        
        //当前位置在最远距离的范围内时，仍能继续
        if(i <= farest){
             faresttmp = i + A[i];
             if(faresttmp > farest)
                farest = faresttmp;
             
        }
        else{
            return false;
        }
    }
}
