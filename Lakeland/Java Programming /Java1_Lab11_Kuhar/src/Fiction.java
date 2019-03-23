public class Fiction extends Book 
{
	public Fiction(String title) 
	{
		super(title);
		setPrice();
	}
	public void setPrice() 
	{
		super.price = 24.99;
	}
	public String toString()
	{
		return "Fiction: " + getTitle() + ", " + price;
	}

}
