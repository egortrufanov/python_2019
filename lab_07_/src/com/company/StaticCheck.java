package com.company;
///# 7///
public class StaticCheck {

    public static void main(String[] args) {
        while (true) {
            StaticContainer.operation();
            if (StaticContainer.counter > 100) {
                System.out.println(StaticContainer.counter);
                break;
            }
        }
    }

}
