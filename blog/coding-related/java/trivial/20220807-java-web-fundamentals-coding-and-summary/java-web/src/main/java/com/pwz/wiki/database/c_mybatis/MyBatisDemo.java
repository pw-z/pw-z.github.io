package com.pwz.wiki.database.c_mybatis;

import com.pwz.wiki.database.c_mybatis.mapper.GuitarMapper;
import com.pwz.wiki.database.c_mybatis.pojo.Guitar;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.InputStream;
import java.util.List;

public class MyBatisDemo {

    public static void main(String[] args) throws Exception {

        //加载mybatis配置文件，获取SqlSessionFactory
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory =
                new SqlSessionFactoryBuilder().build(inputStream);

        //获取SqlSession用于执行sql
        SqlSession sqlSession = sqlSessionFactory.openSession();

        //执行sql
        ///获取mapper代理对象
        GuitarMapper guitarMapper = sqlSession.getMapper(GuitarMapper.class);
        //调用mapper方法
        List<Guitar> guitars = guitarMapper.selectAllGuitar();
        System.out.println(guitars);

        //释放资源
        sqlSession.close();

    }
    //[Guitar{id='1', brand='Fender', type='Stratocaster'}, Guitar{id='2', brand='Fender', type='Telecaster'}, Guitar{id='3', brand='Gibson', type='Les Paul'}, Guitar{id='4', brand='Epiphone', type='Les Paul'}]
}
