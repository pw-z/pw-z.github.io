package pwz.bcms.ui.pointsmanage;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.util.AccountValidatorUtil;
import pwz.bcms.util.AlertUtils;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Date;
import java.util.ResourceBundle;

public class ExchangeGiftController implements Initializable {

    @FXML
    public ChoiceBox giftList;
    public TextField giftNumber;
    public Button saveButton;
    public Label warning;

    ObservableList<String> giftName = FXCollections.observableArrayList();  //礼品选择框里的内容

    @Override
    public void initialize(URL location, ResourceBundle resources) {

        //加载礼品下拉列表
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT name FROM GIFT");
            //statement.setString(1,card_number.getText());
            ResultSet rs = statement.executeQuery();
            while (rs.next()){
                giftName.add(rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        giftList.setItems(giftName);
        giftList.getSelectionModel().select(0); //默认选中第一个  避免空选错误
    }


    /**
     * 保存礼品兑换记录
     * 此处直接操作数据库了，没有经过po与dbhandler两个模块
     * @version 2020年3月7日
     * @param event
     */
    public void saveGiftRecord(ActionEvent event) {

        if (checkInput()){
            Date now = new Date();
            java.sql.Date sqlDate = new java.sql.Date(now.getTime());
            //增
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "INSERT INTO GIFTRECORD(name,date,number) VALUES(?,?,?)");
                statement.setString(1, giftList.getSelectionModel().getSelectedItem().toString());
                statement.setDate(2, sqlDate);
                statement.setInt(3, Integer.parseInt(giftNumber.getText()));

                statement.execute();

                AlertUtils.saveGiftRecordAlert();
                ((Stage)saveButton.getScene().getWindow()).close();

            } catch (SQLException ex) {
                System.err.println(ex.getMessage() + " - - - saveGiftRecord");
            }
        }else {
            warning.setText("请输入数量");
        }
    }


    /**
     * 检查输入状态
     * @return 没问题就返回true
     */
    private boolean checkInput(){
        //判断是否输入数字
        if (!AccountValidatorUtil.isNumber(giftNumber.getText())){
            return false;
        }else {
            return true;
        }
    }


}
