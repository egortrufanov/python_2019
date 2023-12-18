package com.company;
///# 13, 15, 17, 19///
public class Planet {

    String name;
    Double radius;
    Double sunDistance;
    Satellite satellite;

    public Planet(String name, Double radius, Double sunDistance) {
        this.name = name;
        this.radius = radius;
        this.sunDistance = sunDistance;
    }

    public void getSatelliteInfo() {
        System.out.println("Satellite name: " + satellite.name);
        System.out.println("Satellite radius: " + satellite.radius);
        System.out.println("Satellite period: " + satellite.period);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double toThousandKm(String param) {
        double result = 0;
        switch (param) {
            case "sunDistance":
                result = this.sunDistance / 1000;
            case "radius":
                result = this.radius / 1000;
        }
        return result;
    }

}
