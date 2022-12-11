package pwz.bcms.ui.pointsmanage;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.db.RecordDataHelper;
import pwz.bcms.po.Record;
import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.util.AlertUtils;
import pwz.bcms.util.IdentityUtils;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.stage.Modality;
import javafx.stage.Stage;
import org.apache.commons.lang3.StringUtils;

import java.io.IOException;
import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Date;
import java.util.ResourceBundle;

public class PointsManageController implements Initializable {

    @FXML
    public TableView tableView;
    public TableColumn id;
    public TableColumn csr_name;
    public TableColumn card_number;
    public TableColumn account;
    public TableColumn product_name;
    public TableColumn product_points;
    public TableColumn value;
    public TableColumn date;
    public TableColumn type;
    public TableColumn points;
    public TableColumn intro_cardnumber;  //介绍人身份证号
    public TableColumn note; //兑换标识：已兑换、未兑换
    public TableColumn intro_flag; //转介绍标识： 是、否
//    public TableColumn<Record,Boolean> useFlag;  //是否兑换此纪录的积分 (非查询结果状态下不可选)
    public TableColumn<Record,CheckBox> useFlag;  //是否兑换此纪录的积分 (非查询结果状态下不可选)
    public Label totalPoints;  //所选的积分总数
    public ChoiceBox note_flag;  //搜索条件：已兑换、未兑换
    public Button searchButton; //搜索按钮
    public TextField searchInfo;  //搜索关键字   使用身份证号进行搜索
    public Button newButton;  //新建记录按钮
    public Button manageButton;  //管理记录按钮
    public Label warning; //底部信息提示标签
    public Button reloadButton;
    public Button exchangeButton; //兑换按钮


    //自定义属性
    ObservableList<Record> list = FXCollections.observableArrayList();//持久化数据列表

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        note_flag.setItems(FXCollections.observableArrayList("已兑换","未兑换"));
        note_flag.getSelectionModel().select("未兑换");
        exchangeButton.setDisable(true);
        //tableView.setTableMenuButtonVisible(true);

        //tableview样式
        tableView.setColumnResizePolicy(TableView.UNCONSTRAINED_RESIZE_POLICY);

