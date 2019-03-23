import javax.swing.JOptionPane;
public class TestBirdSighting {
	public static void main(String[] args)
	{
		BirdSighting BS;
		BS = new BirdSighting();
		BS.setSpecies("Robin");
		BS.setAmount(1);
		BS.setDate(1);	
		JOptionPane.showMessageDialog(null, "So you would like " + YUM.getBread() + 
					" bread with " + YUM.getMeat() + " for $" + YUM.getPrice() + "?");
	}

}
