import sys


styles = ['solid', 'dot', 'dashdot']

filename = sys.argv[1]
with open(filename) as f:
    content = f.read()

lines = content.splitlines()
headers = [field.strip() for field in lines[0].split(',')]

selected_headers = sys.argv[2:]
if len(selected_headers) == 0:
    selected_headers = headers[1:]

display_name_map = {}
selected_column_names = []
for name in selected_headers:
    if '=' in name:
        column_name, display_name = name.split('=')
    else:
        column_name = display_name = name
    selected_column_names.append(column_name)
    display_name_map[column_name] = display_name

data = [line.split(',') for line in lines[1:]]
columns = list(zip(*data))

for k in range(1, len(columns)):
    if headers[k] in selected_column_names:
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
        print(f"  name: '{display_name_map[headers[k]]}'")
        print("}")

print("")
if len(selected_column_names) == 0:
    names = ", ".join(headers[1:])
else:
    names = ", ".join(selected_column_names)
print(f"const data = [{names}]")
print("export {data}")
