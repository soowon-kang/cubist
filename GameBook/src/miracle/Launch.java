package miracle;

import java.io.IOException;

import ksw.*;
//import ljs.*;

public class Launch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	    
	    /*
	     * LuckOfToday.java 문제 출력.
	     * 
		LuckOfToday ksw = new LuckOfToday();
		ksw.run();
	     */
	    
	    /*
	     * MultiplicationTable.java 문제 출력.
	     * 
		MultiplicationTable ksw = new MultiplicationTable(0);
		try {
			ksw.run();
		} catch (IOException e) {
			e.printStackTrace();
		}
	     */
	    
	    RockPaperScissors ksw = new RockPaperScissors();
	    try {
	        ksw.run();
	    } catch (IOException e) {
	        e.printStackTrace();
	    }
	}
}
