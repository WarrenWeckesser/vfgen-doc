/*
 *  pend_taylor7_demo.c
 *
 *  This program demonstrates the use of the function created by the
 *  "taylor" mode of VFGEN.
 *
 *
 *  Copyright (c) 2006-2014 Warren Weckesser, https://warrenweckesser.github.io
 */

#include <stdio.h>
#include "pendulum_taylor15.h"


void print_header()
{
    printf("t, theta3, v3, theta7, v7, theta15, v15\n");
}

void print_solution(double t, double x3[], double x7[], double x15[])
{
    printf("%8.5f, %15.10f, %15.10f, %15.10f, %15.10f, %15.10f, %15.10f\n",
           t, x3[0], x3[1], x7[0], x7[1], x15[0], x15[1]);
}

int main(int argc, char *argv[])
{
    double p[4];
    double xn3[2], xn7[2], xn15[2];
    double x0[2], x15derivs[15][2];
    double t, tmin, tmax;
    int numsamples;
    int i;

    /*
     *  Set the pendulum parameters.
     */
    p[0] = 9.81;   /*  g  */
    p[1] = 0.25;   /*  b  */
    p[2] = 1.0;    /*  L  */
    p[3] = 1.0;    /*  m  */

    /*
     *  Initial point where we will do the Taylor expansion.
     */
    
    x0[0] = 1.0;  /* theta(0) */
    x0[1] = 1.5;  /* v(0)     */

    pendulum_derivs15(x15derivs, x0, p);

    tmin =  0.0;
    tmax =  1.0;
    numsamples = 101;

    print_header();
    for (i = 0; i < numsamples; ++i) {
        t = tmin + i*(tmax - tmin)/(numsamples - 1);
        pendulum_evaltaylor15n(xn3, 3, t, x0, x15derivs);
        pendulum_evaltaylor15n(xn7, 7, t, x0, x15derivs);
        pendulum_evaltaylor15n(xn15, 15, t, x0, x15derivs);
        print_solution(t, xn3, xn7, xn15);
    }
}
