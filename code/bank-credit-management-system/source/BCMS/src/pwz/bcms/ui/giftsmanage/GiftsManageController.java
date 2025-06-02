package pwz.bcms.ui.giftsmanage;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.db.GiftDataHelper;
import pwz.bcms.po.Gift;
import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.util.AccountValidatorUtil;
import pwz.bcms.util.AlertUtils;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.paint.Color;
import org.apache.commons.lang3.StringUtils;

import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class GiftsManageController implements Initializable {

    @FXML
    public TableView tableView;
    public TableColumn id;
    public TableColumn name;
    public TableColumn type;
    public TableColumn value;
    public TableColumn flag;
    public TableColumn note;
    public Button searchButton;
    public TextField searchInfo;
    public Button manageButton;
    public Button newButton;

    @FXML
    public Group r_group;
    public TextField r_id;
    public TextField r_name;
    public TextField r_type;
    public TextField r_value;
    public ChoiceBox r_flag;
    public TextArea r_note;
    public Label r_warning;

    @FXML
    public Button saveButton;
    public Button deleteButton;
    public Button reloadButton;


    //自定义属性
    public static Gift gift = null;
    public static GiftDataHelper giftDataHelper = null;
    ObservableList<Gift> list = FXCollections.observableArrayList();//持久化数据列表


    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("---实例化---giftsManageController---initialize");

        r_warning.setTextFill(Color.RED);
        r_flag.getItems().addAll("是","否");
        r_flag.getSelectionModel().select("否");

        manageButton.setDisable(true);
        saveButton.setDisable(true);
        deleteButton.setDisable(true);

        initCol();
        loadData();
        myListener();
    }

    //动态设置TableView中的单元格
    public void initCol() {
        id.setCellValueFactory(new PropertyValueFactory<>("id"));
        name.setCellValueFactory(new PropertyValueFactory<>("name"));
        type.setCellValueFactory(new PropertyValueFactory<>("type"));
        value.setCellValueFactory(new PropertyValueFactory<>("value"));
        flag.setCellValueFactory(new PropertyValueFactory<>("flag"));
        note.setCellValueFactory(new PropertyValueFactory<>("note"));
    }


    //加载数据 （Gift）
    public void loadData() {
        list.clear();

        DatabaseHandler handler = DatabaseHandler.getInstance();//拿到已经创建的实例引用 （最开始是在Main中的主函数里创建的）
        String qu = "SELECT * FROM GIFT";
        ResultSet rs = handler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                String type = rs.getString("type");
                String value = rs.getString("value");
                String flag = rs.getString("flag");
                String note = rs.getString("note");
                list.add(new Gift(id, name,  type,  value,  flag, note));
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------加载Tableview客户数据过程中的loadData()方法");
        }
        tableView.setItems(list);
    }

    private void myListener(){
        tableView.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                //得到选择的客户
                Gift selectedGift = (Gift) newValue;
                r_id.setText(selectedGift.getId());
                r_name.setText(selectedGift.getName());
                r_type.setText(selectedGift.getType());
                r_value.setText(selectedGift.getValue());
                r_flag.getSelectionModel().select(selectedGift.getFlag());
                r_note.setText(selectedGift.getNote());

                //不点击编辑按钮，不可编辑
                for (Node node:r_group.getChildren()
                ) {
                    node.setDisable(true);
                }

                //每次新选中一条信息，退出编辑模式
                manageButton.setDisable(false);
                saveButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
                deleteButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
                if (r_flag.getSelectionModel().getSelectedItem().equals("是")){
                    manageButton.setDisable(true);
                    r_warning.setText("过期礼品不可修改或删除");
                }
            }
        });
    }

    //新增礼品信息
    @FXML
    public void newGift(ActionEvent event){

        r_warning.setText("");

        Gift newGift = new Gift();
        newGift.setName(r_name.getText());
        newGift.setType(r_type.getText());
        newGift.setValue(r_value.getText());
        newGift.setFlag(r_flag.getSelectionModel().getSelectedItem().toString());
        newGift.setNote(r_note.getText());

        if (checkInput(newGift)){
            if (GiftDataHelper.insertNewGift(newGift)){
                //System.out.println("保存新礼品信息成功");
                AlertUtils.newAlert();
                //新增礼品之后刷新界面
                MainController mainController = MainWindowLoader.getMainController();
                mainController.loadGiftsManageTab();
            }else {
//                r_warning.setText("警告：该礼品已在数据库中");
                //System.out.println("保存新礼品信息失败");
                AlertUtils.newWrongAlert();
            }
        }

    }

    //进入编辑模式
    @FXML
    public void manageGift(ActionEvent event) {

        //不点击编辑按钮，不可编辑
        for (Node node:r_group.getChildren()
        ) {
            node.setDisable(false);
        }

        newButton.setDisable(true);
        saveButton.setDisable(false);
        deleteButton.setDisable(false);
    }

    public void saveGift(ActionEvent event) {
        Gift newGift = new Gift();
        newGift.setId(r_id.getText());
        newGift.setName(r_name.getText());
        newGift.setType(r_type.getText());
        newGift.setValue(r_value.getText());
        newGift.setFlag(r_flag.getSelectionModel().getSelectedItem().toString());
        newGift.setNote(r_note.getText());

        if (checkInput(newGift)){
            if (GiftDataHelper.updateGift(newGift)){

                AlertUtils.editAlert();

                //新增客户之后刷新界面
                MainController mainController = MainWindowLoader.getMainController();
                mainController.loadGiftsManageTab();
//                r_warning.setTextFill(Color.GREEN);
//                r_warning.setText("修改礼品信息成功");
            }else {
                //r_warning.setTextFill(Color.RED);
//                r_warning.setText("修改礼品信息失败");
                AlertUtils.editWrongAlert();
            }
        }

    }

    public void deleteGift(ActionEvent event) {
        Gift newGift = new Gift();
        newGift.setId(r_id.getText());
        if (GiftDataHelper.deleteGift(newGift)){
//            System.out.println("删除礼品信息成功");
            AlertUtils.deleteAlert();
            //新增客户之后刷新界面
            MainController mainController = MainWindowLoader.getMainController();
            mainController.loadGiftsManageTab();
        }else {
            AlertUtils.deleteWrongAlert();
//            System.out.println("删除礼品信息失败");
        }
    }


    //查询礼品信息
    @FXML
    public void searchGift(ActionEvent event) {
        //每次查询到一条信息，退出编辑模式
        manageButton.setDisable(false);
        newButton.setDisable(true);
        saveButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
        deleteButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
        r_id.setText("");
        r_name.setText("");
        r_type.setText("");
        r_value.setText("");
        r_note.setText("");
        for (Node node:r_group.getChildren()
        ) {
            node.setDisable(false);
        }
        r_warning.setTextFill(Color.RED);
        r_warning.setText("");
        if (AccountValidatorUtil.isUsername(StringUtils.trimToEmpty(searchInfo.getText()))){
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT * FROM GIFT WHERE name = ?");
                statement.setString(1,searchInfo.getText());
                ResultSet rs = statement.executeQuery();
                while (rs.next()){
                    String id = rs.getString("id");
                    String name = rs.getString("name");
                    String type = rs.getString("type");
                    String value = rs.getString("value");
                    String flag = rs.getString("flag");
                    String note = rs.getString("note");
                    Gift selectedGift = new Gift(id, name,  type,  value,  flag, note);

                    r_id.setText(selectedGift.getId());
                    r_name.setText(selectedGift.getName());
                    r_type.setText(selectedGift.getType());
                    r_value.setText(selectedGift.getValue());
                    r_flag.getSelectionModel().select(selectedGift.getFlag());
                    r_note.setText(selectedGift.getNote());

                    //不点击编辑按钮，不可编辑
                    for (Node node:r_group.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    r_warning.setTextFill(Color.GREEN);
                    r_warning.setText("查询成功");
                    manageButton.setDisable(false);

                }//while
            } catch (SQLException ex) {
                System.err.println(ex.getMessage() + " - - - searchGift");
            }
            if (!r_name.isDisable()){
                r_warning.setText("未查询到指定礼品");
            }
        }else {
            r_warning.setText("警告：搜索关键字有误");
        }

    }


    /**
     * 输入信息检查
     * @param newGift
     * @return
     */
    private boolean checkInput(Gift newGift){

        r_warning.setTextFill(Color.RED);

        //礼品名称
        if (!AccountValidatorUtil.isUsername(newGift.getName())){
            r_warning.setText("警告：礼品名称有误");
            return false;
        }

        //礼品型号
        if (!AccountValidatorUtil.isUsername(newGift.getName())){
            r_warning.setText("警告：礼品型号有误");
            return false;
        }

        //采购价格
        if (!AccountValidatorUtil.isNumber(newGift.getValue())) {
            r_warning.setText("警告：礼品采购价格格式有误");
            return false;
        }else {
            return true;
        }

    }

    @FXML
    public void reloadPage(ActionEvent event) {
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadGiftsManageTab();
    }
}
