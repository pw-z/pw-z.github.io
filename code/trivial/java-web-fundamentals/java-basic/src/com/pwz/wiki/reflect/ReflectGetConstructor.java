package com.pwz.wiki.reflect;

import java.io.InputStream;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.Arrays;

/***
 * 4个方法获取构造器，通过构造器实例化对象
 */
public class ReflectGetConstructor {
    public static void main(String[] args) throws Exception {

        // 获取所有public构造器
        Constructor[] cons1 = Teddy.class.getConstructors();
        System.out.println(Arrays.toString(cons1));
        // [public com.pwz.wiki.reflect.Teddy(java.lang.String), public com.pwz.wiki.reflect.Teddy()]

        // 获取特定public构造器（根据参数）(获取private类型的会报错)
        Constructor cons2 = Teddy.class.getConstructor(String.class);
        System.out.println(cons2);
        // public com.pwz.wiki.reflect.Teddy(java.lang.String)


        // 获取所有构造器（包括private）
        Constructor[] cons3 = Teddy.class.getDeclaredConstructors();
        System.out.println(Arrays.toString(cons3));
        // [private com.pwz.wiki.reflect.Teddy(java.lang.String,int), public com.pwz.wiki.reflect.Teddy(java.lang.String), public com.pwz.wiki.reflect.Teddy()]

        // 获取特定构造器（包括private）
        Constructor cons4 = Teddy.class.getDeclaredConstructor(String.class, int.class);
        System.out.println(cons4);
        // private com.pwz.wiki.reflect.Teddy(java.lang.String,int)

        // -------------------------------

        // 通过public构造器创建实例
        Teddy t = (Teddy) cons2.newInstance("Ted");
        t.bark(2);
        // Ted: Arf, Arf.
        // Ted: Arf, Arf.

        // 通过private构造器创建实例
        cons4.setAccessible(true);
        Teddy t2 = (Teddy) cons4.newInstance("Ted", 3);
        t2.bark("Private Arf.");
        // Ted: Private Arf.
    }
}
