package ksw;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

/**
 * Created by CubePenguin on 2016. 7. 16..
 */
public class RockPaperScissors {
   public RockPaperScissors() {
       // DO NOTHING
   }
    
    public void run() throws IOException {
        Random random = new Random();

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String user_choice;
        System.out.print("가위, 바위, 보 중 하나를 선택하세요 (가위:c, 바위:r, 보:p) ? ");
        user_choice = in.readLine();

        int com_choice = Math.abs(random.nextInt() % 3); 

        if (user_choice.equals("c")) {
            switch (com_choice) {
                case 0:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "가위", "가위", "무승부!"));
                    break;
                case 1:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "가위", "바위", "컴퓨터 승!"));
                    break;
                case 2:
                    System.out.println(String.format("사람: %s, 컴퓨터: %s -> %s", "가위", "보", "사람 승!"));
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
