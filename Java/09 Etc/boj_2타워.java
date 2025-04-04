/**
 * 1(2의 1) 2 .. 2
 * 2(2의 2) 4 .. 1
 * 3(2의 4) 16 .. 1
 * 4(2의 16) 65536 .. 1
 */
import java.io.*;
import java.math.BigInteger;

public class boj_2타워 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        BigInteger n = new BigInteger(br.readLine());

        if (n.equals(BigInteger.valueOf(1))) bw.write("2\n");
        else bw.write("1\n");

        bw.flush();
        bw.close();
    }
}