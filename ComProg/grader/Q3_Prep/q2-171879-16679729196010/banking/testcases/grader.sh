# for 1 to 5

for i in {1..5};
do
    echo "Test $i"
    python sol.py < $i.in > sol.sol
    diff -wall sol.sol $i.sol || break 
done