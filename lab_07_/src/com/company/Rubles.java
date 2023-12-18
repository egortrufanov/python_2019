package com.company;

public class Rubles extends Bank_Account {

    char type_of_currency = 'R';

    public Rubles(String number, double limit, double current) {
        super(number, limit, current);
    }

    public void print() {
        System.out.println("The account " + this.number_bank_cell +
                " has " + this.current + " rubbles. It can contain " + this.limit + ".");
    }

    public double toDollars() {
        return this.current / 64.2;
    }
}
