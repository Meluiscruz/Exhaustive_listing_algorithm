#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main( int argc, const char *argv[] )

{

int target;
int answer = 0;

	target = atoi( argv[1] );

while( pow(answer, 2) < target){

	//printf("%d \n\n", answer);
	answer++;

	}

if( pow(answer, 2) == target ){

	printf("The square root of %d is %d \n", target, answer);

	}
else{

	printf("Sorry, the number %d does not have a perfect square root. \n", target);

}

return 0;

}
