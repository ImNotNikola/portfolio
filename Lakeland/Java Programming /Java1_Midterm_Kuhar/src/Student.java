public class Student
{
	// Variable declaration
	private final String lastName;
	private final int id;

	// Constructor
	public Student(int tempid, String tempName)
	{
		this.id = tempid;
		this.lastName = tempName;

	}

	public <String> String setLastName()
	{
		String newLastName = lastName.substring(0, 9);
		return (newLastName);
	}

	public int setId()
	{
		int intid = Integer.parseInt(id);
		return intid;
	}
}
