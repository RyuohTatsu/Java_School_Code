
class Time {
	// Data fields
	private int hour;
	private int minute;
	private int second;

	// Creates a Time object for the current time
	Time() {
		this(0);	
	}

	// Constructs a Time object with a specified elapsed 
	// time since midnight, January 1, 1970, in milliseconds.
	Time(int elapseTime) {
		setTime(elapseTime);
	}

	// Constructs a Time object with hour, minute, and second
	Time(int hour, int minute, int second) {
		this.hour = hour;
		this.minute = minute;
		this.second = second;
	}

	// Return hour
	public int getHour() {
		return hour;
	}

	// Return minute
	public int getMinute() {
		return minute;
	}

	// Return second
	public int getSecond() {
		return second;
	}

	// Sets a new time for the object using the elapsed time
	public void setTime(int elapseTime) {
		int totalMilliseconds = (int) System.currentTimeMillis();
		int totalSeconds = totalMilliseconds / 1000;
		second = totalSeconds % 60;
		int totalMinutes = totalSeconds / 60;
		minute = totalMinutes % 60;
		int totalHours = totalMinutes / 60;
		hour = totalHours % 24;

		if (elapseTime > 0) {
			totalSeconds = elapseTime / 1000;
			second += totalSeconds % 60;
			second = totalSeconds % 60;
			totalMinutes = totalSeconds / 60;
			minute += totalMinutes % 60;
			minute = totalMinutes % 60;
			totalHours = totalMinutes / 60;
			hour += totalHours % 24;
			hour = totalHours % 24;
		}
	}
}