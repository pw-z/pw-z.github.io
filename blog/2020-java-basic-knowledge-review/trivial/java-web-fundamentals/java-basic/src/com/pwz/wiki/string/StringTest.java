package com.pwz.wiki.string;

import java.util.Arrays;

/**
 * String各种基础操作
 */
public class StringTest {

    public static void main(String[] args) {
        String s = "012345abcdef";

        // 索引
        char c = s.charAt(1);
        System.out.println(c);

        // 遍历
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            System.out.print(c);
        }
        System.out.println();

        // 转字符数组
        char[] chars = s.toCharArray();
        System.out.println(Arrays.toString(chars));

        // 截取
        String subs = s.substring(3);
        System.out.println(subs);
        subs = s.substring(2, 5);
        System.out.println(subs);

        // 替换
        System.out.println(s);
        s = s.replace("123", "iii");
        System.out.println(s);

        // 包含判断
        String target = "123";
        System.out.println(s.contains(target));
        target = "iii";
        System.out.println(s.contains(target));

        // 分割
        String origin = "abc,123,oiu,pwz";
        String[] after = origin.split(",");
        System.out.println(Arrays.toString(after));


        //1
        //012345abcdef
        //[0, 1, 2, 3, 4, 5, a, b, c, d, e, f]
        //345abcdef
        //234
        //012345abcdef
        //0iii45abcdef
        //false
        //true
        //[abc, 123, oiu, pwz]
    }
}
