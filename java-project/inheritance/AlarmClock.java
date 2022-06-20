public class AlarmClock extends Clock{

    private int alarmHours;
    private int alarmMinutes;
  
    public AlarmClock() {
        super(0, 0, 0);
    }

    public AlarmClock(int h, int m) {
        super(h, m, 0);
    }

    public AlarmClock(int h, int m, int s) {
        super(h, m, s);
    }

    public int getAlarmHours() {
        return alarmHours;
    }

    public int getAlarmMinutes() {
        return alarmMinutes;
    }

    public void setAlarm(int h, int m){
        if (h < 0 || h >= HOURS_IN_A_DAY) {
            throw new IllegalArgumentException("invalid alarm hours");
        }
        alarmHours = h;
        if (m < 0  || m >= MINUTES_IN_AN_HOUR) {
            throw new IllegalArgumentException("invalid alarm minutes");
          }
        alarmMinutes = m;
    }
    public boolean isRinging(){
        return alarmMinutes == super.getMinutes() && alarmHours == super.getHours() && super.getSeconds() < 15; 
    }

    @Override
    public void display() {
        if(isRinging() == true){
            System.out.println(this + " - WAKE UP!");
        }
        else {
            System.out.println(this);
        }
    }
}
