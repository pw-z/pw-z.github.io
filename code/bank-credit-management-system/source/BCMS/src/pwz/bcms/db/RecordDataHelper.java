package pwz.bcms.db;

import pwz.bcms.po.Record;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class RecordDataHelper {

    //增
    public static boolean insertNewRecord(Record record) {
        //转化util.date为sql.date
        java.sql.Date sqlDate = new java.sql.Date(record.getDate().getTime());
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "INSERT INTO RECORD(csr_name,card_number,account,product_name,product_points,value,date,type,points,intro_cardnumber,note,intro_flag,intro_pointsType,intro_name) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
            statement.setString(1, record.getCsr_name());
            statement.setString(2, record.getCard_number());
            statement.setString(3, record.getAccount());
            statement.setString(4, record.getProduct_name());
            statement.setInt(5, record.getProduct_points());
            statement.setString(6, record.getValue());
            statement.setDate(7, sqlDate);
            statement.setString(8, record.getType());
            statement.setInt(9, record.getPoints());
            statement.setString(10, record.getIntro_cardnumber());
            statement.setString(11, record.getNote());
            statement.setString(12, record.getIntro_flag());
            statement.setString(13, record.getIntro_pointsType()); //积分计算方式
            statement.setString(14, record.getIntro_name()); //转介绍人姓名

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
            System.err.println(ex.getMessage() + " - - - insertNewRecord");
        }
        return false;
    }


    //改
    public static boolean updateNewRecord(Record record) {

        //转化util.date为sql.date
        java.sql.Date sqlDate = new java.sql.Date(record.getDate().getTime());

        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "UPDATE RECORD SET csr_name=?,account=?,product_name=?,product_points=?,value=?,date=?,type=?,points=?,intro_cardnumber=?,note=?,intro_flag=?,intro_pointsType=?,intro_name=? WHERE id=? ");
            statement.setString(1, record.getCsr_name());
            statement.setString(2, record.getAccount());
            statement.setString(3, record.getProduct_name());
            statement.setInt(4, record.getProduct_points());
            statement.setString(5, record.getValue());
            statement.setDate(6, sqlDate);
            statement.setString(7, record.getType());
            statement.setInt(8, record.getPoints());
            statement.setString(9, record.getIntro_cardnumber());
            statement.setString(10, record.getNote());
            statement.setString(11, record.getIntro_flag());
            statement.setString(12, record.getIntro_pointsType()); //积分计算方式
            statement.setString(13, record.getIntro_name()); //转介绍人姓名

            statement.setString(14, record.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - updateNewRecord");
        }
        return false;
    }

    //删
    public static boolean deleteRecord(Record record) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "DELETE FROM RECORD WHERE  id = ? ");

            statement.setString(1, record.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - deleteRecord");
        }
        return false;
    }


    /**
     * 积分管理按钮 辅助查询 转介绍积分是否已经兑换
     * @param id
     * @return 若已经消费了 返回true，否则返回false
     */
    public static boolean check(String id) throws SQLException {

        PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                "SELECT * FROM RECORD WHERE id=?"
        );
        statement.setString(1, id);
        ResultSet rs = statement.executeQuery();
        while (rs.next()){
            String note = rs.getString("note");
            if (note.equals("已兑换")){
                return true;
            }else {
                return false;
            }
        }
        return true;
    }

}
