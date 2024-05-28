package com.pwz.wiki.reflect;

/***
 * 3种途径获取类对象
 */
public class ReflectGetClass {

    public static void main(String[] args) throws Exception {

        // 通过全类名
        Class t = Class.forName("com.pwz.wiki.reflect.Teddy");
        System.out.println(t);
        ((Teddy)t.newInstance()).bark();

        // 通过类本身
        Class c = Teddy.class;
        System.out.println(c);

        // 通过实例
        Teddy teddy = new Teddy();
        Class x = teddy.getClass();
        System.out.println(x);
    }
}
