package com.pwz.wiki.database.a_jdbc;

import java.sql.*;

/**
 * PreparedStatement防止SQL注入
 * 原理：将传入的参数进行转义处理，规避改变原sql语义的问题
 */
public class JDBC_5_PreparedStatement {

    public static void main(String[] args) throws Exception {
        // 注册驱动
        Class.forName("org.sqlite.JDBC");
        // 获取连接
        String url = "jdbc:sqlite:sqliteDB.db";
        String user = "root";
        String pwd = "root";
        Connection conn = DriverManager.getConnection(url, user, pwd);

        // 使用？作为占位符
        String sql = "select * from GUITAR where brand = ? or type = ?";
        // 构造PrepareStatement，通过其方法将参数设置好，注意问号序号从1开始
        PreparedStatement pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, "Fender");
        pstmt.setString(2, "Les Paul");

        // 查询数据
        ResultSet resultSet = pstmt.executeQuery();
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }

        pstmt.close();
        conn.close();

        //1, Fender, Stratocaster
        //2, Fender, Telecaster
        //3, Gibson, Les Paul
        //4, Epiphone, Les Paul
    }
}
