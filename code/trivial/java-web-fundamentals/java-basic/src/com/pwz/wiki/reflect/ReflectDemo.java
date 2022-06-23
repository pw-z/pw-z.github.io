package com.pwz.wiki.reflect;

import java.lang.reflect.Constructor;

public class ReflectDemo {

    public static void main(String[] args) throws Exception {


        Class t = Class.forName("com.pwz.wiki.reflect.Teddy");
        System.out.println(t);
        ((Teddy)t.newInstance()).bark();

        Class c = Teddy.class;
        System.out.println(c);

        Teddy teddy = new Teddy();
        Class x = teddy.getClass();
        System.out.println(x);


        // -------------------------------------

        Class a = Teddy.class;
        Constructor cons = a.getDeclaredConstructor(String.class);
        Object o = cons.newInstance("Ted");
        ((Teddy)o).bark();

    }
}
