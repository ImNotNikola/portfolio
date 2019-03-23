/*
Lab# Midterm
Filename: java1_Midterm_Kuhar.java
Author: Nikola Kuhar
Date: 10/18/2013
Description: Program which inputs a students last name and ID in one window
				truncates the name, pulls the number from the name, verifies 
				that the user selected OK or Cancel and spits out the info.
 */
public class TestStudent
{
	public static void main(String[] args)
	{
		String input = "";
		String name = "";
		String id = "";
		int done = 0;
		int x = 0;
		input = JOptionPane
				.showInputDialog("Please input the students last name and ID: ");
		while (x < input.length())
		{
			if (input.charAt(x) == ' ')
			{
				name = input.substring(0, x);
				id = input.substring(x + 1, input.length());
				done = 1;
				x = input.length();
			}
			++x;
			if (input != null || input != "")
				// Error detection for ID number <1 & >1000
				if (intid < 1 || intid > 1000)
				{
					JOptionPane.showMessageDialog(null,
							"I'm sorry your ID number is not correct.");
				}

			// main program code
			if (done == 1)
			{
				Student newStudent = new Student(id, name);
				JOptionPane.showMessageDialog(null,
						"The students last name is %s & the ID is %i",
						newStudent.setLastName(), newStudent.setId());
			}

		}
	}

}
