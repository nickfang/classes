/**
 * Created by nfang on 7/8/2016.
 */
public class Car extends Vehicle{

   private int wheels;
   private int doors;
   private boolean isManual;
   private int currentGear;

   public Car(String name, String size, int wheels, int doors, boolean isManual) {
      super(name, size);
      this.wheels = wheels;
      this.doors = doors;
      this.isManual = isManual;
      this.currentGear = 1;
   }

   public int getWheels() {
      return wheels;
   }

   public void setWheels(int wheels) {
      this.wheels = wheels;
   }

   public int getDoors() {
      return doors;
   }

   public void setDoors(int doors) {
      this.doors = doors;
   }

   public boolean isManual() {
      return isManual;
   }

   public void setManual(boolean manual) {
      isManual = manual;
   }

   public int getCurrentGear() {
      return currentGear;
   }

   public void setCurrentGear(int currentGear) {
      this.currentGear = currentGear;
   }


}
