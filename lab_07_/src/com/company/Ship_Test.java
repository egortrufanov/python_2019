package com.company;

public class Ship_Test {
    public static void main(String[] args) {

        Ship ship1 = new Ship();
        Ship ship2 = new Ship();

        ship1.updateShipInfo("Aurora", 4);
        ship1.updateShipInfo("Jack", 'A', 7);
        ship2.updateShipInfo("Kutuzov", "Petr");
        ship2.updateShipInfo("Alexander", 'D');
    }
}
