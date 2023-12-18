package com.company;

import java.util.Scanner;

public class Nomer_24 {

    public void n24(int n, int source, int receiver, int intermediary) {

        if (n > 0) {

            n24(n - 1, source, intermediary, receiver);
            System.out.println(source + " --> " + receiver);
            n24(n - 1, intermediary, receiver, source);

        }

    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Nomer_24 nomer_24 = new Nomer_24();
        nomer_24.n24(n, 1, 2, 3);

    }
}
