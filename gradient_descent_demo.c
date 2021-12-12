#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double dydx(double x);

/* This program caculates the minimum of a function using gradient descent */

int main(){

	int i, epochs;
	double x_new, x, learning_rate;

	printf("Enter initial guess: ");
    scanf("%lf", &x); 

    printf("Enter learning rate: ");
    scanf("%lf", &learning_rate);

    printf("Enter epochs: ");
    scanf("%d", &epochs);  

	for (i=1;i<epochs+1;++i){

		x_new = x;
		x_new = x_new - learning_rate*dydx(x_new);
		if ((x-x_new) < 0.1){
			printf("number of epochs to converge %d\n", i);
			break;
		}
		x = x_new;
	}

	printf("minimum is at the x value %lf\n", x_new);


}

double dydx(double x){
	return 2*x-5;
}