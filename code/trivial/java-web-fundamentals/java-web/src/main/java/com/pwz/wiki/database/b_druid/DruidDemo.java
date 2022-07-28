package com.pwz.wiki.database.b_druid;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.FileInputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class DruidDemo {

    /**
     * 使用DataSource统一管理数据库连接
     * 需要做的就是创建DruidDataSourceFactory，然后通过它获取dataSource，再通过dataSource获取connection就行了
     * druid初始化需要传入配置信息，配置文件中可以配置的参数，具体见官网，参数名是规定好的，不要自己处理
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        //1.配置druid依赖
        //详见POM文件

        //2.编写配置文件
        //详见druid.properties

        //3.加载配置文件
        Properties prop = new Properties();
//        prop.load(Files.newInputStream(Paths.get("./druid.properties")));
        prop.load(DruidDemo.class.getClassLoader().getResourceAsStream("druid.properties"));

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
