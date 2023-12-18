package com.company;

import java.util.ArrayList;
import java.util.Scanner;

public class Polinoms {

    public int binary_search(ArrayList<Double> a, double s, int n) {

        int result = 0;
        int left = 0, right = n - 1, mid = 0;

        return result;
    }

    public static void main(String[] args) {

        ArrayList<Double> w = new ArrayList<>(); //array of numbers, which we get from user
        Scanner in = new Scanner(System.in);
        int n = 0; // amount of numbers
        double s = 0.0;

        System.out.println("Enter amount of numbers: ");
        n = in.nextInt();
        System.out.println("Enter numbers and in the end the number 's': ");
        for (int i = 0; i < n; i++) {
            w.add(in.nextDouble());
        }
        s = in.nextDouble();
    }
}
