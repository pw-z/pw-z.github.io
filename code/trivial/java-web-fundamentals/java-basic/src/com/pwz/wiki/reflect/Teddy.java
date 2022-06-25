package com.pwz.wiki.reflect;

public class Teddy {
    private final String name;
    private int age;
    public String size;
    public String color;

    public Teddy(){
        this.name = "Det";
    };

    public Teddy(String name){
        this.name = name;
    }

    private Teddy(String name, int age){
        this.name = name;
        this.age = age;
    }

    public void bark(){
        System.out.println(name + ": Arf, Arf.");
    }

    public void bark(String word){
        System.out.println(name + ": " + word);
    }

    public void bark(int count){
        for (int i = 0; i < count; i++) {
            bark();
        }
    }
}
