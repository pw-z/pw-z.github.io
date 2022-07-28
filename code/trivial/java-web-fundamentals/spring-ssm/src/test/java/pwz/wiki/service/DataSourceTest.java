package pwz.wiki.service;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import pwz.wiki.config.SpringConfig;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class DataSourceTest {

    @Autowired
    private DataSource dataSource;

    @Test
    public void test() throws SQLException {
        //5.获取数据库连接
        Connection conn = dataSource.getConnection();
        System.out.println(conn);

        //获取执行sql的对象
        Statement statement = conn.createStatement();

        //创建表
        statement.execute("CREATE TABLE GUITAR(id VARCHAR(50) PRIMARY KEY, brand VARCHAR(10), type VARCHAR(10))");

        //插入测试数据
        statement.executeUpdate("INSERT INTO GUITAR VALUES('1', 'Fender', 'Stratocaster') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('2', 'Fender', 'Telecaster') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('3', 'Gibson', 'Les Paul') ");
        statement.executeUpdate("INSERT INTO GUITAR VALUES('4', 'Epiphone', 'Les Paul') ");

        ResultSet resultSet = statement.executeQuery("select * from GUITAR");
        while (resultSet.next()) {
            System.out.println(resultSet.getInt("id") + ", " + resultSet.getString("brand") + ", " + resultSet.getString("type"));
        }
    }
}
