// Comma operator usage
#include <stdio.h>
int main()
{
  int x=10;
  int j=(x++, ++x); // Comma operator evaluates the first operand discards the result and second operand evaluates and hands it to j.
  printf("%d",j); // j=12
  return 0;
 }
