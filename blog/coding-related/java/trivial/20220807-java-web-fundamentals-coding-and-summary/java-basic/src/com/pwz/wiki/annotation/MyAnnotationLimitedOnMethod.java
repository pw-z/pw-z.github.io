package com.pwz.wiki.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * 元注解有两个：<br>
 * 1. Target： 注解有效范围，可用枚举在ElementType中<br>
 * 2. Retention：注解生命周期，可用枚举在RetentionPolicy<br>
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotationLimitedOnMethod {
}
