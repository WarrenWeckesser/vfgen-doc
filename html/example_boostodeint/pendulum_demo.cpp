#include <iostream>
#include <vector>
#include <cmath>
#include <boost/numeric/odeint.hpp>

#include "pendulum_vf.h"

using namespace std;
using namespace boost::numeric::odeint;

void writer(const state_type &y, const double t)
{
    cout << t;
    for (auto v : y) {
        cout << " " << v;
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    const double Pi = M_PI;
    state_type y_(2);
    double t0 = 0.0;
    double tfinal = 10.0;
    double dt = 0.01;

    y_[0] = -0.01+Pi;
    y_[1] = 0.0;

    auto pendulum = pendulum_vf(9.81, 0.0, 1.0, 1.0);
    integrate_const(make_dense_output<rosenbrock4<double>>(1e-9, 1e-9), 
        make_pair(pendulum,
            [&pendulum](const state_type &x_, matrix_type &J_, const double &t_, state_type &dfdt_)
            {pendulum.jac(x_, J_, t_, dfdt_);}
        ), y_, t0, tfinal, dt, writer);
}
