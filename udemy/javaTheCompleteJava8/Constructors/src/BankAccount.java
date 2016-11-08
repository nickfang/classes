/**
 * Created by nfang on 7/6/2016.
 */
public class BankAccount {
   private int number;
   private int balance;
   private String customerName;
   private String email;
   private String phoneNumber;

   public BankAccount() {
      System.out.println("Empty Constructor Called!");
   }

   public BankAccount (int number, int balance, String customerName, String email, String phoneNumber) {
      this.number = number;
      this.balance = balance;
      this.customerName = customerName;
      this.email = email;
      this.phoneNumber = phoneNumber;
   }

   public void setNumber(int number){
      this.number = number;
   }

   public int getNumber() {
      return this.number;
   }

   public void setBalance(int balance) {
      this.balance = balance;
   }

   public int getBalance() {
      return this.balance;
   }

   public void setCustomerName(String customerName) {
      this.customerName = customerName;
   }

   public String getCustomerName() {
      return this.customerName;
   }

   public void setEmail(String email) {
      this.email = email;
   }

   public String getEmail() {
      return this.email;
   }

   public void setPhoneNumber(String phoneNumber) {
      this.phoneNumber = phoneNumber;
   }

   public String getPhoneNumber() {
      return this.phoneNumber;
   }

   public void deposit(int amount) {
      this.balance += amount;
      System.out.println("$" + amount + " deposited.  Account balance is now $" + this.balance);
   }

   public void widthdraw(int amount) {
      if (this.balance >= amount){
         this.balance -= amount;
         System.out.println("$" + amount + " widthdrawn.  The remaining balance is $" + this.balance);
      } else {
         System.out.println("Insufficient funds!  Attempted to widthdraw $" + amount + " when your balance is $" + this.balance);
      }
   }
}
