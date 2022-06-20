// Program provided for use with Exercise 10

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Ex10 {
  public static void create(List<Writeable> things) {
    things.add(new Money(2, 7));
    things.add(new Money(11, 80));
    things.add(new Circle(6.3952));
  }

  public static void display(List<Writeable> things) throws IOException {
    PrintWriter out = new PrintWriter(System.out);
    for (Writeable thing: things) {
      thing.writeTo(out);
    }
  }

  public static void main(String[] args) {
    try {
      List<Writeable> things = new ArrayList<>();
      create(things);
      display(things);
    }
    catch (Exception error) {
      System.err.println(error);
      System.exit(1);
    }
  }
}