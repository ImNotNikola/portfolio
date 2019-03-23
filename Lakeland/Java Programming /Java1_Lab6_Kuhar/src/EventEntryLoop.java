/*
Lab# 6
Filename: Java1_Lab6_Kuhar.java
Author: Nikola Kuhar
Date: 10/15/2013
Description: Enter a number and a message is spit out depending on what number is entered
*/
import javax.swing.JOptionPane;
public class EventEntryLoop 
{
	public static void main(String[] args) 
	{
		int number;
		String entry, message;
		final int QUIT = 999;
		entry = JOptionPane.showInputDialog(null, "Enter an even number or " + QUIT + " to quit"); 
		number =  Integer.parseInt(entry); 
		while(number != QUIT)
		{ 
			if(number % 2 == 0)
			{
				message = "Good job!";
			}
			else
			{
				message = number + " is not an even number";
			}
			JOptionPane.showMessageDialog(null,message);
			entry = JOptionPane.showInputDialog(null, "Enter an even number or " + QUIT + " to quit");     
			number =  Integer.parseInt(entry);  
		}   
	}
}
