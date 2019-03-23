/*
Lab# 4
Filename: Java1_Lab4_Kuhar.java
Author: Nikola Kuhar
Date: 10/15/2013
Description: Prompt to explain birds sighted and on what day.
*/
import javax.swing.*;
public class TestBirdSighting 
{
	public static void main(String[] args) 
	{
		BirdSighting sighting = new BirdSighting();
		JOptionPane.showMessageDialog(null, sighting.getNumber() + " " + sighting.getSpecies() +
				" sighted on day " + sighting.getDay() + " of the year.");
		BirdSighting sighting2 = new BirdSighting("cardinal", 3, 75);
		JOptionPane.showMessageDialog(null,sighting2.getNumber() + " " + sighting2.getSpecies() +
				" sighted on day " + sighting2.getDay() + " of the year.");;
	}

}
