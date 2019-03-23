/*
Lab# 5
Filename: Java1_Lab5_Kuhar.java
Author: Nikola Kuhar
Date: 10/15/2013
Description: Pop-up menu for Condo Sales info
*/
import javax.swing.JOptionPane;
public class CondoSales 
{
	public static void main(String[] args) 
	{
		int selection;
		int price;
		String result;
		String input;		     
		final int 		PARK = 1; 
		final int 		GOLF = 2;
		final int 		LAKE = 3;
		final int 		PARK_PR = 150000;
		final int 		GOLF_PR = 170000;
		final int 		LAKE_PR = 210000;
		final String 	PARK_STR = "Park view";
		final String 	GOLF_STR = "Golf course view";
		final String 	LAKE_STR = "Lake view";
		final String 	INVALID_STR = "\nInvalid selection";
		final String 	GARAGE_STR = "Garage";
		final String 	PARKING_STR = "Parking space";
		final int 		GAR = 1;
		final int	 	PS = 2;
		final int 		GARAGE_PR = 5000;
		input = JOptionPane.showInputDialog(null,
				"\t\n\nMenu\n" + "(" + PARK + ") " + PARK_STR + "\n" + "(" + GOLF + ") " + GOLF_STR + "\n" +
				"(" + LAKE + ") " + LAKE_STR + "\n" + "Enter Selection (1, 2, or 3) ");
		selection = Integer.parseInt(input);
		switch(selection)
		{
			case PARK:
				result = PARK_STR;
		    	  price = PARK_PR;
		    	  break;
			case GOLF:
				result = GOLF_STR;
		    	  price = GOLF_PR;
		    	  break;
			case LAKE:
				result = LAKE_STR;
				price = LAKE_PR;
				break;
			default:
				result = INVALID_STR;
		        price = 0;
		}
		JOptionPane.showMessageDialog(null, "You selected " + result + "  $" + price);
		if(price != 0)
		{
			input = JOptionPane.showInputDialog(null, 
					"\t\n\nMenu\n" + 
					"(" + GAR + ") " + GARAGE_STR + "\n" +
					"(" + PS + ") " +  PARKING_STR + "\n" +
					"Enter Selection (1 or 2) ");
			selection = Integer.parseInt(input);
			if(selection == GAR)
			{
				price = price + GARAGE_PR;
			}
			else if(selection != PS)
			{
				JOptionPane.showMessageDialog(null, "Selection is invalid - assuming no garage.");
			}
			JOptionPane.showMessageDialog(null, "New price is " + price);					
      }
	}

}
