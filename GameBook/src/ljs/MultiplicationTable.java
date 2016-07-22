package ljs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

public class MultiplicationTable {
    /*
     * 총 5문제.
     */
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
		    this.nDan = 0;          // 1. 1~9까지 랜덤 숫자 할당 
        int randInt = 0;            // 2. 1~9까지 랜덤 숫자 할당 

        int answer = 0;             // 3. 컴퓨터 계산 정답 

        /* 4. 문항 출력 
         * 예시 
         * # 구구단 2단에 대한 문제입니다.
         *  -> 2 * 7 = 
         */
        
        int user_input_int = 0;     // 5. 사용자 정답 입력 
        
        if (answer == user_input_int) {
            System.out.println("맞았습니다!");
        } else {
            System.out.println(String.format("틀렸습니다. 정답은 %d입니다.", answer));
        }
	}
}
