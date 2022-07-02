package com.pwz.wiki.database.a_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class JDBC_3_Statement {

    public static void testDML() throws Exception {
        // 注册驱动
        Class.forName("org.sqlite.JDBC");
        // 获取连接
        String url = "jdbc:sqlite:sqliteDB.db";
        String user = "root";
        String pwd = "root";
        Connection conn = DriverManager.getConnection(url, user, pwd);

        //获取执行sql的对象
        Statement statement = conn.createStatement();

        String sql = "INSERT INTO GUITAR VALUES('5', 'TEMPFender', 'TEMPStratocaster')";
        int count = statement.executeUpdate(sql);  // 执行DML将返回该sql影响的行数
        System.out.println(count);
        if(count > 0){
            System.out.println("nice");
        }else{
            System.out.println("oops");
        }

        //查询数据
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }

        statement.close();
        conn.close();
    }

    public static void testDDL() throws Exception{
        // DDL语句也通过statement.executeUpdate(sql)方法执行
        // 需要注意的是，DDL可能执行成功时返回结果为0，比如drop表
    }

    public static void testDQL() {
        // 查询通过statement.executeQuery()执行，不再赘述
    }

    public static void main(String[] args) throws Exception {
        JDBC_3_Statement.testDML();
        //1
        //nice
        //1, Fender, Stratocaster
        //2, Fender, Telecaster
        //3, Gibson, Les Paul
        //4, Epiphone, Les Paul
        //5, TEMPFender, TEMPStratocaster

        // DDL语句也通过
    }
}
