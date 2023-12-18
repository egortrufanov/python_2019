package com.company;

import java.util.Scanner;

public class BANK {
    public static void main(String[] args) {

        String num = "";
        double cur = 0.0;
        double lim = 0.0;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the number of account with rubbles: ");
        num = in.nextLine();
        System.out.println("Enter the current value of rubbles: ");
        cur = in.nextDouble();
        System.out.println("Enter the limit value of rubbles: ");
        lim = in.nextDouble();
        Rubles rub = new Rubles(num, lim, cur);

        System.out.println("Enter the number of account with dollars: ");
        num = in.next();
        System.out.println("Enter the current value of dollars: ");
        cur = in.nextDouble();
        System.out.println("Enter the limit value of dollars: ");
        lim = in.nextDouble();
        Dollars dol = new Dollars(num, lim, cur);

        System.out.println();
        rub.print();
        System.out.println("The rubbles to dollars: " + rub.toDollars());

        System.out.println();
        dol.print();
        System.out.println("The dollars to rubbles: " + dol.toRubbles());
    }
}
