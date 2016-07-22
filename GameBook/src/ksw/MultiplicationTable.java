package ksw;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

/**
 * Created by CubePenguin on 2016. 7. 16..
 */
public class MultiplicationTable {
	int nDan;
	
	public MultiplicationTable() {
		this.nDan = 0;
	}
	
	public MultiplicationTable(int nDan) {
		this.nDan = nDan;
	}
	
	public void setNdan(int inputNdan) {
		this.nDan = inputNdan;
	}
	
	public int getNdan() {
		return this.nDan;
	}
	
	public void run() throws IOException {
		Random random = new Random();

		if (this.nDan == 0)
		    this.setNdan(Math.abs(random.nextInt() % 9) + 1);
        int randInt = Math.abs(random.nextInt() % 9) + 1;

        int answer = this.nDan * randInt;

        System.out.print(String.format("# 구구단 %d단에 대한 문제입니다.\n -> %d * %d = ", 
        		this.nDan, this.nDan, randInt));

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String user_input_str;
        user_input_str = in.readLine();
        int user_input_int = Integer.valueOf(user_input_str);

        if (answer == user_input_int) {
            System.out.println("맞았습니다!");
        } else {
            System.out.println(String.format("틀렸습니다. 정답은 %d입니다.", answer));
        }
	}
}
