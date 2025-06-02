package com.pwz.wiki.reflect;

import java.lang.reflect.Field;
import java.util.Arrays;

/**
 * 获取成员变量
 */
public class ReflectGetField {

    public static void main(String[] args) throws NoSuchFieldException {

        // 获取全部public成员变量
        Field[] f1 = Teddy.class.getFields();
        System.out.println(Arrays.toString(f1));

        // 获取特定public成员变量
        Field f2 = Teddy.class.getField("size");
        System.out.println(f2);

        // 获取全部成员变量
        Field[] f3 = Teddy.class.getDeclaredFields();
        System.out.println(Arrays.toString(f3));

        // 获取特定成员变量（可取private属性）
        Field f4 = Teddy.class.getDeclaredField("name");
        System.out.println(f4);

        //[public java.lang.String com.pwz.wiki.reflect.Teddy.size, public java.lang.String com.pwz.wiki.reflect.Teddy.color]
        //public java.lang.String com.pwz.wiki.reflect.Teddy.size
        //[private final java.lang.String com.pwz.wiki.reflect.Teddy.name, private int com.pwz.wiki.reflect.Teddy.age, public java.lang.String com.pwz.wiki.reflect.Teddy.size, public java.lang.String com.pwz.wiki.reflect.Teddy.color]
        //private final java.lang.String com.pwz.wiki.reflect.Teddy.name
    }
}
