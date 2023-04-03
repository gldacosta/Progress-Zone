#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


void getBin(int num, char *str)
{
  *(str+6) = '\0';
  int mask = 0x20 << 1;
  while(mask >>= 1)
    *str++ = !!(mask & num) + '0';
}

/////////////////////////////////////////////////////////////////////////////////
int main()
/////////////////////////////////////////////////////////////////////////////////
{
  char k, l, m, n, o, p, q, r, output[5];
  int i;

  char str[7];

  for(i=0; i<32; i++)  {
      getBin(i, str);

      k = (str[0]=='0') ? 'A' : 'B' ;     // str[0] primeiro shuffle
      l = (str[0]=='0') ? 'B' : 'A' ; 

      m = (str[1]=='0') ? 'C' : 'D' ;      
      n = (str[1]=='0') ? 'D' : 'C' ;

      o = (str[2]=='0') ? k : m ;      
      p = (str[2]=='0') ? m : k ;

      q = (str[3]=='0') ? l : n ;      
      r = (str[3]=='0') ? n : l ;


      output[0] =  (str[4]=='0') ? o : q ;      
      output[1]  = (str[4]=='0') ? q : o ;

      output[2]  = (str[5]=='0') ? p : r ;      
      output[3]  = (str[5]=='0') ? r : p ;

      output[4] =  '\0'; 

      printf("%s  ctr:%c%c%c%c%c%c  \n", output, str[0], str[1], str[2], str[3], str[4], str[5]);

  }
  return 0  
}