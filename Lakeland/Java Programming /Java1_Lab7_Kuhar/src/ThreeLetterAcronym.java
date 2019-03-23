/*
Lab#7
Filename: Java1_Lab7_Kuhar.java
Author: Nikola Kuhar
Date: 10/13/2013
Description: Takes a phrase and converts it to an acronym
*/
import javax.swing.JOptionPane;
public class ThreeLetterAcronym 
{
	public static void main(String[] args) 
	{
		{
		    String phrase = "";
		    String firstWord = "";
		    String secondWord = "";
		    String thirdWord = "";
			    phrase = JOptionPane.showInputDialog(null, "Please enter three words");
			    firstWord = firstWord.toUpperCase();
			    secondWord = secondWord.toUpperCase();
			    thirdWord = thirdWord.toUpperCase();
			    JOptionPane.showMessageDialog(null, "Original phrase was " + phrase + "\nThree lettr aronym is " + firstWord.charAt(0) + secondWord.charAt(0) + thirdWord.charAt(0));
		}
	}
}
