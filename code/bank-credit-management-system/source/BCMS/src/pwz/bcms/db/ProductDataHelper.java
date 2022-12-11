package pwz.bcms.db;

import pwz.bcms.po.Product;

import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ProductDataHelper {

    //Product(String id, String name, String points, String tlimit, String flag, String note)
    //增
    public static boolean insertNewProduct(Product product) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "INSERT INTO PRODUCT(name,points,tlimit,flag,note) VALUES(?,?,?,?,?)");
            statement.setString(1, product.getName());
            statement.setString(2, product.getPoints());
            statement.setString(3, product.getTlimit());
            statement.setString(4, product.getFlag());
            statement.setString(5, product.getNote());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - insertProduct");
        }
        return false;
    }

    //Gift(String id, String name, String type, String value, Boolean flag, String note)
    //改
    public static boolean updateProduct(Product product) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "UPDATE PRODUCT SET name=?,points=?,tlimit=?,flag=?,note=? WHERE id = ?");
            statement.setString(1, product.getName());
            statement.setString(2, product.getPoints());
            statement.setString(3, product.getTlimit());
            statement.setString(4, product.getFlag());
            statement.setString(5, product.getNote());
            statement.setString(6, product.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - updateProduct");
        }
        return false;
    }

    //删
    public static boolean deleteProduct(Product product) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "DELETE FROM PRODUCT WHERE id = ?");
            statement.setString(1,product.getId());  //根据ID来删除礼物

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - deleteProduct");
        }
        return false;
    }
}
