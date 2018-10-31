for run in {1..10}
do
	gpio mode 0 out
	gpio write 0 1 
	gpio mode 0 in
	sleep .5
	gpio mode 1 out
	gpio write 1 1
	gpio mode 1 in
	sleep .5
done
