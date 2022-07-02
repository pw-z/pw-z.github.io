package com.pwz.wiki.database.b_druid;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class DruidDemo {

    public static void main(String[] args) throws Exception {
        //1.配置druid依赖
        //详见POM文件

        //2.编写配置文件
        //详见druid.properties

        //3.加载配置文件
        Properties prop = new Properties();
        prop.load(new FileInputStream("java-web/src/main/java/com/pwz/wiki/database/druid/druid.properties"));

        //4.获取连接池对象
        DataSource dataSource = DruidDataSourceFactory.createDataSource(prop);

        //5.获取数据库连接
        Connection conn = dataSource.getConnection();
        System.out.println(conn);

        //6.执行sql
        Statement statement = conn.createStatement();
        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }

        //Jun 27, 2022 12:54:13 AM com.alibaba.druid.pool.DruidDataSource error
        //SEVERE: testWhileIdle is true, validationQuery not set
        //Jun 27, 2022 12:54:13 AM com.alibaba.druid.pool.DruidDataSource info
        //INFO: {dataSource-1} inited
        //org.sqlite.jdbc4.JDBC4Connection@57fa26b7
        //1, Fender, Stratocaster
        //2, Fender, Telecaster
        //3, Gibson, Les Paul
        //4, Epiphone, Les Paul
    }

}
