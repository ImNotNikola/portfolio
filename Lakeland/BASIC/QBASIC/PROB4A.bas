'Nikola Kuhar
'PROB4A

CLS
DIM dwloop AS STRING
dwloop = "yes"
DIM counter AS INTEGER
counter = 1
GOSUB var
DO WHILE dwloop = "yes"
    CLS
    GOSUB getuserinput
    GOSUB printcalc
    countervar = countervar + 1
    PRINT "Please check your email for the confirmation number."
    PRINT
    INPUT "Would you like to shop again?: ", dwloop
LOOP
END

var:
DIM quantity AS INTEGER
DIM price AS SINGLE
DIM total AS SINGLE
DIM gtotal AS SINGLE
DIM tquantity AS SINGLE
RETURN

getuserinput:
PRINT "Nikola Kuhar"
PRINT
PRINT TAB(5); "ORDER CALCULATOR"
PRINT
INPUT "Enter the quantity: ", quantity
INPUT "Enter the item price: $", price
total = quantity * price
gtotal = total + gtotal
tquantity = quantity + tquantity
RETURN

printcalc:
PRINT
PRINT "Orders placed";
PRINT TAB(11); "Total Quantity";
PRINT TAB(25); "Grand Total";
PRINT USING "###"; countervar;
PRINT TAB(12); USING "###"; tquantity
PRINT TAB(27); USING "$$##.##"; gtotal;
PRINT
RETURN

