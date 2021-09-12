package pwz.bcms.ui.pointsmanage;

import pwz.bcms.db.RecordDataHelper;
import pwz.bcms.po.Record;
import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class ManageRecord implements Initializable {

    final String INTRO_POINTS_PER_RECORD = "20"; //固定积分制，每笔交易转介绍人获得的积分数

    @FXML
    public TextField card_number;  //身份证号  以此定位客户
    public TextField csr_name;  //搜索到客户后，将名字返回
    public TextField account;  //客户的账号
    public Label accountLabel;

    @FXML
    public TextField product_name;  //产品名称 （下拉选框，选择此次交易涉及到的积分产品）
    public TextField product_points; //单位产品积分数
    public TextField value;  //此次交易的金额
    public TextField type;  //交易类型 电子、线下
    public TextField points;  //此次交易获得的积分数量
    public TextField is_intro_exist;


    @FXML
    public TextField intro_cardnumber;  //介绍人的身份证号  以此定位介绍人
    public TextField intro_name;  //介绍人姓名  搜索到介绍人后后，将名字返回
   // public Button saveButton;  //保存按钮  （保存此次记录）  // 2020年3月8日改动：删除此按钮
    public TextField intro_getpoints; //转介绍人将获得积分
    public TextField intro_pointsType; //转介绍人获得的积分 的计算方式 ：固定积分制、按金额记
    public TextField intro_flag; //转介绍积分标识
    public TextField note;  //备注信息（是否已兑换）

    @FXML
    public Label warning;  //底部提示信息
    public Button deleteButton;
    public Label recordID; //记录编号


    //自定义属性
    Record newRecord = new Record();


    @Override
    public void initialize(URL location, ResourceBundle resources) {
        //saveButton.setDisable(true);
        //myListener();
    }


//    private void myListener(){
//
//        /**
//         * 输入了金额之后自动与单位产品积分数相乘并输出到界面
//         * 判断当前输入情况，看是否激活保存按钮
//         */
//        value.textProperty().addListener(new ChangeListener<String>() {
//            @Override
//            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
//
//                if (AccountValidatorUtil.isNumber(newValue) && !newValue.isEmpty()){//验证输入的是否为数字
//                    if (Integer.valueOf(newValue) <=10000){//验证数字是否小于10000
//                        warning.setText("");
//                        Integer inputValue = Integer.valueOf(newValue); //输入的金额
//                        Integer pointsInteger= Integer.valueOf(product_points.getText()); //单位产品积分数 由字符串改为数字
//                        Integer sumPoints = pointsInteger*inputValue; //积分数
//                        points.setText(sumPoints.toString());
//
//                        //处理转介绍人获得的积分 (如果有转介绍人)
//                        if (!intro_cardnumber.getText().isEmpty()){
//                            if (intro_pointsType.getText().equals("固定积分制")){
//                                intro_getpoints.setText(INTRO_POINTS_PER_RECORD);
//                            }else {//按金额记(与客户相同)
//                                intro_getpoints.setText(sumPoints.toString());
//                            }
//                        }
//                        saveButton.setDisable(false);
//                    }else {
//                        saveButton.setDisable(true);
//                        warning.setTextFill(Color.RED);
//                        warning.setText("警告：金额需小于10000");
//                    }//验证数字是否小于10000
//                }else if (newValue.isEmpty()){//验证金额是否为空（ 场景：删除重输 ）
//                    saveButton.setDisable(true);
//                    warning.setText("");
//                    points.setText("");
//                }else {//验证输入的是否为数字
//                    saveButton.setDisable(true);
//                    warning.setTextFill(Color.RED);
//                    warning.setText("警告：金额只能为数字");
//                }
//            }
//        });
//    }


    /**！！！！！！！！！此方法已经作废
     * 修改用户信息，需要同时更新两条记录 （只有非转介绍记录可以修改）
     * @param event
     */
//    public void saveRecord(ActionEvent event) {
//        //当前时间
//        Date now = new Date();
//        //SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//设置日期格式
//        //String createTime = dateFormat.format(now);//格式化然后放入字符串中
//
//        newRecord.setId(recordID.getText());
//        //第一组输入
//        newRecord.setCsr_name(csr_name.getText());  //客户名字
//        newRecord.setCard_number(card_number.getText());  //客户身份证号
//        newRecord.setAccount(account.getText());  //客户账号
//        //第二组输入
//        newRecord.setProduct_name(product_name.getText()); //产品名字
//        newRecord.setProduct_points(Integer.valueOf(product_points.getText()));  //单位产品积分数
//        newRecord.setPoints(Integer.valueOf(points.getText())); //积分数  单位产品积分数 * 金额
//        newRecord.setType(type.getText()); //交易渠道 电子或线下
//        newRecord.setValue(value.getText());  //金额
//        //第三组输入
//        newRecord.setIntro_cardnumber(intro_cardnumber.getText());  //转介绍人身份证号
//        newRecord.setIntro_name(intro_name.getText());
//        newRecord.setIntro_flag("否");//转介绍标识： 此份记录并非转介绍积分
//        newRecord.setIntro_pointsType(intro_pointsType.getText());
//
//        //默认输入
//        newRecord.setNote("未兑换");  //兑换标志 （默认否）
//        newRecord.setDate(now);  //当前日期
//
//        //更新数据库
//        if (RecordDataHelper.updateNewRecord(newRecord)){
//            System.out.println("更新【积分产品】信息成功");
//        }else {
//            System.out.println("更新【积分产品】信息失败");
//        }
//
//
//        /**
//         * 有转介绍人，另更新一份转介绍人对应记录
//         */
//        if (is_intro_exist.getText().equals("是")){
//            Record introRecord = new Record();
//
//            introRecord.setId(String.valueOf(Integer.valueOf(recordID.getText())+1));
//            //第一组输入
//            introRecord.setCsr_name(intro_name.getText());  //介绍人名字
//            introRecord.setCard_number(intro_cardnumber.getText());  //介绍人身份证号
//            introRecord.setAccount(account.getText());  //账号
//            //第二组输入
//            introRecord.setProduct_name(product_name.getText()); //产品名字
//            introRecord.setProduct_points(Integer.valueOf(product_points.getText()));  //单位产品积分数
//            introRecord.setPoints(Integer.valueOf(intro_getpoints.getText())); //积分数  单位产品积分数 * 金额
//            introRecord.setType(type.getText()); //交易渠道 电子或线下
//            introRecord.setValue(value.getText());  //金额
//            //第三组输入
//            introRecord.setIntro_cardnumber("");  //转介绍人身份证号 留空
//            introRecord.setIntro_flag("是");//转介绍标识： 此份记录为转介绍积分
//            introRecord.setIntro_pointsType(intro_pointsType.getText());
//            //默认输入
//            introRecord.setNote("未兑换");  //兑换标志 （默认否）
//            introRecord.setDate(now);  //当前日期
//
//            //更新数据库
//            if (RecordDataHelper.updateNewRecord(introRecord)){
//                System.out.println("更新介绍人【积分产品】信息成功");
//            }else {
//                System.out.println("更新介绍人【积分产品】信息失败");
//            }
//        }
//        //更新之后刷新界面
//        MainController mainController = MainWindowLoader.getMainController();
//        mainController.loadPointsManageTab();
//        //关闭窗口
//        ((Stage)saveButton.getScene().getWindow()).close();
//    }


    /**
     * 删除，需要同时删除两条记录(如果有转介绍人)
     * @param event
     */
    public void deleteRecord(ActionEvent event) {

        newRecord.setId(recordID.getText());
        RecordDataHelper.deleteRecord(newRecord);
        if (is_intro_exist.getText().equals("是")){
            newRecord.setId(String.valueOf(Integer.valueOf(recordID.getText())+1)); //对应转介绍积分记录的编号，是原记录+1
            RecordDataHelper.deleteRecord(newRecord);
        }

        //更新之后刷新界面
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadPointsManageTab();
        //关闭窗口
        ((Stage)deleteButton.getScene().getWindow()).close();

    }
}
