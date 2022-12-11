package pwz.bcms.db;

import java.sql.ResultSet;
import java.sql.SQLException;

public class SQLTest {
    private static DatabaseHandler databaseHandler = DatabaseHandler.getInstance();
    public static void main(String[] args) {


        queryRecord();

    }

    private static void update(){
        String qu1 = "INSERT INTO CSR(name,gender,card_number,phone,company,homelocation,note) VALUES(?,?,?,?,?,?,?)";
        String qu = "UPDATE CSR SET name='西门吹风' WHERE id = 101";
        databaseHandler.execAction(qu);
    }



    private static void query(){
        String qu = "SELECT * FROM CSR";
        ResultSet rs = databaseHandler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                String gender = rs.getString("gender");
                String card_number = rs.getString("card_number");
                String phone = rs.getString("phone");
                String company = rs.getString("company");
                String homelocation = rs.getString("homelocation");
                String note = rs.getString("note");

                System.out.println(id + name + gender + card_number + phone + company + homelocation + note);
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------");
        }
    }

    private static void queryProduct(){
        String qu = "SELECT * FROM Product";
        ResultSet rs = databaseHandler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                String points = rs.getString("points");
                String tlimit = rs.getString("tlimit");
                String flag = rs.getString("flag");
                String note = rs.getString("note");

                System.out.println(id + name + points + tlimit + flag + note);
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------");
        }
    }

    private static void queryRecord(){
        String qu = "SELECT * FROM RECORD";
        ResultSet rs = databaseHandler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String note = rs.getString("note");
                String intro_flag = rs.getString("intro_flag");

                System.out.println(id + csr_name   + note + intro_flag);
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------");
        }
    }
}
