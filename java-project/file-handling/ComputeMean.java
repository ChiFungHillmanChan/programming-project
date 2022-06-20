// Program for Exercise 8

import java.io.IOException;

public class ComputeMean {
  public static void main(String[] args) {
    if (args.length != 1) {
      System.err.println("Usage: java ComputeMean <filename>");
      System.exit(1);
    }

    try {
      Dataset numbers = new Dataset(args[0]);
      System.out.printf("Dataset size = %d\n", numbers.size());
      System.out.printf("Mean value = %.3f\n", numbers.meanValue());
    }
    catch (IOException error) {
      System.err.printf("Error: cannot access '%s'\n", args[0]);
      System.exit(2);
    }
    catch (Exception error) {
      System.err.println(error);
      System.exit(2);
    }
  }
}