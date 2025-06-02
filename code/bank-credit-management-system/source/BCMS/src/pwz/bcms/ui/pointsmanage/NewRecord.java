package pwz.bcms.ui.pointsmanage;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.db.RecordDataHelper;
import pwz.bcms.po.Record;

import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.util.AccountValidatorUtil;
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
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import org.apache.commons.lang3.StringUtils;

import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Date;
import java.util.ResourceBundle;

public class NewRecord implements Initializable {

    public static final String INTRO_POINTS_PER_RECORD = "20"; //固定积分制，每笔交易转介绍人获得的积分数

    @FXML
    public TextField card_number;  //身份证号  以此定位客户
    public Button searchCsrButton;  //用身份证号搜索客户
    public TextField csr_name;  //搜索到客户后，将名字返回
    public TextField account;  //客户的账号
    public Label accountLabel;

    @FXML
    public ComboBox product_name;  //产品名称 （下拉选框，选择此次交易涉及到的积分产品）
    public TextField product_points; //单位产品积分数
    public TextField value;  //此次交易的金额
    public ChoiceBox type;  //交易类型 电子、线下
    public TextField points;  //此次交易获得的积分数量
    public ChoiceBox is_intro_exist;


    @FXML
    public TextField intro_cardnumber;  //介绍人的身份证号  以此定位介绍人
    public TextField intro_name;  //介绍人姓名  搜索到介绍人后后，将名字返回
    public Button searchIntroButton;  //搜索介绍人 （使用身份证号搜索）
    public Button saveButton;  //保存按钮  （保存此次记录）
    public TextField intro_getpoints; //转介绍人将获得积分
    public ChoiceBox intro_pointsType; //转介绍人获得的积分 的计算方式 ：固定积分制、按金额记
    public TextField intro_flag; //转介绍积分标识
    public TextField note;  //备注信息（是否已兑换）

    @FXML
    public Group input_group1; //首先定位客户
    public Group input_group2;  //其次订单产品信息
    public Group input_group3; //最后选填转介绍信息
    public Label warning;  //底部提示信息
    public ComboBox intro_product_name; //转介绍版本产品
    public TextField intro_product_points; //转介绍版本产品


    //自定义属性
    Record newRecord = new Record();
    ObservableList<String> productsName = FXCollections.observableArrayList();  //积分产品选择框里的内容(产品名称)
    ObservableList<String> introProductsName = FXCollections.observableArrayList();  //积分产品选择框里的内容(产品名称)


