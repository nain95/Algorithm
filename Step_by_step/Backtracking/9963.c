#include <stdio.h>
int check1[40] = { 0, };
int check2[40] = { 0, };
int check3[40] = { 0, };
int solve_result = 0;
int N;

int solve(int cur){
	int i;
    if (cur == N){
        solve_result +=1;
        return 0;
    }
    for(i = 0 ; i < N ; i++){
    	if (check1[i]==1 || check2[i+cur]==1 || check3[cur-i+N-1]==1){
    		continue;
    	}
		check1[i] = 1;
        check2[cur+i] = 1;
        check3[cur-i+N-1] =1;
        solve(cur+1);
        check1[i] = 0;
        check2[cur + i] = 0;
        check3[cur - i + N - 1] = 0;
    }
    return solve_result;
}


int main(void) {
	int result;
	scanf("%d",&N);
	solve(0);
	printf("%d",solve_result);
	return 0;
}