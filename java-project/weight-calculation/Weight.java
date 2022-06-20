import java.util.Scanner; 

class Weight
{
    public static void main(String[] args) 
    {
        Scanner thein = new Scanner(System.in); 
        System.out.print("Enter weight in kilograms: "); 

        float store = thein.nextFloat();
        double kilograms = (double) store; 

        double ounces = (kilograms / 0.45359237) * 16;
        int pounds = (int) (kilograms / 0.45359237); 
        double remaining_ounces = ounces - (pounds * 16); 

        System.out.printf("Equivalent imperial weight is %d lb %.1f oz%n",  pounds, remaining_ounces);
    } 
}
