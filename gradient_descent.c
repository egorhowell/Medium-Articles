#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double dydx(double x);

/* This program caculates the minimum of a given function 
   using gradient descent */

int main()
{
	int epochs, i;
	double learning_rate, x, x_new;

	printf("Enter your intial guess integer: ");
    scanf("%lf", &x); 

    printf("Enter how many epochs: ");
    scanf("%d", &epochs); 

    printf("Enter your learning rate: ");
    scanf("%lf", &learning_rate); 


	for (i=1;i<epochs+1;++i)
	{	
		x_new = x;
		x_new = x_new - learning_rate*dydx(x_new);
		printf("%lf\n", x_new);

		if ((x - x_new) < 0.000001){
			printf("number of epochs to coverge %d\n", i);
			break;
		}

		x = x_new;
	}

	printf("The value of x that minimises is %lf", x);

}

double dydx(double x){
	return 2*x - 5;
}