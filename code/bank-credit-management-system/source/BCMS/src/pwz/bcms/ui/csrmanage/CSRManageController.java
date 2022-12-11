package pwz.bcms.ui.csrmanage;

import pwz.bcms.db.CsrDataHelper;
import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.po.Csr;
import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.util.AccountValidatorUtil;
import pwz.bcms.util.AlertUtils;
import pwz.bcms.util.IdentityUtils;
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

public class CSRManageController implements Initializable {


    @FXML
    public TableView tableView;
    public TableColumn id;
    public TableColumn name;
    public TableColumn gender;
    public TableColumn card_type;
    public TableColumn card_number;
    public TableColumn phone;
    public TableColumn company;
    public TableColumn homelocation;
    public TableColumn note;
    public Button searchButton;//搜索按钮
    public TextField searchInfo;//搜索框内容

    @FXML
    public Button manageButton; //编辑按钮
    public Button deleteButton; //删除按钮
    public Button saveButton; //保存按钮
    public Button reloadButton; //重载页面按钮
    public Button newButton; //新增按钮

    //改版后，所有弹窗整合到界面右侧，此为新版右侧区域变量
    @FXML
    public Group r_group;
    public TextField r_id;
    public TextField r_name;
    public ChoiceBox r_gender;
    public TextField r_card_number;
    public TextField r_phone;
    public TextField r_company;
    public TextArea r_note;
    public TextField r_homelocation;
    public Label r_warning;

