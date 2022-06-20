public class MeanValue {
    public static double meanValue(double[] data) 
    {
        double sum = 0; 
        for (int i = 0; i < data.length ; i++)
        {
            sum += data[i]; 
        }
        sum = sum/data.length; 
        return sum; 
    }
  
    public static void main(String[] args) 
    {
        if(args.length > 0)
        {
            double [] input = new double [args.length];
            for(int i = 0; i < args.length; i++)
            {
                input[i] = Double.parseDouble(args[i]); 
            }
            meanValue(input);
            System.out.printf("Mean value = %.3f\n", meanValue(input)); 
        }
        else
        {
            System.err.println("Usage: java MeanValue <values...>"); 
            System.exit(1); 
        }
    }
}