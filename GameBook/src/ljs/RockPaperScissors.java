package ljs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

public class RockPaperScissors {
    /*
     * 총 3문제.
     */
   public RockPaperScissors() {
       
   }
    
    public void run() throws IOException {
        Random random = new Random();

        /*
         * 아래 코드로 사용자 입력을 받을 수 있다.
         */
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String user_choice;
        System.out.print("가위, 바위, 보 중 하나를 선택하세요 (가위:c, 바위:r, 보:p) ? ");
        user_choice = in.readLine();

        /*
         * 아래 코드로 1~3까지 랜덤 숫자를 할당받을 수 있다.
         */
        int com_choice = Math.abs(random.nextInt() % 3); 

        if (user_choice.equals("c")) {
            switch (com_choice) {
                case 0:
                    System.out.println(String.format(""));  // 1. 출력: 가위 vs 가위 
                    break;
                case 1:
                    System.out.println(String.format(""));  // 2. 출력: 가위 vs 바위 
                    break;
                case 2:
                    System.out.println(String.format(""));  // 3. 출력: 가위 vs 보 
                    break;
                default:
                    System.out.println("컴퓨터 입력이 잘못되었습니다.");
            }
        } else if (user_choice.equals("r")) {
            switch (com_choice) {
                case 0:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "바위", "가위", "사람 승!"));
                    break;
                case 1:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "바위", "바위", "무승부!"));
                    break;
                case 2:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "바위", "보", "컴퓨터 승!"));
                    break;
                default:
                    System.out.println("컴퓨터 입력이 잘못되었습니다.");
            }
        } else if (user_choice.equals("p")) {
            switch (com_choice) {
                case 0:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "보", "가위", "컴퓨터 승!"));
                    break;
                case 1:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "보", "바위", "사람 승!"));
                    break;
                case 2:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "보", "보", "무승부!"));
                    break;
                default:
                    System.out.println("컴퓨터 입력이 잘못되었습니다.");
            }
        } else {
            System.out.println("사용자 입력이 잘못되었습니다.");
        }

    }
}