        initCol();
        loadData();
    }

    //动态设置TableView中的单元格
    public void initCol() {
        id.setCellValueFactory(new PropertyValueFactory<>("id"));
        csr_name.setCellValueFactory(new PropertyValueFactory<>("csr_name"));
        card_number.setCellValueFactory(new PropertyValueFactory<>("card_number"));
        account.setCellValueFactory(new PropertyValueFactory<>("account"));
        product_name.setCellValueFactory(new PropertyValueFactory<>("product_name"));
        product_points.setCellValueFactory(new PropertyValueFactory<>("product_points")); //暂时不在界面显示产品的单位产品积分数
        value.setCellValueFactory(new PropertyValueFactory<>("value"));
        date.setCellValueFactory(new PropertyValueFactory<>("date"));
        type.setCellValueFactory(new PropertyValueFactory<>("type"));
        points.setCellValueFactory(new PropertyValueFactory<>("points"));
        intro_cardnumber.setCellValueFactory(new PropertyValueFactory<>("intro_cardnumber"));
        note.setCellValueFactory(new PropertyValueFactory<>("note"));
        intro_flag.setCellValueFactory(new PropertyValueFactory<>("intro_flag"));
        useFlag.setCellValueFactory(cellData ->cellData.getValue().cb.getCheckBox());//调用封装了的checkbox的getCheckBox()方法，这里会返回一个ObservableValue<CheckBox>类型的checkbox
//        useFlag.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Record, CheckBox>, ObservableValue<CheckBox>>() {
//            @Override
//            public ObservableValue<CheckBox> call(TableColumn.CellDataFeatures<Record, CheckBox> param) {
//                System.out.println("进入setCellValueFactory");
//                checkbox cb = param.getValue().cb;
//                return cb.getCheckBox();
//            }
//        });

//        useFlag.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Record,Boolean>, ObservableValue<Boolean>>() {
//            @Override
//            public ObservableValue<Boolean> call(TableColumn.CellDataFeatures<Record, Boolean> param) {
//                // TODO Auto-generated method stub
//                return param.getValue().cbbooleanProperty();
//            }
//        });
        tableView.setEditable(true);
//        useFlag.setCellFactory(CheckBoxTableCell.forTableColumn(useFlag));
        useFlag.setVisible(false);

    }

    //加载数据 （Record）
    public void loadData() {
        list.clear();

        DatabaseHandler handler = DatabaseHandler.getInstance();//拿到已经创建的实例引用 （最开始是在Main中的主函数里创建的）
        String qu = "SELECT * FROM RECORD WHERE note = '未兑换' "; //只显示未对换的记录
        ResultSet rs = handler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                String account = rs.getString("account");
                String product_name = rs.getString("product_name");
                Integer product_points = rs.getInt("product_points");
                String value = rs.getString("value");
                Date date = rs.getDate("date");
                String type = rs.getString("type");
                Integer points = rs.getInt("points");
                String intro_cardnumber = rs.getString("intro_cardnumber");
                String note = rs.getString("note");
                String intro_flag = rs.getString("intro_flag");
                String intro_pointsType = rs.getString("intro_pointsType");
                String intro_name = rs.getString("intro_name");
                list.add(new Record( id,  csr_name,  card_number,  account,  product_name,product_points,  value,  date,  type,  points,  intro_cardnumber,  note,intro_flag,intro_pointsType,intro_name));
            }
        } catch (SQLException ex) {
            System.err.println(ex + "---积分管理控制器---加载Tableview客户数据过程中的loadData()方法");
        }
        tableView.setItems(list);
        //useFlag.setVisible(false);
    }


    /**
     * 新建记录
     * @param event
     */
    @FXML
    public void newRecord(ActionEvent event) {
        warning.setText("");
        try {
            Parent root = FXMLLoader.load(getClass().getResource("newRecord.fxml"));
            Scene scene = new Scene(root);
            scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");
            Stage stage = new Stage();
            stage.setScene(scene);
            stage.setResizable(false); //窗口大小固定，不可伸缩
            //确定标题
            if (((Stage)newButton.getScene().getWindow()).getTitle().equals("XXX银行积分管理系统 (未注册)")){
                stage.setTitle("新建记录（未注册）");
            }else {
                stage.setTitle("新建记录");
            }
            stage.initModality(Modality.APPLICATION_MODAL);//设置为模态窗口
            stage.show();
        }catch (Exception ex){
            System.err.println(ex + "----newRecordButton--新窗口 出错");
        }
    }


    /**
     * 管理记录
     * @param event
     */
    @FXML
    public void manageRecord(ActionEvent event) throws SQLException {

        warning.setText("");
        boolean isManageable = false; //是否可管理

        //在选中模式下选中TableView的一行
        Record selectedRecord = (Record) tableView.getSelectionModel().getSelectedItem();

        if (selectedRecord!=null){
            /**
             * 非转介绍积分&&未兑换积分&&（如果有）对应转介绍人的积分未消费   才可以修改
             */
            if (!(selectedRecord.getIntro_flag()).equals("否")){
                warning.setTextFill(Color.RED);
                warning.setText("转介绍积分记录主动不可修改");
            }else if (!(selectedRecord.getNote()).equals("未兑换")){
                warning.setTextFill(Color.RED);
                warning.setText("已兑换的积分记录不可修改");
            }else if (!selectedRecord.getIntro_cardnumber().isEmpty()){
                //判断对应转介绍人的积分消费与否
                if (RecordDataHelper.check(String.valueOf(Integer.valueOf(selectedRecord.getId())+1))){
                    warning.setTextFill(Color.RED);
                    warning.setText("对应转介绍人的积分已经消费，本条记录不能修改");
                }else{
                    isManageable=true;
                }
            }else {
                isManageable=true;
            }

            if (isManageable){
                try {
                    FXMLLoader fxmlLoader = new FXMLLoader();
                    fxmlLoader.setLocation(getClass().getResource("manageRecord.fxml"));
                    Parent root = fxmlLoader.load();
                    Scene scene = new Scene(root);
                    scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");
                    Stage stage = new Stage();
                    stage.setScene(scene);
                    stage.setResizable(false);
                    stage.initModality(Modality.APPLICATION_MODAL);//设置为模态窗口
                    stage.show();

                    //在manageRecord.fxml页面中显示
                    ManageRecord manageRecord = fxmlLoader.getController();
                    manageRecord.recordID.setText(selectedRecord.getId());
                    //第一组数据
                    manageRecord.card_number.setText(selectedRecord.getCard_number());
                    manageRecord.csr_name.setText(selectedRecord.getCsr_name());
                    manageRecord.account.setText(selectedRecord.getAccount());
                    //第二组数据
                    manageRecord.product_name.setText(selectedRecord.getProduct_name());
                    manageRecord.product_points.setText(selectedRecord.getProduct_points().toString());
                    manageRecord.value.setText(selectedRecord.getValue());
                    manageRecord.type.setText(selectedRecord.getType());
                    manageRecord.points.setText(selectedRecord.getPoints().toString());
                    //第三组数据
                    if (selectedRecord.getIntro_cardnumber().isEmpty()){
                        manageRecord.is_intro_exist.setText("否");
                    }else{
                        manageRecord.is_intro_exist.setText("是");
                        manageRecord.intro_pointsType.setText(selectedRecord.getIntro_pointsType());
                        manageRecord.intro_cardnumber.setText(selectedRecord.getIntro_cardnumber());
                    }
                    manageRecord.intro_name.setText(selectedRecord.getIntro_name());

                }catch (Exception ex){
                    System.err.println(ex + "----manageRecordButton--新窗口 出错");
                }
            }
        }else {
            warning.setTextFill(Color.RED);
            warning.setText("未选择记录");
        }




    }//manageRecord



    /**
     * 搜索客户 （兑换积分）
     * @param event
     * @throws IOException
     */
    Integer sumPoints;
    @FXML
    public void searchCsr(ActionEvent event) throws IOException {
        warning.setText("");
        //验证身份证格式
        if (!IdentityUtils.isLegalIDNumber(StringUtils.trimToEmpty(searchInfo.getText()))){
            warning.setTextFill(Color.RED);
            warning.setText("请输入正确的身份证格式进行搜索");
        }else {
            loadSearchRs();
            checkboxListener();
        }
    }

    //加载查询结果 （Record）
    public void loadSearchRs() {
        list.clear();
        sumPoints = 0;
        PreparedStatement statement = null;

        try {
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE card_number =? AND note=?");
            statement.setString(1,searchInfo.getText());
            statement.setString(2,note_flag.getSelectionModel().getSelectedItem().toString());
            ResultSet rs = statement.executeQuery();
            int count = 0;//查询到的记录数量
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                String account = rs.getString("account");
                String product_name = rs.getString("product_name");
                Integer product_points = rs.getInt("product_points");
                String value = rs.getString("value");
                Date date = rs.getDate("date");
                String type = rs.getString("type");
                Integer points = rs.getInt("points");
                String intro_name = rs.getString("intro_name");
                String intro_cardnumber = rs.getString("intro_cardnumber");
                String note = rs.getString("note");
                String intro_flag = rs.getString("intro_flag");
                list.add(new Record( id,  csr_name,  card_number,  account,  product_name,product_points,  value,  date,  type,  points,  intro_cardnumber,  note,intro_flag));
                count++;
            }
            if (count>0){
                AlertUtils.searchAlert();
            }else {
                AlertUtils.searchWrongAlert();
            }
        } catch (SQLException ex) {
            System.err.println(ex + "---积分管理控制器---加载查询结果");
        }
        if (note_flag.getSelectionModel().getSelectedItem().equals("未兑换")){
            useFlag.setVisible(true);
        }else {
            useFlag.setVisible(false);
        }
        //tableView.setItems(list);  //tableView会自动根据list的改变而更新内容，不必再次setItems();

        //查询结果页面 禁用新增与管理按钮  只允许刷新、兑换
        manageButton.setDisable(true);
        newButton.setDisable(true);

    }



    @FXML
    public void reloadTab(ActionEvent event) {
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadPointsManageTab();
    }

    /**
     * 兑换按钮
     * 点击后，便利TableView列表，将所有被勾选的积分记录更新为已兑换
     * @param event
     */
    public void handleExchangeButton(ActionEvent event) throws IOException {
        PreparedStatement statement = null;
        ObservableList<Record> list=tableView.getItems();
        for (Record o:list) {
            if (o.cb.isSelected()){
                try {
                    statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                            "UPDATE RECORD SET note=? WHERE id=?");
                    statement.setString(1,"已兑换");
                    statement.setString(2,o.getId());

                    statement.execute();

                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

        //弹窗登记礼品
        FXMLLoader fxmlLoader = new FXMLLoader();
        fxmlLoader.setLocation(getClass().getResource("exchangeGift.fxml"));
        Parent root = fxmlLoader.load();
        Scene scene = new Scene(root);
        scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");
        Stage stage = new Stage();
        stage.setScene(scene);
        stage.setResizable(false);
        stage.initModality(Modality.APPLICATION_MODAL);//设置为模态窗口
        stage.show();

        //刷新页面
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadPointsManageTab();
    }


    /**
     * 监听checkbox状态，计算所有选中记录的总积分数量
     * TODO: 此处有一个小BUG，因为监听的是鼠标移动，如果单击选框后不移动，则选中积分数不变   此问题待处理
     */
    Integer totalPointsInt = 0;
    private void checkboxListener(){

        tableView.setOnMouseMoved(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                totalPoints.setText("0");
                totalPointsInt = 0;
                ObservableList<Record> list=tableView.getItems();
                for (Record o:list
                ) {
                    if (o.cb.isSelected()){
                        totalPointsInt += Integer.valueOf(o.getPoints());
                        totalPoints.setText(totalPointsInt.toString());
                    }
//                    if (o.cb.isSelected()){
//                        totalPointsInt += Integer.valueOf(o.getPoints());
//                        totalPoints.setText(totalPointsInt.toString());
//                    }
                }
                if (!totalPoints.getText().equals("0"))exchangeButton.setDisable(false);
            }
        });



    }//checkboxListener






}


