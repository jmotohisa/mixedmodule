%module hello
%{
/* #define SWIG_FILE_WITH_INIT */
#include <complex.h>
  /* #include "hello_c.h" */
  
extern int hello_c(char *);
extern double complex hello_f_(double complex *);
extern double complex hello_f_wrap(char *, double complex);
%}

extern int hello_c(char *);
extern double complex hello_f_(double complex *);
extern double complex hello_f_wrap(char *, double complex );
