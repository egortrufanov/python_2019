package com.company;
///#10///

public class FourthClass {
    public static void main(String[] args) {
        int p = 0;
        for (int i = 0; i < 30; i++) {
            if (i % 2 == 0) {
                double d = (double) i / 4;
                System.out.print(d+"; ");
            }
        }
        System.out.println();
        int year = 2016;
        switch (year) {
            case 2014:
                System.out.println("You're 3rd year student");
                break;
            case 2015:
                System.out.println("You're 2nd year student");
                break;
            case 2016:
                System.out.println("You're 1st year student");
                break;
        }
        System.out.println();

        ///# 11///
        boolean[] bool = {false, true};
        boolean x, y, z;
        System.out.println("x1\tx2\tx3\ty");
//        for (int i = 0; i < bool.length; i++) {
//            x = bool[i];
//            for (int j = 0; j < bool.length; j++) {
//                y = bool[j];
//                for (int k = 0; k < bool.length; k++) {
//                    z = bool[k];
//                    System.out.println(Integer.toBinaryString(i) + "\t" + Integer.toBinaryString(j) + "\t" + Integer.toBinaryString(k) + "\t" + ((x & y | !z) ? 1 : 0));
//                }
//            }
//        }

        int i = 0;
        int j = 0;
        int k = 0;
//        while (i < bool.length) {
//            x = bool[i];
//            j = 0;
//            while (j < bool.length) {
//                y = bool[j];
//                k = 0;
//                while (k < bool.length) {
//                    z = bool[k];
//                    System.out.println(Integer.toBinaryString(i) + "\t" + Integer.toBinaryString(j) + "\t" + Integer.toBinaryString(k) + "\t" + ((x & y | !z) ? 1 : 0));
//                    k++;
//                }
//                j++;
//            }
//            i++;
//        }

        do {
            x = bool[i];
            j = 0;
            do {
                y = bool[j];
                k = 0;
                do {
                    z = bool[k];
                    System.out.println(Integer.toBinaryString(i) + "\t" + Integer.toBinaryString(j) + "\t" + Integer.toBinaryString(k) + "\t" + ((x & y | !z) ? 1 : 0));
                    k++;
                } while (k < bool.length);
                j++;
            } while (j < bool.length);
            i++;
        } while (i < bool.length);
        System.out.println();

        ///# 12///
        int count = 0;
        while (count < 130) {
            if (count % 7 == 0)
                System.out.print(count + " ");
            if (count == 69) break;
            count++;
        }
    }
}
