 '5 Nikola Kuhar
' PROB1

CLS
GOSUB var
GOSUB getuserinput
GOSUB printcalc
END

var:
DIM quantity AS INTEGER
DIM price AS SINGLE
DIM total AS SINGLE
DIM gtotal AS SINGLE
DIM shipping AS SINGLE
quantity = 0
price = 0
total = 0
gtotal = 0
shipping = 3.00
RETURN

getuserinput:
PRINT "Nikola Kuhar"
PRINT
PRINT TAB(5); "ORDER CALCULATOR"
PRINT
INPUT "Enter the quantity: ", quantity
INPUT "Enter the item price: $", price
total = quantity * price
gtotal = total + shipping
RETURN

printcalc:
PRINT
PRINT "Quantity";
PRINT TAB(11); "Total Price";
PRINT TAB(25); "Grand Total"
PRINT USING "##"; quantity;
PRINT TAB(12); USING "$$##.##"; total;
PRINT TAB(27); USING "$$##.##"; gtotal
PRINT
PRINT "Happy Shopping"
RETURN

