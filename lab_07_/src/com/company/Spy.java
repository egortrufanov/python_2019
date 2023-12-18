package com.company;
///# 3///
public class Spy {
    public String name;
    private String realName;
    private int squad;

    private String getSpyInfo() {
        String info;
        info = name + " " + realName + " " + squad;
        return info;
    }

    public int getSquad() {
        return squad;
    }

    public String getName() {
        return name;
    }

    public String getRealName() {
        return realName;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setRealName(String realName) {
        this.realName = realName;
    }

    public void setSquad(int squad) {
        this.squad = squad;
    }

    public void print() {
        System.out.println("Name: " + getName() + "\nReal name: " + getRealName() + "\nSquad: " + getSquad());
        System.out.println("getSpyInfo: " + getSpyInfo());
    }
}
