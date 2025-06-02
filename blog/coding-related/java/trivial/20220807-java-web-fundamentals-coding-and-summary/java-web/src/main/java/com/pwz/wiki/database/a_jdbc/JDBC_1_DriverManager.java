package com.pwz.wiki.database.a_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class JDBC_1_DriverManager {

    public static void main(String[] args) throws Exception {
        // 通过DriverManager获取数据库连接
        // 3个参数，数据库URL+用户名+密码

        Class.forName("org.sqlite.JDBC");
        // 注册驱动，此处可以通过forName的形式注册驱动，是因为驱动类中的静态代码块：
        // static {
        //        try {
        //            DriverManager.registerDriver(new JDBC());
        //        } catch (SQLException var1) {
        //            var1.printStackTrace();
        //        }
        //
        //    }

        // 获取连接
        // url的格式规范：【协议://IP:端口/数据库名称？参数键值对1&参数键值对2...】
        // url示例：jdbc:mysql://127.0.0.1:3306/test_db?useSSL=false
        // url连接本机数据库，且端口式默认的3306时，可以简写为jdbc:mysql:///test_db?useSSL=false
        String url = "jdbc:sqlite:sqliteDB.db";
        String user = "root";
        String pwd = "root";
        Connection conn = DriverManager.getConnection(url, user, pwd);

        //获取执行sql的对象
        Statement statement = conn.createStatement();
        //查询数据
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }

        statement.close();
        conn.close();
    }
}
