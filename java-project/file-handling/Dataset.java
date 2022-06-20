import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Dataset {

    private List<Double> data; 

    public Dataset(String filename)throws IOException{
        this.data = new ArrayList<>();

        Scanner input = new Scanner(Paths.get(filename));

        while(input.hasNextDouble()){

            Double line = input.nextDouble();
            data.add(line);
        }
        input.close(); 
    }
    public int size(){
        return data.size(); 
    }
    public double meanValue(){

        double TotalValue = 0;
        if(data.isEmpty()){
            throw new ArithmeticException();
        }
        for (int i = 0; i < data.size(); i++) {
            TotalValue = TotalValue + data.get(i);
        }
        return TotalValue/data.size();
    }
}
