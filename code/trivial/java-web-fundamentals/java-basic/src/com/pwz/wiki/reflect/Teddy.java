package com.pwz.wiki.reflect;

public class Teddy {
    private String name;

    public Teddy(){
        this.name = "Det";
    };

    public Teddy(String name){
        this.name = name;
    }

    public void bark(){
        System.out.println(name + ": Arf, Arf.");
    }
}
