package com.pwz.wiki.reflect;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;

/**
 * 获取类方法
 */
public class ReflectGetMethod {

    public static void main(String[] args) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Method[] m1 = Teddy.class.getMethods();
        Method m2 = Teddy.class.getMethod("bark");
        Method[] m3 = Teddy.class.getDeclaredMethods();
        Method m4 = Teddy.class.getDeclaredMethod("bark", int.class);

        System.out.println(Arrays.toString(m1));
        System.out.println(m2);
        System.out.println(Arrays.toString(m3));
        System.out.println(m4);

        //获取到方法后触发方法
        m4.invoke(new Teddy(), 4);

        //[public void com.pwz.wiki.reflect.Teddy.bark(int), public void com.pwz.wiki.reflect.Teddy.bark(java.lang.String), public void com.pwz.wiki.reflect.Teddy.bark(), public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException, public final native void java.lang.Object.wait(long) throws java.lang.InterruptedException, public final void java.lang.Object.wait() throws java.lang.InterruptedException, public boolean java.lang.Object.equals(java.lang.Object), public java.lang.String java.lang.Object.toString(), public native int java.lang.Object.hashCode(), public final native java.lang.Class java.lang.Object.getClass(), public final native void java.lang.Object.notify(), public final native void java.lang.Object.notifyAll()]
        //public void com.pwz.wiki.reflect.Teddy.bark()
        //[public void com.pwz.wiki.reflect.Teddy.bark(int), public void com.pwz.wiki.reflect.Teddy.bark(java.lang.String), public void com.pwz.wiki.reflect.Teddy.bark()]
        //public void com.pwz.wiki.reflect.Teddy.bark(int)
        //Det: Arf, Arf.
        //Det: Arf, Arf.
        //Det: Arf, Arf.
        //Det: Arf, Arf.
    }
}
