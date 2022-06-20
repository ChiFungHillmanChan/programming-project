import java.util.Scanner;

public class CircleDemo {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        double radius = input.nextDouble(); 

        Circle circle1 = new Circle(radius);
        Circle circle2 = new Circle();

        System.out.printf("radius = %f\n", circle1.getRadius()); 
        System.out.printf("perimeter = %f\n", circle1.perimeter());
        System.out.printf("area = %f\n", circle1.area()); 

        System.out.printf("radius = %f\n", circle2.getRadius()); 
        System.out.printf("perimeter = %f\n", circle2.perimeter());
        System.out.printf("area = %f\n", circle2.area()); 
        
        System.out.print(circle1.equals(circle2)); 
    }
}
