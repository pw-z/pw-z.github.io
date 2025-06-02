package com.pwz.wiki.abc;

import java.util.Arrays;

public class ArrayTest {

    public void test(){
        // 静态初始化
        String[] s = new String[]{"abc", "xyz", "uv"};
        int[] i = {0, 1, 2, 3, 4};
        System.out.println(s);  // 数组变量存储的是地址
        System.out.println(i);
        System.out.println(s[0] + i[2]);
        System.out.println(i.length);
        //[Ljava.lang.String;@75b84c92
        //[I@6bc7c054
        //abc2
        //5

        // 动态初始化
        int[] a = new int[10];
        System.out.println(a.length);
        System.out.println(a[0]);
        System.out.println(a[4]);
        a[4] = 8976;
        System.out.println(a[4]);
        //10
        //0
        //0
        //8976

        // 数组默认值
        String[] strings = new String[1];
        char[] chars = new char[1];
        int[] ints = new int[1];
        float[] floats = new float[1];
        double[] doubles = new double[1];
        boolean[] booleans  = new boolean[1];
        byte[] bytes = new byte[1];
        System.out.println(strings[0]);
        System.out.println(chars[0]);
        System.out.println(ints[0]);
        System.out.println(floats[0]);
        System.out.println(doubles[0]);
        System.out.println(booleans[0]);
        System.out.println(bytes[0]);
        //null
        //
        //0
        //0.0
        //0.0
        //false
        //0
    }

    public static void changeArrayContent(int[] ints){
        System.out.println("===========");
        System.out.println(ints);
        System.out.println(Arrays.toString(ints));
        if(ints.length > 1){
            ints[0] = 111222;
        }
        System.out.println("============");
    }
    public static void main(String[] args) {
        int[] ints_origin = {11, 22, 33, 44, 55};
        System.out.println(ints_origin);
        changeArrayContent(ints_origin);
        System.out.println(Arrays.toString(ints_origin));
        //[I@75b84c92
        //===========
        //[I@75b84c92
        //[11, 22, 33, 44, 55]
        //============
        //[111222, 22, 33, 44, 55]
    }
}
