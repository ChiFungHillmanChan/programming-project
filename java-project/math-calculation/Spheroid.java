import java.util.Scanner;

public class Spheroid {
    public static void main(String[] args) 
    {
        Scanner input= new Scanner(System.in);
        System.out.print("Enter equatorial radius in km: "); 
        double a = input.nextDouble(); 

        System.out.print("Enter polar radius in km: "); 
        double c = input.nextDouble(); 

        double Eccentricity = Math.sqrt(1 - (c * c)/(a * a)); 
        double Volume= (4 * Math.PI * a * a * c / 3);

        System.out.printf("Eccentricity = %1.3f\n" , Eccentricity);
        System.out.printf("Volume = %g cubic km\n" , Volume); 
    }
}
