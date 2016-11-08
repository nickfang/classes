/**
 * Created by nfang on 7/6/2016.
 */
public class Main {
   public static void main(String[] args) {
//      BankAccount nick = new BankAccount();
//      nick.setNumber(100);
//      nick.setBalance(5000);
//      nick.setCustomerName("Nicholas Fang");
//      nick.setEmail("gnafkcin@gmail.com");
//      nick.setPhoneNumber("512.588.3264");
      BankAccount nick = new BankAccount(100, 5000, "Nicholas Fang", "gnafkcin@gmail.com", "512.588.3264");
      System.out.println("Account #: " + nick.getNumber());
      System.out.println("Name: " + nick.getCustomerName());
      System.out.println("Email: " + nick.getEmail());
      System.out.println("Phone: " + nick.getPhoneNumber());
      System.out.println("Balance: $" + nick.getBalance());
      nick.deposit(555);
      nick.widthdraw(1111);
      nick.widthdraw(5000);
   }
}
