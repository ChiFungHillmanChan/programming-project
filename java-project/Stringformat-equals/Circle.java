public class Circle {

    private double radius;

    public Circle(){
        radius = 1.0;
    }
    public Circle(double r) {
        if(r <= 0)
        {
            throw new IllegalArgumentException("Invalid radius");
        }
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

    @Override
    public String toString() {
        return String.format("Circle(radius=%.4f)", radius);
    }

    @Override
    public boolean equals(Object object) {
        Circle circle = (Circle) object;
        if(circle.radius > radius){
            return circle.radius - radius < 0.00005;
        }
        else if(circle.radius <= radius){
            return  radius - circle.radius< 0.00005;
        }
        else{
            return false;
        }
    }
}