package ljs;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

public class LuckOfToday {
    /*
     * 총 1문제.
     */
	public LuckOfToday() {
		// DO NOTHING
	}
	
	public void run() {
        Date today = new Date();
        SimpleDateFormat dateForm = new SimpleDateFormat("yyyy년 MM월 dd일");
        Random random = new Random();
        int randInt = 0;    // 1. 1~100 까지 랜덤 숫자 할당 

        String str = String.format("%s의 금전운(100)은 %d%%", dateForm.format(today), randInt);
        System.out.println(str);
	}
}
