import sys


styles = ['solid', 'dash', 'dot', 'dashdot']

filename = sys.argv[1]
with open(filename) as f:
    content = f.read()
lines = content.splitlines()
headers = [field.strip() for field in lines[0].split(',')]
data = [line.split(',') for line in lines[1:]]
columns = list(zip(*data))

for k in range(1, len(columns)):
    print(f"const {headers[k]} = {{")
    print("  x: ", end="")
    values = ", ".join(columns[0])
    print(f"[{values}],")
    print("  y: ", end='')
    values = ", ".join(columns[k])
    print(f"[{values}],")
    style = styles[(k - 1) % len(styles)]
    print("  line: {")
    print(f"    dash: '{style}'")
    print("  },")
    print(f"  name: '{headers[k]}'")
    print("}")

print("")
names = ", ".join(headers[1:])
print(f"const data = [{names}]")
print("export {data}")
