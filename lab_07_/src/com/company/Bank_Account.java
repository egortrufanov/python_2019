package com.company;

public class Bank_Account {

    static String name = "Trufanov Egor Vladimirovich";
    String number_bank_cell;
    double limit;
    double current;

    public Bank_Account() {}

    public Bank_Account(String number_bank_cell, double limit, double current) {
        this.current = current;
        this.limit = limit;
        this.number_bank_cell = number_bank_cell;
    }

    public void print() {
        System.out.println("Number: " + this.number_bank_cell);
        System.out.println("Limit: " + this.limit);
        System.out.println("Current: " + this.current);
    }

}
