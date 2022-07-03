package com.pwz.wiki.database.a_jdbc;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 * 数据库工具类<br>
 *
 * refer:<br>
 * <a href="https://www.bilibili.com/video/BV1Qf4y1T7Hx?p=30">JavaWeb基础教程~JDBC</a><br>
 * <a href="https://www.51cto.com/article/616432.html?edm">Java 生态圈中的嵌入式数据库，哪家强？ </a><br>
 * <a href="https://www.sqlite.org/index.html">SQLite Home Page</a><br>
 */
public class JDBC_0_QuickStart {

    /**
     * 以嵌入式连接方式连接数据库
     */
    private static final String JDBC_URL = "jdbc:sqlite:sqliteDB.db";
    private static final String DRIVER_CLASS = "org.sqlite.JDBC";
    private static final String USER = "root";
    private static final String PASSWORD = "root";

    public static void initSqliteDB() throws Exception {

        //注册驱动
        Class.forName(DRIVER_CLASS);
        //获取连接
        Connection conn = DriverManager.getConnection(JDBC_URL, USER, PASSWORD);
        //获取执行sql的对象
        Statement statement = conn.createStatement();

        //创建表
        statement.execute("CREATE TABLE GUITAR(id VARCHAR(50) PRIMARY KEY, brand VARCHAR(10), type VARCHAR(10))");

        //插入测试数据
        statement.executeUpdate("INSERT INTO GUITAR VALUES('1', 'Fender', 'Stratocaster') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('2', 'Fender', 'Telecaster') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('3', 'Gibson', 'Les Paul') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('4', 'Epiphone', 'Les Paul') ");

        //查询数据
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }
        //关闭连接
        statement.close();
        conn.close();
    }

    public static void main(String[] args) throws Exception {
        initSqliteDB();
    }
}