    //自定义属性
    public static Csr csr = null;
    public static CsrDataHelper csrDataHelper = null;
    ObservableList<Csr> list = FXCollections.observableArrayList();//持久化数据列表，用于TableView
    public boolean isInManage = false;  //是否处于编辑模式，true时 保存与删除按钮才可以使用
    private boolean isInNew =false;  //是否处于新建模式，ture是，可以编辑右侧区域



    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("CSRManageController被实例化  ---CSRManageController---initialize");
        saveButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
        deleteButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
        manageButton.setDisable(true);
        r_gender.setItems(FXCollections.observableArrayList("男","女")); //右侧区域，性别选择框
        r_gender.getSelectionModel().select("男");  //默认为 男
        r_warning.setTextFill(Color.RED);
        initCol();
        loadData();
        myListener();
    }

    /**
     * 动态设置TableView中的单元格
     */
    public void initCol() {
        id.setCellValueFactory(new PropertyValueFactory<>("id"));
        name.setCellValueFactory(new PropertyValueFactory<>("name"));
        gender.setCellValueFactory(new PropertyValueFactory<>("gender"));
        card_number.setCellValueFactory(new PropertyValueFactory<>("card_number"));
        phone.setCellValueFactory(new PropertyValueFactory<>("phone"));
        company.setCellValueFactory(new PropertyValueFactory<>("company"));
        homelocation.setCellValueFactory(new PropertyValueFactory<>("homelocation"));
        note.setCellValueFactory(new PropertyValueFactory<>("note"));
    }


    /**
     * 加载数据 （CSR）
     */
    public void loadData() {
        list.clear();

        DatabaseHandler handler = DatabaseHandler.getInstance();//拿到已经创建的实例引用 （最开始是在Main中的主函数里创建的）
        String qu = "SELECT * FROM CSR";
        ResultSet rs = handler.execQuery(qu);
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
                list.add(new Csr(id, name,  gender,  card_number,  phone,  company,  homelocation,  note));
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------加载Tableview客户数据过程中的loadData()方法");
        }
        tableView.setItems(list); //将list放进tableView
    }


    /**
     * 监听选择客户：选中TableView的一行，并在界面右侧【信息处理区】显示
     */
    private void myListener(){

        tableView.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                //得到选择的客户
                Csr selectedCsr = (Csr)newValue;
                r_id.setText(selectedCsr.getId());
                r_name.setText(selectedCsr.getName());
                r_gender.getSelectionModel().select(selectedCsr.getGender());
                r_card_number.setText(selectedCsr.getCard_number());
                r_phone.setText(selectedCsr.getPhone());
                r_company.setText(selectedCsr.getCompany());
                r_homelocation.setText(selectedCsr.getHomelocation());
                r_note.setText(selectedCsr.getNote());

                //不点击编辑按钮，不可编辑
                for (Node node:r_group.getChildren()
                     ) {
                    node.setDisable(true);
                }

                //每次新选中一条信息，退出编辑模式
                manageButton.setDisable(false); //选中一条记录，才可编辑
                saveButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
                deleteButton.setDisable(false);//非编辑模式下，选中某用户，可以删除用户
                newButton.setDisable(true);
            }
        });
    }


    /**
     *  新增客户:
     *  在右侧区域填写客户信息，点击新增按钮，向数据库插入一条数据
     */
    @FXML
    public void newCsr(ActionEvent event) {
        Csr newCsr = new Csr(); //新增用户
        newCsr.setName(r_name.getText());
        newCsr.setGender(r_gender.getSelectionModel().getSelectedItem().toString());
        newCsr.setCard_number(StringUtils.trimToEmpty(r_card_number.getText()));
        newCsr.setPhone(StringUtils.trimToEmpty(r_phone.getText()));
        newCsr.setCompany(r_company.getText());
        newCsr.setHomelocation(r_homelocation.getText());
        newCsr.setNote(r_note.getText());

        if (checkR_Input(newCsr)){ //格式检查合格后再进行数据库操作
            if (CsrDataHelper.insertNewCsr(newCsr)){
                //System.out.println("保存新客户信息成功");
                AlertUtils.newAlert();
                //新增客户之后刷新界面
                MainController mainController = MainWindowLoader.getMainController();
                mainController.loadCsrManageTab();
            }else {
                //System.out.println("保存新客户信息失败");
                AlertUtils.newWrongAlert();
            }
        }


    }

    /**
     * 编辑选中客户
     * 点击编辑按钮后进入编辑模式：保存修改或者删除。
     * @param event
     */
    @FXML
    public void manageCsr(ActionEvent event) {

        r_warning.setText("");
        boolean isNameEditable = true;
        //如果该用户没有积分记录，则可以修改姓名、身份证号，不然不可以修改姓名、身份证号
        PreparedStatement statement = null;
        try {
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE card_number =?");
            statement.setString(1,r_card_number.getText());
            ResultSet rs = statement.executeQuery();
            if(rs.next()){//若有记录，禁用姓名与身份证的编辑
                isNameEditable = false;
            }else {
                isNameEditable = true;
            }
        } catch (SQLException ex) {
            System.err.println(ex + "---积分管理控制器---加载查询结果");
        }

        if (isNameEditable){
            for (Node node:r_group.getChildren()
            ) {
                node.setDisable(false);
            }
        }else {
            for (Node node:r_group.getChildren()
            ) {
                node.setDisable(false);
            }
            r_name.setDisable(true);
            r_card_number.setDisable(true);
            r_warning.setTextFill(Color.RED);
            r_warning.setText("该用户有积分记录，不可更改姓名与身份证号");
        }

        newButton.setDisable(true);//进入编辑模式后，新增按钮不可用
        saveButton.setDisable(false);
        deleteButton.setDisable(true);
    }

    /**
     * 保存(更新)用户信息
     */
    @FXML
    public void saveCsr(ActionEvent event) {
        Csr newCsr = new Csr();
        newCsr.setId(r_id.getText());
        newCsr.setName(StringUtils.trimToEmpty(r_name.getText()));
        newCsr.setGender(r_gender.getSelectionModel().getSelectedItem().toString());
        newCsr.setCard_number(r_card_number.getText());
        newCsr.setPhone(r_phone.getText());
        newCsr.setCompany(r_company.getText());
        newCsr.setHomelocation(r_homelocation.getText());
        newCsr.setNote(r_note.getText());

        if (CsrDataHelper.updateCsr(newCsr)){
            //System.out.println("修改新客户信息成功");
            AlertUtils.editAlert();
            //新增客户之后刷新界面
            MainController mainController = MainWindowLoader.getMainController();
            mainController.loadCsrManageTab();

        }else {
            AlertUtils.editWrongAlert();
            //System.out.println("修改新客户信息失败");
        }
    }

    /**
     * 删除用户信息
     * @param event
     */
    @FXML
    public void deleteCsr(ActionEvent event) {
        Csr newCsr = new Csr();
        newCsr.setId(r_id.getText());

        // 判断该用户是否有积分记录
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE card_number =?");
            statement.setString(1,r_card_number.getText());
            ResultSet rs = statement.executeQuery();
            if (rs.next()){
                r_warning.setText("警告：该用户存在积分记录，不可删除");
            }else {
                if (CsrDataHelper.deleteCsr(newCsr)){
//                    r_warning.setText("删除客户信息成功");
                    AlertUtils.deleteAlert();
                    //新增客户之后刷新界面
                    MainController mainController = MainWindowLoader.getMainController();
                    mainController.loadCsrManageTab();

                }else {
                    AlertUtils.deleteWrongAlert();
//                    System.out.println("删除客户信息失败");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }


    }

    /**
     * 查询客户信息: 使用身份证查询，查询结果返回到右侧区域
     * @param event
     */
    @FXML
    public void searchCsr(ActionEvent event) {

        for (Node node:r_group.getChildren()
        ) {
            node.setDisable(false);
        }
        r_id.setText("");
        r_name.setText("");
        r_card_number.setText("");
        r_phone.setText("");
        r_company.setText("");
        r_homelocation.setText("");
        r_note.setText("");

        r_warning.setTextFill(Color.RED);
        r_warning.setText("");
        if (IdentityUtils.isLegalIDNumber(StringUtils.trimToEmpty(searchInfo.getText()))){
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT * FROM CSR WHERE card_number =?");
                statement.setString(1,searchInfo.getText());
                //System.out.println("使用身份证号：" + searchInfo.getText() + "进行查询   - - - searchCsr");
                ResultSet rs = statement.executeQuery();
                while (rs.next()){ //身份证唯一，此处只会返回一条结果
                    System.out.println(rs.getString("name"));
                    String id = rs.getString("id");
                    String name = rs.getString("name");
                    String gender = rs.getString("gender");
                    String card_number = rs.getString("card_number");
                    String phone = rs.getString("phone");
                    String company = rs.getString("company");
                    String homelocation = rs.getString("homelocation");
                    String note = rs.getString("note");
                    Csr selectedCsr = new Csr(id, name,  gender,  card_number,  phone,  company,  homelocation,  note);

                    r_id.setText(selectedCsr.getId());
                    r_name.setText(selectedCsr.getName());
                    //r_gender.setText(selectedCsr.getGender());
                    r_card_number.setText(selectedCsr.getCard_number());
                    r_phone.setText(selectedCsr.getPhone());
                    r_company.setText(selectedCsr.getCompany());
                    r_homelocation.setText(selectedCsr.getHomelocation());
                    r_note.setText(selectedCsr.getNote());

                    //不点击编辑按钮，不可编辑
                    for (Node node:r_group.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    r_warning.setTextFill(Color.GREEN);
                    r_warning.setText("查询成功");
                    manageButton.setDisable(false);
                    newButton.setDisable(true);
                }
                if (!r_name.isDisable())r_warning.setText("警告：未查询到指定客户");
            } catch (SQLException ex) {
                System.err.println(ex.getMessage() + " - - - searchCsr");
            }
        }else {
            r_warning.setText("警告：身份证号格式不正确");
        }


    }

    @FXML
    public void reloadPage(ActionEvent event) {
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadCsrManageTab();
    }

    /**
     * 右侧区域输入检查
     * 待检查内容： 身份证号、手机号是否符合标准，姓名、性别是否不为空
     */
    private boolean checkR_Input(Csr newCsr) {

        //姓名
        if (!AccountValidatorUtil.isUsername(newCsr.getName())) {
            r_warning.setText("警告：姓名格式不合格");
            return false;
        }

        //性别
        if (newCsr.getGender() == ""){
            r_warning.setText("警告：未选择性别");
            return false;
        }

        //身份证号
        if (!IdentityUtils.isLegalIDNumber(newCsr.getCard_number())){
            r_warning.setText("警告：身份证号格式错误");
            return false;
        }else{
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT * FROM CSR WHERE card_number =?");
                statement.setString(1,r_card_number.getText());
                ResultSet rs = statement.executeQuery();
                if (rs.next()){
                    r_warning.setText("警告：该身份证已有记录");
                    return false;
                }
                } catch (SQLException e) {
                    e.printStackTrace();
            }
        }

        //手机号
        if (!IdentityUtils.isLegalPhoneNumber(newCsr.getPhone())){
            r_warning.setText("警告：手机号格式不正确");
            return false;
        }else {
            return true;
        }

    }//checkR_Input

}//main
