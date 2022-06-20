public class Circle {

    private double radius;

    public Circle(double r) {
        radius = r; 
    }
    public double getRadius(){
        return radius; 
    }

    public double area(){
        return Math.PI * radius * radius; 
    }
    public double perimeter(){
        return 2 * Math.PI * radius; 
    }
}
