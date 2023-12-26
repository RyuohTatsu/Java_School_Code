public class Exercise01_11 {
    public static void main(String[] args) {
        //Store current population
        int inPop = 312032486;
 
        // Store 365 days in seconds
        int SecsYear = 31536000;
 
        //Number of births per year
        int bbyYear = SecsYear / 7;
         
        //Number of deaths per year
        int deYear = SecsYear / 13;
         
        //Immigration per year
        int imYear = SecsYear / 45;
         
        //Rate of population change per year
        int incYear = bbyYear - deYear + imYear;
         
        System.out.println("Population after one year : " + (double)(inPop + (1 * incYear)));
        System.out.println("Population after two years:  " + (double)(inPop + (2 * incYear)));
        System.out.println("Population after three years:  " + (double)(inPop + (3 * incYear)));
        System.out.println("Population after four years:  " + (double)(inPop + (4 * incYear)));
        System.out.println("Population after five years:  " + (double)(inPop + (5 * incYear)));
  }
}
