package com.company;

public class Plant {
///# 8, 10///
    private String type;
    private String color;
    private String existenceArea;
    private boolean rare;

    public Plant() {}

    public Plant(String type, String color) {
        this.type = type;
        this.color = color;
    }

    public Plant(String existenceArea, boolean rare){
        this.existenceArea = existenceArea;
        this.rare = rare;
    }

    public Plant(String type) {
        this.type = type;
    }

    public void print() {
        System.out.println("type: " + this.type + "; color: " + this.color + "; existence area: " + this.existenceArea + "; rareness: " + this.rare);
    }
}
