package com.company;

public class Dollars extends Bank_Account {

    char type_of_currency = 'D';

    public Dollars(String number, double limit, double current) {
        super(number, limit, current);
    }

    public void print() {
        System.out.println("The account " + this.number_bank_cell +
                " has " + this.current + " dollars. It can contain " + this.limit + ".");
    }

    public double toRubbles() {
        return this.current * 63.5;
    }
}