    @Override
    public void initialize(URL location, ResourceBundle resources) {

        type.getItems().addAll("电子","线下");
        type.getSelectionModel().select("电子");
        intro_pointsType.getItems().addAll("固定积分制","按金额记(与客户相同)");
        intro_pointsType.getSelectionModel().select("固定积分制");
        is_intro_exist.getItems().addAll("是","否");
        is_intro_exist.getSelectionModel().select("否");

        //加载非转介绍积分产品下拉列表
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT name FROM PRODUCT WHERE flag = '否'"); //只加载非转介绍版本产品
            //statement.setString(1,card_number.getText());
            ResultSet rs = statement.executeQuery();
            while (rs.next()){
                productsName.add(rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        product_name.setItems(productsName);

        //加载转介绍积分产品下拉列表
        try {
            PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT name FROM PRODUCT WHERE flag = '是'"); //只加载非转介绍版本产品
            //statement.setString(1,card_number.getText());
            ResultSet rs = statement.executeQuery();
            while (rs.next()){
                introProductsName.add(rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        intro_product_name.setItems(introProductsName);

        //初始状态： 未定位客户，则input_group2、input_group3、account均不可编辑
        for (Node node:input_group2.getChildren()
        ) {
            node.setDisable(true);
        }
        for (Node node:input_group3.getChildren()
        ) {
            node.setDisable(true);
        }
        accountLabel.setDisable(true);
        account.setDisable(true);
        saveButton.setDisable(true);

        //开启监听器 （监听积分产品选择）
        contentListener();
    }

    /**
     * 定位客户,成功定位到指定客户后，方可以输入账户信息
     * @param event
     */
    @FXML
    public void searchCsr(ActionEvent event) {

        if (IdentityUtils.isLegalIDNumber(StringUtils.trimToEmpty(card_number.getText()))){ //检测身份证号格式
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT name FROM CSR WHERE card_number =?");
                statement.setString(1,card_number.getText());
                ResultSet rs = statement.executeQuery();
                while (rs.next()){
                    csr_name.setText(rs.getString("name"));
                }
                //定位客户成功后，account可以编辑
                if (!csr_name.getText().isEmpty()){
                    warning.setTextFill(Color.GREEN);
                    warning.setText("定位客户成功");
                    accountLabel.setDisable(false);
                    account.setDisable(false);
                }else {
                    warning.setTextFill(Color.RED);
                    warning.setText("未查询到指定客户");

                    //account恢复到不可编辑模式
                    accountLabel.setDisable(true);
                    account.setDisable(true);
                    account.setText("");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }else {
            //定位失败则account恢复到不可编辑模式
            accountLabel.setDisable(true);
            account.setDisable(true);
            account.setText("");

            warning.setTextFill(Color.RED);
            warning.setText("警告：身份证格式有误");
        }


    }


    /***************************************************************************************************
     * 输入监听，实时反馈
     */
    Integer pointsInteger;
    public void contentListener(){

        /**
         * 实时判断账号格式是否正确
         */
        account.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                if (!IdentityUtils.isLegalAccount(newValue)){
                    warning.setTextFill(Color.RED);
                    warning.setText("账号格式有误");
                    for (Node node:input_group2.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    for (Node node:input_group3.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                }else {
                    warning.setTextFill(Color.GREEN);
                    warning.setText("账号格式正确");

                    //账号格式正确之后，第二组输入区才可以编辑
                    for (Node node:input_group2.getChildren()
                    ) {
                        node.setDisable(false);
                    }

                }
            }
        });


        /**
         * 实时更新 对应产品的单位产品积分数
         * 判断是否符合激活保存按钮的条件
         */
        product_name.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {

                //清除提示信息
                warning.setText("");


                //获取所选产品的单位产品积分数
                try {
                    PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                            "SELECT points FROM PRODUCT WHERE name = ?");
                    statement.setString(1,newValue.toString());
                    ResultSet rs = statement.executeQuery();
                    while (rs.next()){
                        //System.out.println(rs.getString("points"));
                        product_points.setText(rs.getString("points"));
                        pointsInteger = Integer.valueOf(rs.getString("points"));//单位产品积分数 由字符串改为数字
                    }
                } catch (SQLException e) {
                    e.printStackTrace();
                }

                //若金额已经设定，则更新总积分数
                if (!value.getText().isEmpty()){
                    Integer inputValue = Integer.valueOf(value.getText());
                    Integer sumPoints = pointsInteger*inputValue;
                    points.setText(sumPoints.toString());
                    //若无转介绍人，则激活保存按钮
                    if (is_intro_exist.getSelectionModel().getSelectedItem().toString().equals("否")){
                        saveButton.setDisable(false);
                    }else {
                        saveButton.setDisable(true);
                    }
                }else {
                    saveButton.setDisable(true);
                }

                /**
                 * 判断是否有对应的转介绍版本的产品
                 * @version 2020.03.08
                 */
                try {
                    PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                            "SELECT * FROM PRODUCT WHERE name = ?");
                    statement.setString(1,newValue.toString()+"转介绍");
                    ResultSet rs = statement.executeQuery();
                    if (rs.next()){ //若有对应转介绍版本
                        warning.setTextFill(Color.GREEN);
                        warning.setText("提示：该产品有转介绍版本");
                        //让转介绍人输入区绑定对应转介绍版本
                        intro_product_name.getSelectionModel().select(rs.getString("name"));
                        intro_product_points.setText(rs.getString("points"));
                        intro_product_points.setDisable(true);

                    }else {//若无对应转介绍版本 : 转介绍人积分记录的产品信息与客户相同
                        warning.setTextFill(Color.GREEN);
                        warning.setText("提示：该产品无转介绍版本");
                        //清除转介绍人输入区对应的转介绍产品信息
                        intro_product_name.getSelectionModel().select(product_name.getSelectionModel().getSelectedItem());
                        intro_product_points.setText(product_points.getText());
                        intro_product_points.setDisable(true);
                        //积分计算方式限制为固定积分制
                        intro_pointsType.getSelectionModel().select("固定积分制");
                        intro_pointsType.setDisable(true);

                    }
                } catch (SQLException e) {
                    e.printStackTrace();
                }



            }
        });

        /**
         * 监听 积分计算方式
         */
        intro_pointsType.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                warning.setText("");
                //判断是否已经定位转介绍人
                if (!intro_name.getText().isEmpty()){
                    //若已经定位成功： 根据积分计算方式，计算积分
                    if (newValue.equals("按金额记(与客户相同)")){
                        intro_getpoints.setDisable(true);
                        intro_getpoints.setText(String.valueOf(Integer.valueOf(value.getText())*Integer.valueOf(intro_product_points.getText())));
                        saveButton.setDisable(false);
                    }else{//固定积分制
                        System.out.println("选择了固定积分制");
                        //激活积分栏，手动输入积分
                        intro_getpoints.setText("");
                        intro_getpoints.setDisable(false);
                        //若已经输入积分数量，激活保存按钮
                        if (AccountValidatorUtil.isNumber(intro_getpoints.getText())){
                            saveButton.setDisable(false);
                        }else {
                            saveButton.setDisable(true);
//                            warning.setTextFill(Color.RED);
//                            warning.setText("转介绍人积分数格式有误");
                        }
                    }
                }else {//没有定位转介绍人
                    warning.setTextFill(Color.RED);
                    warning.setText("请定位转介绍人");
                    saveButton.setDisable(true);
                }

            }
        });

        /**
         * 监听 转介绍人获得的积分数量
         */
        intro_getpoints.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                warning.setText("");
                //判断是否已经定位转介绍人
                if (intro_name.getText().isEmpty()){
//                    warning.setTextFill(Color.RED);
//                    warning.setText("请定位转介绍人");
                }else if (!AccountValidatorUtil.isNumber(newValue)){//判断是否为合法数字
                    saveButton.setDisable(true);
//                    warning.setTextFill(Color.GREEN);
//                    warning.setText("请输入转介绍人获得的积分");
                }else {
                    saveButton.setDisable(false);
                }
            }
        });



        /**
         * 输入了金额之后自动与单位产品积分数相乘并输出到界面
         * 判断当前输入情况，看是否激活保存按钮
         */
        value.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {

                if (AccountValidatorUtil.isNumber(newValue) && !newValue.isEmpty()){//验证输入的是否为数字
                    if (Integer.valueOf(newValue) <=10000){//验证数字是否小于10000
                        if (!product_points.getText().isEmpty()){//验证是否已经选择了产品
                            warning.setText("");
                            Integer inputValue = Integer.valueOf(newValue);
                            Integer sumPoints = pointsInteger*inputValue;
                            points.setText(sumPoints.toString());
                            //若无转介绍人，则激活保存按钮
                            if (is_intro_exist.getSelectionModel().getSelectedItem().toString().equals("否")){
                                saveButton.setDisable(false);
                            }
                        }else {
                            saveButton.setDisable(true);
                            warning.setText("选择产品后将自动计算积分数");
                        }//验证是否已经选择了产品
                    }else {
                        saveButton.setDisable(true);
                        warning.setTextFill(Color.RED);
                        warning.setText("警告：金额需小于10000");
                    }//验证数字是否小于10000
                }else if (newValue.isEmpty()){//验证金额是否为空（ 场景：删除重输 ）
                    saveButton.setDisable(true);
                    warning.setText("");
                    points.setText("");
                }else {//验证输入的是否为数字
                    saveButton.setDisable(true);
                    warning.setTextFill(Color.RED);
                    warning.setText("警告：金额只能为数字");
                }

            }
        });

        /**
         * 监听是否有转介绍人
         * 是：第三组输入有效
         * 否，则判断第二组输入是否完成，
         *        若完成，则激活保存按钮
         */
        is_intro_exist.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                warning.setText("");
                if (newValue.equals("是")){
                    //需要输入转介绍人信息，停用保存按钮
                    saveButton.setDisable(true);
                    //激活第三组输入组件
                    for (Node node:input_group3.getChildren()
                    ) {
                        node.setDisable(false);
                    }
                    //产品选择框不可手动更改
                    intro_product_name.setDisable(true);
                    //单位产品积分数不可手动更改
                    intro_product_points.setDisable(true);

                    //判断有无对应转介绍版本
                    if (intro_product_points.getText().isEmpty()){//无对应转介绍版本
                        intro_pointsType.setDisable(true);//限定为固定积分制
                        intro_getpoints.setDisable(false);
                    }

                }else {//选择无转介绍人后，清空并禁用第三组输入
                    intro_cardnumber.setText("");
                    intro_name.setText("");
                    intro_getpoints.setText("");
                    //intro_product_points.setText("");
                    for (Node node:input_group3.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    //判断是否已经完成第二组输入 (积分数是否有数字)
                    if (!points.getText().isEmpty()){
                        saveButton.setDisable(false);
                    }else {
                        saveButton.setDisable(true);
                    }
                }
            }
        });

        /**
         * 实时判断身份证格式是否正确
         */
        card_number.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {

                account.setText("");
                value.setText("");


                if (!IdentityUtils.isLegalIDNumber(newValue)){
                    warning.setTextFill(Color.RED);
                    warning.setText("身份证格式有误");
                    for (Node node:input_group2.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    for (Node node:input_group3.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    saveButton.setDisable(true);

                }else {
                    warning.setTextFill(Color.GREEN);
                    warning.setText("身份证格式正确");

                }
            }
        });






    }//contentListener*********************************************************************************************


    /**
     * 定位转介绍人
     * @param event
     */
    @FXML
    public void searchIntro(ActionEvent event) {

        if (IdentityUtils.isLegalIDNumber(StringUtils.trimToEmpty(card_number.getText()))){ //检测身份证号格式
            //执行数据库查询
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT name FROM CSR WHERE card_number =?");
                statement.setString(1,intro_cardnumber.getText());
                ResultSet rs = statement.executeQuery();
                while (rs.next()){
                    intro_name.setText(rs.getString("name"));
                }
                //验证数据库中是否有此客户
                if (!intro_name.getText().isEmpty()){
                    if (intro_cardnumber.getText().equals(card_number.getText())){
                        warning.setTextFill(Color.RED);
                        warning.setText("不可将本人作为转介绍人");
                    }else{
                        warning.setTextFill(Color.GREEN);
                        warning.setText("定位转介绍人成功");

                        //TODO 固定积分制的积分数在本类开始处设定。
                        //定位成功： 根据积分计算方式，作出处理
                        if (intro_pointsType.getSelectionModel().getSelectedItem().equals("按金额记(与客户相同)")){
                            intro_getpoints.setText(String.valueOf(Integer.valueOf(product_points.getText())*Integer.valueOf(intro_product_points.getText())));
                            saveButton.setDisable(false);
                            intro_getpoints.setDisable(true);
                        }else if (intro_pointsType.getSelectionModel().getSelectedItem().equals("固定积分制")){
                            //输入金额后才能激活保存按钮
                            saveButton.setDisable(true);
                            intro_getpoints.setDisable(false);
                            //再选一便固定积分制，让下一步判断进入积分计算方式的监听器里
//                            intro_pointsType.getSelectionModel().select("按金额记(与客户相同)");
//                            intro_pointsType.getSelectionModel().select("固定积分制");
                        }
                    }
                }else {
                    warning.setTextFill(Color.RED);
                    warning.setText("数据库中不存在此客户信息");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }else {
            warning.setTextFill(Color.RED);
            warning.setText("警告：身份证格式有误");
        }

    }


    /**
     * 保存
     *
     * 由于前面的逻辑已经决定了，能按保存按钮的时候，所有信息必定已经输入完毕
     * 所以只需判断是否含有转介绍人即可，若有，则保存两份记录，若无，则保存一份
     *
     * @param event
     */
    @FXML
    public void saveRecord(ActionEvent event) {

        if (((Stage)saveButton.getScene().getWindow()).getTitle().equals("新建记录（未注册）") && !checkDB()){
            warning.setText("试用版仅可添加20条记录");
        }else {
            //当前时间
            Date now = new Date();
            //SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");//设置日期格式
            //String createTime = dateFormat.format(now);//格式化然后放入字符串中

            //第一组输入
            newRecord.setCsr_name(csr_name.getText());  //客户名字
            newRecord.setCard_number(card_number.getText());  //客户身份证号
            newRecord.setAccount(account.getText());  //客户账号
            //第二组输入
            newRecord.setProduct_name(product_name.getSelectionModel().getSelectedItem().toString()); //产品名字
            newRecord.setProduct_points(Integer.valueOf(product_points.getText()));  //单位产品积分数
            newRecord.setPoints(Integer.valueOf(points.getText())); //积分数  单位产品积分数 * 金额
            newRecord.setType(type.getSelectionModel().getSelectedItem().toString()); //交易渠道 电子或线下
            newRecord.setValue(value.getText());  //金额
            //第三组输入
            newRecord.setIntro_cardnumber(intro_cardnumber.getText());  //转介绍人身份证号
            newRecord.setIntro_name(intro_name.getText());
            newRecord.setIntro_flag("否");//转介绍标识： 此份记录并非转介绍积分
            newRecord.setIntro_pointsType(intro_pointsType.getSelectionModel().getSelectedItem().toString());

            //默认输入
            newRecord.setNote("未兑换");  //兑换标志 （默认否）
            newRecord.setDate(now);  //当前日期

            if (RecordDataHelper.insertNewRecord(newRecord)){
                System.out.println("保存新积分记录信息成功");
            }else {
                System.out.println("保存新积分记录信息失败");
            }


            /**
             * 有转介绍人，另存一份转介绍人信息
             */
            if (is_intro_exist.getSelectionModel().getSelectedItem().equals("是")){
                Record introRecord = new Record();

                //第一组输入
                introRecord.setCsr_name(intro_name.getText());  //介绍人名字
                introRecord.setCard_number(intro_cardnumber.getText());  //介绍人身份证号
                introRecord.setAccount(account.getText());  //账号
                //第二组输入
                introRecord.setProduct_name(intro_product_name.getSelectionModel().getSelectedItem().toString()); //产品名字
                introRecord.setProduct_points(Integer.valueOf(intro_product_points.getText()));  //单位产品积分数
                introRecord.setPoints(Integer.valueOf(intro_getpoints.getText())); //积分数  单位产品积分数 * 金额
                introRecord.setType(type.getSelectionModel().getSelectedItem().toString()); //交易渠道 电子或线下
                introRecord.setValue(value.getText());  //金额
                //第三组输入
                introRecord.setIntro_cardnumber("");  //转介绍人身份证号 留空
                introRecord.setIntro_flag("是");//转介绍标识： 此份记录为转介绍积分
                introRecord.setIntro_pointsType(intro_pointsType.getSelectionModel().getSelectedItem().toString());
                //默认输入
                introRecord.setNote("未兑换");  //兑换标志 （默认否）
                introRecord.setDate(now);  //当前日期

                if (RecordDataHelper.insertNewRecord(introRecord)){
                    System.out.println("保存介绍人【积分产品】信息成功");
                }else {
                    System.out.println("保存介绍人【积分产品】信息失败");
                }
            }

            //新增客户之后刷新界面
            MainController mainController = MainWindowLoader.getMainController();
            mainController.loadPointsManageTab();
            //关闭本窗口
            ((Stage)saveButton.getScene().getWindow()).close();
        }

    }//saveRecord


    /**
     * 检查数据库是否可以继续使用
     * 如果是未注册版本，检查数据库中是否超过20条记录了
     * @return 如果超过20，返回false，不然返回true
     */
    private static boolean checkDB(){
        try {
            DatabaseHandler handler = DatabaseHandler.getInstance();//拿到已经创建的实例引用 （最开始是在Main中的主函数里创建的）
            String qu = "SELECT * FROM RECORD";
            ResultSet rs = handler.execQuery(qu);
//            rs.last();
//            int rowCount = rs.getRow();
            int rowCount=0;
            while (rs.next()){
                rowCount++;
            }
            System.out.println(rowCount);

            if (rowCount>=20){
                return false;
            }else {
                return true;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return true;
    }



}//NewRecord
