import numpy as np


def print_trace(out, name, x, y, plot_style="line", color="black"):
    x = np.array(x).tolist()
    y = np.array(y).tolist()
    print(f"const {name} = {{", file=out)
    print(f"  x: {x!r},", file=out)
    print(f"  y: {y!r},", file=out)
    if plot_style == "scatter":
        print("  mode: 'markers',", file=out)
        print("  type: 'scatter',", file=out)
    else:
        print("  line: {", file=out)
        print(f"    dash: 'solid'", file=out)
        print("  },", file=out)
    print("  marker: {", file=out)
    print(f"    color: '{color}',", file=out)
    print("  },", file=out)
    print(f"  name: '{name}'", file=out)
    print("}", file=out)


def example2_solution(t):
    # This function assumes 0 <= t <= 10.
    t1mask = t <= np.e - 1
    t2mask = ((np.e - 1) < t) & (t <= (np.exp(2) - 1))
    t3mask = t > np.exp(2) - 1
    tp1 = t + 1
    y = np.empty_like(t)
    y[t1mask] = tp1[t1mask]
    y[t2mask] = np.exp(tp1[t2mask]/np.e)
    y[t3mask] = np.power(np.e/(3 - np.log(tp1[t3mask])), np.e)
    return y


def example3_solution(t):
    # This function assumes 0 <= t <= 2.
    t1mask = t <= 1
    t2mask = t > 1
    tp1 = t + 1
    y = np.empty_like(t)
    t1 = tp1[t1mask]
    t2 = tp1[t2mask]
    y[t1mask] = np.sqrt(t1)
    y[t2mask] = t2/4 + 0.5 + (1 - np.sqrt(2)/2)*np.sqrt(t2)
    return y


t, y = np.loadtxt('sdd.csv', unpack=True, skiprows=1, delimiter=',')
t_exact = np.linspace(1, 10, 289)
y_exact = example2_solution(t_exact)

with open('plotly_example2_data.js', 'w') as f:
    print_trace(f, "computed", t, y, plot_style="scatter", color="rgba(0, 0, 0, 0.75)")
    print_trace(f, "exact", t_exact, y_exact, color="rgba(64, 192, 64, 0.75)")
    print(f"const data = [computed, exact]", file=f)
    print("export {data}", file=f)

t, y = np.loadtxt('sddfn.csv', unpack=True, skiprows=1, delimiter=',')
t_exact = np.linspace(0, 2, 201)
y_exact = example3_solution(t_exact)

with open('plotly_example3_data.js', 'w') as f:
    print_trace(f, "computed", t, y, plot_style="scatter", color="rgba(0, 0, 0, 0.75)")
    print_trace(f, "exact", t_exact, y_exact, color="rgba(64, 192, 64, 0.75)")
    print(f"const data = [computed, exact]", file=f)
    print("export {data}", file=f)
