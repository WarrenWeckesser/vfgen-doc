echo "Purging index.html"
rm -f index.html

echo "Purging menu_*.html"
rm -f menu_*.html

echo "Purging example directories:"

for name in `/bin/ls -1 -d example_*`; do
    if test ${name} != "example_vf"; then
        echo " " ${name}
        cd ${name}
        make -s purge
        cd ..
    fi
done

echo "Done"
