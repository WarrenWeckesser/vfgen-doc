# Build site.zip
#
# Before running this script:
#   Remove all the old files by running
#       purge_files.sh
#   Generate the example files by running
#       make_examples.sh
#   Generate the HTML by running the python script
#       menumaker.py

rm -f site.zip

zip site.zip index.html menu*.html *.css

echo "Making example files:"

for name in `/bin/ls -1 -d example_*`; do
    zip -r site.zip ${name} -x ".*" Makefile
done

zip -r site.zip MathJax -x ".*"
zip -r site.zip images -x ".*"

echo "Created site.zip"
