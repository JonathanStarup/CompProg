import java.io.BufferedReader;
import java.io.Console;
import java.util.Collections;
import java.util.Scanner;

class EchoEchoEcho {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String output = String.join(" ", Collections.nCopies(3, word));
        System.out.println(output);
        System.console().r.
    }
}