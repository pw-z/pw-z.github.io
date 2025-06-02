package com.pwz.wiki.database.a_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class JDBC_4_ResultSet {

    public static void main(String[] args) throws Exception {
        // 注册驱动
        Class.forName("org.sqlite.JDBC");
        // 获取连接
        String url = "jdbc:sqlite:sqliteDB.db";
        String user = "root";
        String pwd = "root";
        Connection conn = DriverManager.getConnection(url, user, pwd);

        // 获取执行sql的对象
        Statement statement = conn.createStatement();

        // 查询数据
        // getXXX方法有两种重载形式，可以传入列序号，或者传入列名称
        // 注意！列序号从1开始
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }

        System.out.println("------------------------");

        ResultSet resultSet2 = statement.executeQuery("select * from GUITAR");
        while (resultSet2.next()) {
            System.out.println(resultSet2.getInt(1) + ", " + resultSet2.getString(2) + ", " + resultSet2.getString(3));
        }

        statement.close();
        conn.close();

        //1, Fender, Stratocaster
        //2, Fender, Telecaster
        //3, Gibson, Les Paul
        //4, Epiphone, Les Paul
        //5, TEMPFender, TEMPStratocaster
        //------------------------
        //1, Fender, Stratocaster
        //2, Fender, Telecaster
        //3, Gibson, Les Paul
        //4, Epiphone, Les Paul
        //5, TEMPFender, TEMPStratocaster
    }
}
