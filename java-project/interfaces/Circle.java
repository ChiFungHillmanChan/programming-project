import java.io.IOException;
import java.io.Writer;

public class Circle implements Writeable {

    private double radius;

    public Circle (double r){
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
        return String.format("Circle: r=%.4f\n", radius);
    }
    public void writeTo(Writer destination) throws IOException{
        destination.write(toString());
    }
}
