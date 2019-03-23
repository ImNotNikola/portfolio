'** BSampB - Sample BASIC Programming B **
'*** "COUNTDOWN" unsing keyboard input
'** Author: Nikola Kuhar
'**Purpose: This program calculates and displays the
'**hours until the weekend based on the remaining
'**number of days in the workweek.
'**Initialization Routine*****
'**Declare variables:
DIM days AS INTEGER
DIM hours AS INTEGER
'** clear screen:
CLS
PRINT "Nikola Kuhar"
PRINT
'**Input number of days
INPUT "Enter the number of days remaining in the workweek:", days
'**print headings:
PRINT TAB(16); "COUNTDOWN"
PRINT
PRINT "Days Remaining"; TAB(20); "Hours Remaining"
PRINT
'***Calculate and PRint*****
LET hours = days * 8
PRINT days; TAB(20); hours
'***End Runtime*****
PRINT
PRINT "The weekend is in sight!"
END
