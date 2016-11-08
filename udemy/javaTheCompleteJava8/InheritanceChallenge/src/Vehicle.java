/**
 * Created by nfang on 7/8/2016.
 */
public class Vehicle {

   private String name;
   private String size;
   private int currentVelocity;
   private int currentDirection;

   public Vehicle() {
   }

   public Vehicle(String name, int size) {
      this.name = name;
      this.size = size;
      this.currentVelocity = 0;
      this.currentVelocity = 0;
   }

   public void steer(int direction) {
      this.currentDirection += direction;
      System.out.println("Vehicle.steer(): Steering at " + currentDirection + " degrees.");
   }

   public void move(int velocity, int direction) {
      currentVelocity = velocity;
      currentDirection = direction;
   }


}
