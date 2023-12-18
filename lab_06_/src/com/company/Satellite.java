package com.company;
///# 14///
public class Satellite {
///#16///
    String name;
    Double radius; //радиус спутника
    Double period; //период обращения спутника (в часах)
///# 18///
    public Satellite(String name, Double radius, Double period) {
        this.name = name;
        this.radius = radius;
        this.period = period;
    }

    public double getPeriod() {
        return period;
    }

    public double getPeriodInDays() {
        return period / 24;
    }

    public void print() {
        System.out.println("Name of satellite: " + name);
        System.out.println("The radius: " + radius);
        System.out.println("Period: " + period);
    }
}
