import java.util.Scanner;

public class Spheroid {
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter equatorial radius in km: "); 
        double a = input.nextDouble(); 

        if (a <= 0) 
        {
            System.out.print("Error: equatorial radius must be larger than 0\n"); 
            System.exit(1); 
        }
        System.out.print("Enter polar radius in km: "); 
        double c = input.nextDouble();

        if (c <= 0) {
            System.out.print("Error: polar radius must be larger than 0\n"); 
            System.exit(1); 
        }
        if (c > a) {
            System.out.print("Error: equatorial radius must be larger than polar radius\n");
            System.exit(1); 
        }
        double Eccentricity = Math.sqrt(1 - (c * c)/(a * a)); 
        double Volume= (4 * Math.PI * a * a * c / 3);

        System.out.printf("Eccentricity = %.3f\n" , Eccentricity);
        System.out.printf("Volume = %g cubic km\n" , Volume); 
    }
}
