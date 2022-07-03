package com.pwz.wiki.database.a_jdbc;

import java.sql.*;

public class JDBC_2_Connection {
    private static final String JDBC_URL = "jdbc:sqlite:sqliteDB.db";
    private static final String DRIVER_CLASS = "org.sqlite.JDBC";
    private static final String USER = "root";
    private static final String PASSWORD = "root";

    public static void main(String[] args) throws Exception {

        //连接数据库
        Class.forName(DRIVER_CLASS);
        Connection conn = DriverManager.getConnection(JDBC_URL, USER, PASSWORD);
        Statement statement = conn.createStatement();

        try {
            //开启事务
            conn.setAutoCommit(false);

            //查询数据
            ResultSet resultSet = statement.executeQuery("select * from GUITAR");
            while (resultSet.next()) {
                System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
            }

            //插入测试数据
            statement.executeUpdate("INSERT INTO GUITAR VALUES('5', 'Fender', 'Stratocaster') ");
            statement.executeUpdate("INSERT INTO GUITAR VALUES('6', 'Fender', 'Telecaster') ");

            //提交事务
            conn.commit();
        } catch (Exception e) {
            //回滚事务
            conn.rollback();
        }

        //查询数据
        System.out.println();
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }


        //关闭连接
        statement.close();
        conn.close();
    }
}
