package com.pwz.wiki.annotation;

public @interface MyAnnotation {

    public String tag() default "myTag";
    public String note() default "注解属性必须写括号！";
    public int whatever();
}
