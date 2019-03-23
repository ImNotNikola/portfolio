'Nikola Kuhar
'PROB5

CLS
GOSUB var
GOSUB getuserinput
GOSUB printcalc
END

var:
DIM quantity AS INTEGER
DIM price AS SINGLE
DIM total AS SINGLE
DIM discount AS SINGLE
discount = .1
RETURN

getuserinput:
PRINT "Nikola Kuhar"
PRINT
PRINT TAB(5); "ORDER CALCULATOR"
PRINT
INPUT "Enter the quantity: ", quantity
INPUT "Enter the item price: $", price
IF quantity > 5 THEN
total = quantity * price
total = total - (total * discount)
ELSE
total = quantity * price
END IF

RETURN

printcalc:
PRINT
PRINT "Quantity";
PRINT TAB(11); "Regular Price";
PRINT TAB(25); "Discount";
PRINT TAB(38); "Total Price"
PRINT USING "###"; quantity;
PRINT TAB(12); USING "$$##.##"; price;
PRINT TAB(27); USING "##%"; Discount;
PRINT TAB(41); USING "$$###.##"; total
PRINT
RETURN