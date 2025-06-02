package pwz.bcms.db;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.swing.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.sql.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class DatabaseHandler {

    private static DatabaseHandler handler = null;
    private static boolean initDB = false;

    private static final String DB_URL = "jdbc:derby:database;create=true";
    /**
     * note@2087
     * 关于Connection类：
     * ①、Connection是一个接口，是高度抽象的集合。它包含了集合的基本操作：对集合元素的增、删、改、查、判断是否为空，获取大小、遍历等操作；
     * ②、根据Connection接口规范的建议：Collection接口的所有子类(直接子类和间接子类)都必须实现2种构造函数：不带参数的构造函数 和 参数为Collection的构造函数。
     * 关于Statement
     * Statement 是 Java 执行数据库操作的一个重要方法，用于在已经建立数据库连接的基础上，向数据库发送要执行的SQL语句。Statement对象，用于执行不带参数的简单SQL语句。
     * 与此差不多的还有PreparedStatement，PreparedStatement 继承了Statement，一般如果已经是稍有水平开发者，应该以PreparedStatement代替Statement。
     */
    private static Connection conn = null;
    private static Statement stmt = null;

    private DatabaseHandler() {
        //System.out.println("---- 创建新的DatabaseHandler");
        createConnection();
        inflateDB();
    }

    public static DatabaseHandler getInstance() {
        if (handler == null) {
            handler = new DatabaseHandler();
        }
        return handler;
    }

    public static Connection getConnection() {
        return conn;
    }

    //Note@2087 创建数据库连接
    public void createConnection() {
        try {
            System.out.println("Note@2087 try createConnection");
            /**
             * note@2087
             * Class.forName作用就是初始化给定的类
             * Class.forName等价于DriverManager.registerDriver(new Driver)
             */
            Class.forName("org.apache.derby.jdbc.EmbeddedDriver").newInstance();
            conn = DriverManager.getConnection(DB_URL); //Note@2087 通过预设的URL字符串常量 初始化connection
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //Note@2087 加载数据库（没有则创建）
    private static void inflateDB() {
        System.out.println("加载数据库");
        List<String> tableData = new ArrayList<>();
        try {
            Set<String> loadedTables = getDBTables();
            System.out.println("Already loaded tables " + loadedTables);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            /**
             * Note@2087
             * 获取xml文件中的数据库表结构
             */
            Document doc = dBuilder.parse(DatabaseHandler.class.getClass().getResourceAsStream("/pwz/bcms/db/tables.xml"));
            NodeList nList = doc.getElementsByTagName("table-entry");
            for (int i = 0; i < nList.getLength(); i++) {
                Node nNode = nList.item(i);
                Element entry = (Element) nNode;
                String tableName = entry.getAttribute("name");
                String query = entry.getAttribute("col-data");
                if (!loadedTables.contains(tableName.toLowerCase())) {//如果没有加载到对应数据库表，则加载表结构进tableData集合
                    tableData.add(String.format("CREATE TABLE %s (%s)", tableName, query));
                }
            }
            if (tableData.isEmpty()) { //如果表结构为空，证明前面加载了已经存在的数据库
                System.out.println("Tables are already loaded");
            }
            else { //不然则为首次使用本软件，应初始化（创建）数据库表
                System.out.println("Inflating new tables.");
                createTables(tableData);
            }
        }
        catch (Exception ex) {
            //LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - DatabaseHandler---inflateDB--setupDatabase");
        }
    }


    //获取数据库表
    private static Set<String> getDBTables() throws SQLException {
        Set<String> set = new HashSet<>();
        DatabaseMetaData dbmeta = conn.getMetaData();
        readDBTable(set, dbmeta, "TABLE", null);
        return set;
    }

    //读取数据库表 放入set集合
    private static void readDBTable(Set<String> set, DatabaseMetaData dbmeta, String searchCriteria, String schema) throws SQLException {
        ResultSet rs = dbmeta.getTables(null, schema, null, new String[]{searchCriteria});
        while (rs.next()) {
            set.add(rs.getString("TABLE_NAME").toLowerCase());
        }
    }

    //创建数据库表
    private static void createTables(List<String> tableData) throws SQLException {
        Statement statement = conn.createStatement();
        statement.closeOnCompletion();
        for (String command : tableData) {
            System.out.println(command);
            statement.addBatch(command);
        }
        statement.executeBatch();
    }



    //查询语句执行方法
    public ResultSet execQuery(String query) {
        ResultSet result;
        try {
            stmt = conn.createStatement();
            result = stmt.executeQuery(query);
        } catch (SQLException ex) {
            System.out.println("Exception at execQuery:dataHandler" + ex.getLocalizedMessage());
            return null;
        } finally {

        }
        return result;
    }

    //数据库操作（增、删、改）语句执行方法
    public boolean execAction(String qu) {
        try {
            stmt = conn.createStatement();
            stmt.execute(qu);
            return true;
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Error:" + ex.getMessage(), "Error Occured",
                JOptionPane.ERROR_MESSAGE);
            System.out.println("Exception at execQuery:dataHandler" + ex.getLocalizedMessage());
            return false;
        } finally {

        }
    }

}

