import javax.swing.JOptionPane;
public class TestSandwich 
{
		public static void main(String[] args) 
	{
		Sandwich YUM;
		YUM = new Sandwich();
		YUM.setBread("White");
		YUM.setMeat("Chicken");
		YUM.setPrice(4.99);	
		JOptionPane.showMessageDialog(null, "So you would like " + YUM.getBread() + 
					" bread with " + YUM.getMeat() + " for $" + YUM.getPrice() + "?");		
	}
}