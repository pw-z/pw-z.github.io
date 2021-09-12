package pwz.bcms.db;

import pwz.bcms.po.Gift;

import java.sql.PreparedStatement;
import java.sql.SQLException;

public class GiftDataHelper {


    //增
    public static boolean insertNewGift(Gift gift) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "INSERT INTO GIFT(name,type,value,flag,note) VALUES(?,?,?,?,?)");
            statement.setString(1, gift.getName());
            statement.setString(2, gift.getType());
            statement.setString(3, gift.getValue());
            statement.setString(4, gift.getFlag());
            statement.setString(5, gift.getNote());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - insertCSR");
        }
        return false;
    }

    //Gift(String id, String name, String type, String value, Boolean flag, String note)
    //改
    public static boolean updateGift(Gift gift) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "UPDATE GIFT SET name=?,type=?,value=?,flag=?,note=? WHERE id = ?");
            statement.setString(1, gift.getName());
            statement.setString(2, gift.getType());
            statement.setString(3, gift.getValue());
            statement.setString(4, gift.getFlag());
            statement.setString(5, gift.getNote());
            statement.setString(6, gift.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - insertCSR");
        }
        return false;
    }

    //删
    public static boolean deleteGift(Gift gift) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "DELETE FROM GIFT WHERE id =?");
            statement.setString(1,gift.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - insertCSR");
        }
        return false;
    }

}
