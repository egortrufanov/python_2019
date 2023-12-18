package com.company;
///# 20///
public class FifthClass {
    public static void main(String[] args) {
        Satellite satellite = new Satellite("Moon", 2000.0, 84.0);
        Planet planet = new Planet("Earth-01", 6371.0, 149.6);

        System.out.println("Satellite period: " + satellite.getPeriod());
        System.out.println("Satellite period (in days): " + satellite.getPeriodInDays());
        System.out.println("Print data about satellite with print: ");
        satellite.print();
        System.out.println();

        System.out.println(planet.name);
        planet.setName("Earth");
        System.out.println(planet.getName());
        System.out.println(planet.toThousandKm("radius"));
    }
}
