/*
Lab# 10
Filename: Java1_Lab10_Kuhar.java
Author: Nikola Kuhar
Date: 11/18/2013
Description: Lab to demo inheritance.
*/
public class CabinRental 
{
	private int cabinNumber;
	protected double rate;
	final int cutoff = 4;
	final double lowrate = 950;
	final double highrate = 1100;
	public CabinRental(int num) 
	{
		cabinNumber = num;
		if (cabinNumber < cutoff)
		{
			rate = lowrate;
		}
		else
		{
			rate = highrate;
		}
	}
	public int getCabinNumber() 
	{
		return cabinNumber;
	}
	public double getRate() 
	{
		return rate;
	}
}