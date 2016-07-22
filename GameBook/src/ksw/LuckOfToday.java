package ksw;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

/**
 * Created by CubePenguin on 2016. 7. 16..
 */

public class LuckOfToday {
	public LuckOfToday() {
		// DO NOTHING
	}
	
	public void run() {
        Date today = new Date();
        SimpleDateFormat dateForm = new SimpleDateFormat("yyyy년 MM월 dd일");
        Random random = new Random();
        int randInt = Math.abs(random.nextInt() % 100) + 1;

        String str = String.format("%s의 금전운(100)은 %d%%", dateForm.format(today), randInt);
        System.out.println(str);
	}
}
