public class CircleDemo {
    public static double r = 4.5; 
    public static void main(String[] args) {

        
        Circle circle = new Circle(r);

        System.out.printf("radius = %.1f\n", circle.getRadius(r));
        System.out.printf("perimeter = %2.3f\n", circle.perimeter(r));
        System.out.printf("area = %2.3f\n", circle.area(r));
    }
}
