#include <stdio.h> 
#include <math.h> 
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// basically sigma.c without the plot
int main()
{
  int i,npts=99999;
  float top, norm, ytop;
  char  yes,ans[20],ot[2];
  double a[npts], prob, x[npts],y[npts],alpha, S;
  FILE *f1,*f2;
  
  printf("\nEnter the probability (e.g. 0.04): "); scanf("%lf", &alpha);
  printf("\nOne [o] or two-sided [any other]: "); scanf("%s", ot);
  
  if (strcmp(ot, "o") == 0){
    prob = alpha;
      }
  else{
    prob = alpha/2.0;
  }
  norm = pow((2*3.141592654),0.5); // normalisation
  
  if (prob > 1e-6) top = 5;
  else top =20;

  a[0] = x[0] = y[0] = 0;
  for (i=1; i<=npts; ++i){  // integrate up and stop when prob reached 
    
    x[i] = top - (top/npts)*i;
    y[i]=(1/norm)*exp(-0.5*x[i]*x[i]);
    a[i] = (x[i-1]-x[i])*y[i]; 
    a[i]=a[i]+a[i-1]; 
    
    if (a[i] > prob && a[i-1] < prob) S = x[i];
  }
 
  printf("For probabiliy = %1.3e (confidence level %1.3f), \n  z[%1.3e] and Z-value = %1.3f sigma\n", alpha, 1-alpha, prob, S);
  f1 = fopen("sigma.out","w"); 
  fprintf(f1,"%1.3f", S); fclose(f1);
}

// gcc -o Z-value Z-value.c; ./Z-value 
