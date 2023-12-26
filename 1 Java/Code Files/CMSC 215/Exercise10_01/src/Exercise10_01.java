
public class Exercise10_01 {

	public static void main(String[] args) {
		// Create Time objects
		Time time1 = new Time();
		Time time2 = new Time(555550000);
		Time time3 = new Time(5, 23, 55);

		// Display Time objects 
		System.out.println(time1.getHour() + ":" + time1.getMinute() + 
			":" + time1. getSecond());
		System.out.println(time2.getHour() + ":" + time2.getMinute() + 
			":" + time2. getSecond());
		System.out.println(time3.getHour() + ":" + time3.getMinute() + 
				":" + time3. getSecond());
	}
}

