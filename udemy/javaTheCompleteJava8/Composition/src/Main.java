/**
 * Created by nfang on 7/8/2016.
 */
public class Main {

//   Mazda3 newCar = new Mazda3();
   public static void main (String[] args) {
      Dimensions dimensions = new Dimensions(20,20,5);
      Case theCase = new Case("2288", "Dell", "240", dimensions);

      Monitor theMonitor = new Monitor("27inch Beast", "Acer", 27, new Resolution(2540, 1440));

      Motherboard theMotherboard = new Motherboard("BJ-200", "Asus", 4, 6, "v2.44");

      PC thePC = new PC(theCase, theMonitor, theMotherboard);
      thePC.powerUp();
   }
}
