import java.io.IOException;
import java.io.Writer;

public class Money implements Writeable{
    private int euros, cents;

    public Money(int e, int c) {
      euros = e;
      cents = c;
    }

    public int getEuros() {
      return euros;
    }

    public int getCents() {
      return cents;
    }

    public Money plus(Money other) {
      int sumEuros = euros + other.euros;
      int sumCents = cents + other.cents;
      return new Money(sumEuros + sumCents / 100, sumCents % 100);
    }
    @Override
    public String toString(){
      return String.format("Money: €%d.%02d\n", getEuros(), getCents());
    }
    public void writeTo(Writer destination) throws IOException{
      destination.write(toString());
    }
  }
