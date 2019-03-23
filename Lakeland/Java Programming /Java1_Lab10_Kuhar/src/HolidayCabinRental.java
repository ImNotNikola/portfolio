public class HolidayCabinRental extends CabinRental 
{
	public HolidayCabinRental(int num) 
	{
		super(num);
		final int surcharge = 150;
		rate = rate + surcharge;
	}
}
