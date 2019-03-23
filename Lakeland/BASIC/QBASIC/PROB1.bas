' Nikola Kuhar
' PROB1

DIM quantity AS INTEGER
DIM price AS SINGLE
DIM total AS SINGLE
LET quantity = 0
LET price = 0
LET total = 0

CLS
PRINT "Nikola Kuhar"
PRINT
PRINT TAB(5); "ORDER CALCULATOR"
PRINT
INPUT "Enter the quantity: ", quantity
INPUT "Enter the item price: ", price
LET total = quantity * price
PRINT
PRINT "Quantity   Total Price"
PRINT quantity;
PRINT TAB(10); total
PRINT
PRINT "Happy Shopping"

