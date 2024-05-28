package com.pwz.wiki.annotation;

@MyAnnotation(whatever = 3)
public class AnnotationTest {

    @MyAnnotation(tag = "test_field", whatever = 5)
    //@MyAnnotationLimitedOnMethod // error
    private String test;

    @MyAnnotation(tag = "test_method", whatever = 4)
    @MyAnnotationLimitedOnMethod
    public void test(){}
}
