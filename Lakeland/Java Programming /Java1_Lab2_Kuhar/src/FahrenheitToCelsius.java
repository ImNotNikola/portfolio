	/*
	 * Lab2
	 * Java1_Lab2_Kuhar.java
	 * Nikola Kuhar
	 * 08/28/2013
	 * Program which converts an inputed Fahrenheit temperature and converts it to Celsius.
	 */
import javax.swing.JOptionPane;
public class FahrenheitToCelsius {
		public static void main(String[] args) {
			int result = 0;
			int input = 0;
			String inputstring = JOptionPane.showInputDialog(null,
					"What is the temperature to be converted in Fahrenheit?", "Fahrenheit Input", 
					JOptionPane.QUESTION_MESSAGE);
			input = Integer.parseInt(inputstring);
			result = (input-32)*5/9;
			JOptionPane.showMessageDialog(null, input + " degrees F is " + result + " degrees C.");		
		}
	}

