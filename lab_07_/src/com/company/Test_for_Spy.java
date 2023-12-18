package com.company;

public class Test_for_Spy {
    public static void main(String[] args) {
        Spy spy = new Spy();
        spy.setName("Bear");
        spy.setRealName("Andrey");
        spy.setSquad(7);

        System.out.println("Print info with getter: " + "\nName: " + spy.getName() + "\nReal name: " + spy.getRealName() + "\nSquad: " + spy.getSquad());
        System.out.println("Print all info immediately: ");
        spy.print();
    }
}
