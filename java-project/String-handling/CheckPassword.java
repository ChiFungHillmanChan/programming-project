public class CheckPassword 
{
    public static boolean longEnough(String password) 
    {
        return (password.length() >= 12); 
    }

    public static boolean atLeastTwoDigits(String password) 
    {
        int intcount = 0;
        int charcount = 0; 

        for(int i = 0; i < password.length(); i++) 
        {
            Boolean digit = Character.isDigit(password.charAt(i));
            if (digit)  
            {
                charcount++;
            } 
            else 
            {
                intcount++;
            }
        }
        return (charcount > 1 && intcount > 1); 
    }
    public static void main(String[] args) 
    {
        if(args.length > 0)
        {
            String password = args[0];
            if (longEnough(password) == true)
            {
                if (atLeastTwoDigits(password) == true)
                {
                    System.out.printf("Password is valid\n");
                    System.exit(1); 
                }
            }
            if (longEnough(password) == false)
            {
                System.out.printf("Password is not valid\n");
                System.exit(2); 
            }
            if (atLeastTwoDigits(password) == false)
            {
                System.out.printf("Password is not valid\n");
                System.exit(2);   
            }
        }
        else
        {
            System.err.printf("Usage: java CheckPassword <password>\n");
            System.exit(1); 
        }
    }
}