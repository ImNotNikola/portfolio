public abstract class Book
{
   private String title = new String();
   protected double price;  
   public Book(String t)
   {
      title = t;
   }
   public String getTitle()
   {
      return title;
   }
   public double getPrice()
   {
      return price;
   } 
   public abstract void setPrice();
}