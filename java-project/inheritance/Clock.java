// Slightly modified version of Clock class from Lectures 5 & 6

public class Clock implements Runnable {

  // Protected access means these are accessible in subclasses
  protected static final int SECONDS_IN_A_MINUTE = 60;
  protected static final int MINUTES_IN_AN_HOUR = 60;
  protected static final int HOURS_IN_A_DAY = 24;

  private int hours;
  private int minutes;
  private int seconds;

  public Clock() {
    this(0, 0, 0);
  }

  public Clock(int h, int m) {
    this(h, m, 0);
  }

  public Clock(int h, int m, int s) {
    setHours(h);
    setMinutes(m);
    setSeconds(s);
  }

  private void setHours(int h) {
    if (h < 0 || h >= HOURS_IN_A_DAY) {
      throw new IllegalArgumentException("invalid hours");
    }
    hours = h;
  }

  private void setMinutes(int m) {
    if (m < 0 || m >= MINUTES_IN_AN_HOUR) {
      throw new IllegalArgumentException("invalid minutes");
    }
    minutes = m;
  }

  private void setSeconds(int s) {
    if (s < 0 || s >= SECONDS_IN_A_MINUTE) {
      throw new IllegalArgumentException("invalid seconds");
    }
    seconds = s;
  }

  public int getHours() { return hours; }

  public int getMinutes() {
    return minutes;
  }

  public int getSeconds() {
    return seconds;
  }

  @Override
  public String toString() {
    return String.format("%02d:%02d:%02d", hours, minutes, seconds);
  }

  public void display() {
    System.out.println(this);
  }

  public void tick() {
    ++seconds;
    if (seconds == SECONDS_IN_A_MINUTE) {
      seconds = 0;
      ++minutes;
      if (minutes == MINUTES_IN_AN_HOUR) {
        minutes = 0;
        ++hours;
        if (hours == HOURS_IN_A_DAY) {
          hours = 0;
        }
      }
    }
  }

  @Override
  public void run() {
    try {
      while (true) {
        display();
        tick();
        Thread.sleep(1000);
      }
    }
    catch (InterruptedException error) {
      System.exit(1);
    }
  }
}