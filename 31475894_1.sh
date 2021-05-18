#!/bin/bash

for l1 in {A..Z}
do
	for l2 in {A..Z}
	do
		x="$l1$l2"
		echo "Accessing https://en.wikipedia.org/wiki/$x.html..."
		wget https://en.wikipedia.org/wiki/"$x" -O "Bash$x".html
		lynx -dump –nolist "Bash$x".html >> BashTextFile.txt
        done
done
echo "Created text file"
grep -Eo '\w+' BashTextFile.txt >> BashUniq.txt
echo "Created text file with all words  in separate lines"
echo "(Frequency/Word) 15 most frequent words:"
tr ' ' '\n' <BashUniq.txt |sort |uniq -c|sort -nr |head -15
