package ksw.multiplicationtables;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

/**
 * Created by CubePenguin on 2016. 7. 16..
 */
public class Launch {
    public static void main(String[] args) throws IOException{
        int nDan, randInt;
        Random random = new Random();

        if (args.length == 1) {
            nDan = Integer.valueOf(args[0]);
        } else {
            nDan = Math.abs(random.nextInt() % 9) + 1;
        }

        randInt = Math.abs(random.nextInt() % 9) + 1;

        int answer = nDan * randInt;

        System.out.print(String.format("\n# 구구단 %d단에 대한 문제입니다.\n -> %d * %d = ", nDan, nDan, randInt));

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
