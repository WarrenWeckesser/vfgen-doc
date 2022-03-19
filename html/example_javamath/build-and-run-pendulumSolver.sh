# Simple bash shell script for systems where Apache Commons Math is
# in /usr/share/java.  Adjust as needed, or use a more sophisticated
# Java build tool or IDE.
export CLASSPATH=.:/usr/share/java/commons-math3.jar
javac -d . pendulumODE.java
javac pendulumSolver.java
java pendulumSolver
