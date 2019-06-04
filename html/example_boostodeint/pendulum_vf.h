//
//  pendulum_vf.h
//
//  Header file for the vector field pendulum
//
//  This file was generated by the program VFGEN, version: 2.6.0.dev0
//  Generated on  4-Jun-2019 at 01:56
//

#ifndef pendulum_VF_H
#define pendulum_VF_H

#include <boost/numeric/odeint.hpp>

typedef boost::numeric::ublas::vector<double> state_type;
typedef boost::numeric::ublas::matrix<double> matrix_type;

//
//  The vector field.
//

class pendulum_vf
{
    double g, b, L, m;

public:
    pendulum_vf(double g_, double b_, double L_, double m_) : g(g_), b(b_), L(L_), m(m_) {}

    void pendulum_rhs(const state_type &x_, state_type &dxdt_, const double t_);
    void pendulum_jac(const state_type &x_, matrix_type &J_, const double &t_, state_type &dfdt_);
};

#endif
