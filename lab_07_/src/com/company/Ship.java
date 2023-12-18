package com.company;
///# 11///
public class Ship {

    private String title;
    private String captainName;
    private int port;
    private char type;

    public void updateShipInfo(String title, int port) {
        this.title = title;
        this.port = port;

        System.out.println("Title: " + this.title + "; port: " + this.port);
    }

    // Компилятор ругается, потому что метод с переменными таких же типов уже создан
//    public void updateShipInfo(String captainName, String title) {
//        this.title = title;
//        this.captainName = captainName;
//
//        System.out.println("Title: " + this.title + "; captain's name: " + this.captainName);
//    }

    public void updateShipInfo(String captainName, char type, int port) {
        this.captainName = captainName;
        this.type = type;
        this.port = port;

        System.out.println("Captain's name: " + this.captainName + "; type of ship: " + this.type + "; port: " + this.port);
    }

    public void updateShipInfo(String title, String captainName) {
        this.title = title;
        this.captainName = captainName;

        System.out.println("Title: " + this.title + "; captain's name: " + this.captainName);
    }

    public void updateShipInfo(String title, char type) {
        this.title = title;
        this.type = type;

        System.out.println("Title: " + this.title + "; type of ship: " + this.type);
    }

}
