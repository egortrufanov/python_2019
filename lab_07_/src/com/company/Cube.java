package com.company;
///# 1///
public class Cube {
    public double width;
    private double height;
    protected double depth;

    public Cube(double width, double height, double depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }

    public void print() {
        System.out.println(this.width + " | " + this.height + " | " + this.depth);
    }
}
