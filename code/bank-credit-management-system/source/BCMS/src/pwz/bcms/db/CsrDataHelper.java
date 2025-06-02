package pwz.bcms.db;

import pwz.bcms.po.Csr;

import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CsrDataHelper {

    //增
    public static boolean insertNewCsr(Csr csr) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "INSERT INTO CSR(name,gender,card_number,phone,company,homelocation,note) VALUES(?,?,?,?,?,?,?)");
            statement.setString(1, csr.getName());
            statement.setString(2, csr.getGender());
            statement.setString(3, csr.getCard_number());
            statement.setString(4, csr.getPhone());
            statement.setString(5, csr.getCompany());
            statement.setString(6, csr.getHomelocation());
            statement.setString(7, csr.getNote());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - insertCSR");
        }
        return false;
    }

    //改
    public static boolean updateCsr(Csr csr) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "UPDATE CSR SET name=?,gender=?,card_number=?,phone=?,company=?,homelocation=?,note=? WHERE id = ?");
            statement.setString(1, csr.getName());
            statement.setString(2, csr.getGender());
            statement.setString(3, csr.getCard_number());
            statement.setString(4, csr.getPhone());
            statement.setString(5, csr.getCompany());
            statement.setString(6, csr.getHomelocation());
            statement.setString(7, csr.getNote());
            statement.setString(8, csr.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - updateCsr");
        }
        return false;
    }

    //删
    public static boolean deleteCsr(Csr csr) {
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "DELETE FROM CSR WHERE id =?");
            statement.setString(1,csr.getId());

            return statement.executeUpdate() > 0;
        } catch (SQLException ex) {
//            LOGGER.log(Level.ERROR, "{}", ex);
            System.err.println(ex.getMessage() + " - - - deleteCsr");
        }
        return false;
    }

}
