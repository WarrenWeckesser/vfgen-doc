import static java.lang.Math.*;
import org.apache.commons.math3.ode.FirstOrderDifferentialEquations;
import org.apache.commons.math3.ode.FirstOrderIntegrator;
import org.apache.commons.math3.ode.nonstiff.DormandPrince853Integrator;
import pendulumODE.pendulumODE;

public class pendulumSolver {

    static void printState(double t, double[] state) {
        String s = String.format("%14.6f", t);
        System.out.print(s);
        for (int i = 0; i < 2; ++i) {
            s = String.format(" %20.15f", state[i]);
            System.out.print(s);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        double Pi = PI;

        // Adjust these integrator control parameters as needed.
        double minstep = 1e-13;
        double maxstep = 10.0;
        double abstol = 1.0e-12;
        double reltol = 1.0e-9;

        FirstOrderIntegrator dp853 = new DormandPrince853Integrator(minstep, maxstep, abstol, reltol);
        FirstOrderDifferentialEquations ode = new pendulumODE();

        // Initial conditions
        double[] state = new double[] { Pi-1.0000000000000000e-02, 0.0000000000000000e+00};

        // Adjust the following time parameters as needed.
        double t = 0.0;    // Start time.
        double t1 = 10.0;  // End time.
        double stepsize = 0.05;

        printState(t, state);
        while (t < t1) {
            double ts = t + stepsize;
            if (Math.abs((ts - t1)/ts) < 1e-12) {
                ts = t1;
            }
            dp853.integrate(ode, t, state, ts, state);
            printState(ts, state);
            t = ts;
        }
    }
}
