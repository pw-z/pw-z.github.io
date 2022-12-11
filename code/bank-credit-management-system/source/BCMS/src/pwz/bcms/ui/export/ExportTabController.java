package pwz.bcms.ui.export;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.ui.export.model.CSRIntroPointsRecord;
import pwz.bcms.ui.export.model.CSRPointsRecord;
import pwz.bcms.ui.export.model.GiftRecordEx;
import pwz.bcms.util.ExportExcelUtil;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.paint.Color;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;
import javafx.util.Callback;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.*;


/**
 * 文件导出，共六种文件类型
 * 0. 某时间段内 单个客户业务积分总数统计
 * 1. 某时间段内 已兑换积分总数统计
 * 2. 某时间段内 未兑换积分总数统计
 * 3. 某时间段内 礼品兑换统计
 * 4. 某时间段内 转介绍积分总数统计
 * 5. 某时间段内 转介绍业务笔数统计
 *
 */
public class ExportTabController implements Initializable {

    @FXML
    public ChoiceBox exportFileType; //导出文件类型
    public ChoiceBox exportFileFormat; //文件格式: PDF、EXCEL
    public Button exportButton; //导出按钮
    public TextField savePath;  //显示选择的路径
    public Button chooseFolderButton;  //路径选择按钮
    public Label warning; //底部提示信息
    public DatePicker dataStart; //开始日期 格式 yyyy-MM-dd
    public DatePicker dataEnd; //结束日期 格式 yyyy-MM-dd

    public String dataStartString = "";
    public String dataEndString = "";
    private boolean isStartDateSet = false;
    private boolean isEndDateSet = false;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        exportFileType.getItems().addAll("单个客户业务积分总数统计", "已兑换积分总数统计", "未兑换积分总数统计", "礼品兑换统计", "转介绍积分总数统计", "转介绍业务笔数统计");
        exportFileType.getSelectionModel().select(0); //默认选择 单个客户业务积分总数统计
        exportFileFormat.getItems().addAll("Excel");
        //exportFileFormat.getItems().addAll("Excel","PDF");
        exportFileFormat.getSelectionModel().select(0); //默认选择Excel

        //初始化日期选择器
        dataEnd.setValue(LocalDate.now());
        final Callback<DatePicker, DateCell> dataStartCellFactory =
                new Callback<DatePicker, DateCell>() {
                    @Override
                    public DateCell call(final DatePicker datePicker) {
                        return new DateCell() {
                            @Override
                            public void updateItem(LocalDate item, boolean empty) {
                                super.updateItem(item, empty);

                                if (item.isAfter(
                                        dataEnd.getValue().minusDays(1))
                                ) {
                                    setDisable(true);
                                    setStyle("-fx-background-color: #ffc0cb;");
                                }
                                long p = ChronoUnit.DAYS.between(
                                         item,dataEnd.getValue()
                                );
                                setTooltip(new Tooltip(
                                        "您将导出 " + p + " 天的记录")
                                );
                            }
                        };
                    }
                };
        dataStart.setDayCellFactory(dataStartCellFactory);
        dataStart.setValue(dataEnd.getValue().minusYears(1));//过去一年的记录
        final Callback<DatePicker, DateCell> dataEndCellFactory =
                new Callback<DatePicker, DateCell>() {
                    @Override
                    public DateCell call(final DatePicker datePicker) {
                        return new DateCell() {
                            @Override
                            public void updateItem(LocalDate item, boolean empty) {
                                super.updateItem(item, empty);

                                if (item.isAfter(
                                        LocalDate.now())
                                ) {
                                    setDisable(true);
                                    setStyle("-fx-background-color: #ffc0cb;");
                                }
                                long p = ChronoUnit.DAYS.between(
                                        dataStart.getValue(), item
                                );
                                setTooltip(new Tooltip(
                                        "您将导出 " + p + " 天的记录")
                                );
                            }
                        };
                    }
                };
        dataEnd.setDayCellFactory(dataEndCellFactory);

        warning.setTextFill(Color.GREEN);
    }


    /**
     * 导出
     * @param event
     */
    @FXML
    public void exportFile(ActionEvent event) {
        warning.setText("");
        //判断输入条件，无误后执行导出参数
        if (checkInput()){
            switch (exportFileType.getSelectionModel().getSelectedIndex()){
                case 0://单个客户业务积分总数统计
                    warning.setText("正在导出 单个客户业务积分总数统计");
                    exportFileType0();
                    break;
                case 1://已兑换积分总数统计
                    warning.setText("正在导出 已兑换积分总数统计");
                    exportFileType1();
                    break;
                case 2://未兑换积分总数统计
                    warning.setText("正在导出 未兑换积分总数统计");
                    exportFileType2();
                    break;
                case 3://礼品兑换统计
                    warning.setText("正在导出 礼品兑换统计");
                    exportFileType3();
                    break;
                case 4://转介绍积分总数统计
                    warning.setText("正在导出 转介绍积分总数统计");
                    exportFileType4();
                    break;
                case 5://转介绍业务笔数统计
                    warning.setText("正在导出 转介绍业务笔数统计");
                    exportFileType5();
                    break;
            }
        }


    }

    /**
     * 输入判断
     * @return
     */
    private boolean checkInput(){
        warning.setTextFill(Color.RED);
        warning.setText("");
        if (savePath.getText().isEmpty()){
            warning.setText("未选择导出路径");
            return false;
        }else {
            return true;
        }
    }

    /**
     * 获取时间区间
     */
    private void initTimeValue(){
        dataStartString = dataStart.getValue().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));
        dataEndString = dataEnd.getValue().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));

        System.out.println(dataStartString + "----" + dataEndString);
    }

    /**
     * 单个客户业务积分总数统计
     */
    private void exportFileType0(){

        //获取时间区间
        initTimeValue();

        //哈希表内容：姓名、身份证号、总积分数
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE date >=? AND date<=? ORDER BY points DESC");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            ResultSet rs = statement.executeQuery();

            //用于将积分记录按照身份证号划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //积分记录哈希表，用于存放不同用户的总积分
            Integer tempTotalPoints; //临时的总分（从哈希表中取出的）
            Enumeration cardNumber; //哈希表的Key值

            List<CSRPointsRecord> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                Integer points = rs.getInt("points");
                System.out.print("ID：" + id + "   客户名：" + csr_name + "   身份证号：" + card_number + "   积分数：" + points);

                //构造一条记录  需要的属性：姓名、身份证号、总积分数
                CSRPointsRecord csrPointsRecord = new CSRPointsRecord();
                csrPointsRecord.setCsr_name(csr_name);
                csrPointsRecord.setGender(getGenderByCertId(card_number)); //到Csr表中获取各户性别
                csrPointsRecord.setAge(getAgeByCertId(card_number));
                csrPointsRecord.setCard_number(card_number);
                csrPointsRecord.setTotalPoints(points);

                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(card_number)){//若表中没有此身份证，则直接放进去
                    System.out.println("  表中==没有===添加新表项");
                    pointsHashtable.put(card_number,csrPointsRecord);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalPoints = ((CSRPointsRecord)pointsHashtable.get(card_number)).getTotalPoints();
                    csrPointsRecord.setTotalPoints(csrPointsRecord.getTotalPoints()+tempTotalPoints);
                    System.out.println("  表中==有=====更新积分   取出表中积分：" +  tempTotalPoints + "   当前积分总数：" + csrPointsRecord.getTotalPoints());
                    pointsHashtable.put(card_number, csrPointsRecord);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            cardNumber = pointsHashtable.keys();
            while (cardNumber.hasMoreElements()){
                str = (String)cardNumber.nextElement();
                list.add((CSRPointsRecord)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<CSRPointsRecord> util = new ExportExcelUtil<CSRPointsRecord>();
            String[] columnNames = { "客户姓名","性别", "身份证号","年龄", "积分数量"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "单个客户业务积分总数统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 单个客户业务积分总数统计.xls 成功");
    }



    /**
     * 已兑换积分总数统计
     */
    private void exportFileType1(){

        //获取时间区间
        initTimeValue();

        //哈希表内容：姓名、身份证号、总积分数
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE date >=? AND date<=? AND note=? ORDER BY points DESC");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            statement.setString(3,"已兑换");
            ResultSet rs = statement.executeQuery();

            //用于将积分记录按照身份证号划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //积分记录哈希表，用于存放不同用户的总积分
            Integer tempTotalPoints; //临时的总分（从哈希表中取出的）
            Enumeration cardNumber; //哈希表的Key值

            List<CSRPointsRecord> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                Integer points = rs.getInt("points");
                System.out.print("ID：" + id + "   客户名：" + csr_name + "   身份证号：" + card_number + "   积分数：" + points);

                //构造一条记录  需要的属性：姓名、身份证号、总积分数
                CSRPointsRecord csrPointsRecord = new CSRPointsRecord();
                csrPointsRecord.setCsr_name(csr_name);
                csrPointsRecord.setGender(getGenderByCertId(card_number)); //到Csr表中获取各户性别
                csrPointsRecord.setAge(getAgeByCertId(card_number));
                csrPointsRecord.setCard_number(card_number);
                csrPointsRecord.setTotalPoints(points);

                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(card_number)){//若表中没有此身份证，则直接放进去
                    System.out.println("  表中==没有===添加新表项");
                    pointsHashtable.put(card_number,csrPointsRecord);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalPoints = ((CSRPointsRecord)pointsHashtable.get(card_number)).getTotalPoints();
                    csrPointsRecord.setTotalPoints(csrPointsRecord.getTotalPoints()+tempTotalPoints);
                    System.out.println("  表中==有=====更新积分   取出表中积分：" +  tempTotalPoints + "   当前积分总数：" + csrPointsRecord.getTotalPoints());
                    pointsHashtable.put(card_number, csrPointsRecord);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            cardNumber = pointsHashtable.keys();
            while (cardNumber.hasMoreElements()){
                str = (String)cardNumber.nextElement();
                list.add((CSRPointsRecord)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<CSRPointsRecord> util = new ExportExcelUtil<CSRPointsRecord>();
            String[] columnNames = { "客户姓名","性别", "身份证号","年龄", "已兑换积分总数"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "已兑换积分总数统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 已兑换积分总数统计.xls 成功");
    }

    /**
     * 未兑换积分总数统计
     */
    private void exportFileType2(){

        //获取时间区间
        initTimeValue();

        //哈希表内容：姓名、身份证号、总积分数
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE date >=? AND date<=? AND note=? ORDER BY points DESC");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            statement.setString(3,"未兑换");
            ResultSet rs = statement.executeQuery();

            //用于将积分记录按照身份证号划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //积分记录哈希表，用于存放不同用户的总积分
            Integer tempTotalPoints; //临时的总分（从哈希表中取出的）
            Enumeration cardNumber; //哈希表的Key值

            List<CSRPointsRecord> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                Integer points = rs.getInt("points");
                System.out.print("ID：" + id + "   客户名：" + csr_name + "   身份证号：" + card_number + "   积分数：" + points);

                //构造一条记录  需要的属性：姓名、身份证号、总积分数
                CSRPointsRecord csrPointsRecord = new CSRPointsRecord();
                csrPointsRecord.setCsr_name(csr_name);
                csrPointsRecord.setGender(getGenderByCertId(card_number)); //到Csr表中获取各户性别
                csrPointsRecord.setAge(getAgeByCertId(card_number));
                csrPointsRecord.setCard_number(card_number);
                csrPointsRecord.setTotalPoints(points);

                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(card_number)){//若表中没有此身份证，则直接放进去
                    System.out.println("  表中==没有===添加新表项");
                    pointsHashtable.put(card_number,csrPointsRecord);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalPoints = ((CSRPointsRecord)pointsHashtable.get(card_number)).getTotalPoints();
                    csrPointsRecord.setTotalPoints(csrPointsRecord.getTotalPoints()+tempTotalPoints);
                    System.out.println("  表中==有=====更新积分   取出表中积分：" +  tempTotalPoints + "   当前积分总数：" + csrPointsRecord.getTotalPoints());
                    pointsHashtable.put(card_number, csrPointsRecord);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            cardNumber = pointsHashtable.keys();
            while (cardNumber.hasMoreElements()){
                str = (String)cardNumber.nextElement();
                list.add((CSRPointsRecord)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<CSRPointsRecord> util = new ExportExcelUtil<CSRPointsRecord>();
            String[] columnNames = { "客户姓名","性别", "身份证号","年龄", "未兑换积分总数"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "未兑换积分总数统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 未兑换积分总数统计.xls 成功");

    }

    /**
     * 礼品兑换统计
     */
    private void exportFileType3(){
//        warning.setTextFill(Color.RED);
//        warning.setText("暂不支持导出礼品兑换统计表");

        //获取时间区间
        initTimeValue();

        //哈希表内容：礼品名称、总兑换数量
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM GIFTRECORD WHERE date >=? AND date<=? ");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            ResultSet rs = statement.executeQuery();

            //用于将记录按照礼品名称划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //礼品兑换记录哈希表
            Integer tempTotalNumber; //临时的总兑换数量（从哈希表中取出的）
            Enumeration giftName; //哈希表的Key值

            List<GiftRecordEx> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                Integer number = rs.getInt("number");

                System.out.print("ID：" + id + "   礼品名：" + name + "   兑换数量：" + number );

                //构造一条记录  需要的属性：礼品名称、兑换数量
                GiftRecordEx giftRecordEx = new GiftRecordEx();
                giftRecordEx.setName(name);
                giftRecordEx.setNumber(number);

                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(name)){//若表中没有此身份证，则直接放进去
                    System.out.println("  表中==没有===添加新表项");
                    pointsHashtable.put(name,giftRecordEx);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalNumber = ((GiftRecordEx)pointsHashtable.get(name)).getNumber();
                    giftRecordEx.setNumber(giftRecordEx.getNumber()+tempTotalNumber);
                    System.out.println("  表中==有=====更新积分   取出表中兑换总数：" +  tempTotalNumber + "   当前总数：" + giftRecordEx.getNumber());
                    pointsHashtable.put(name, giftRecordEx);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            giftName = pointsHashtable.keys();
            while (giftName.hasMoreElements()){
                str = (String)giftName.nextElement();
                list.add((GiftRecordEx)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<GiftRecordEx> util = new ExportExcelUtil<GiftRecordEx>();
            String[] columnNames = { "礼品名称","总兑换量"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "礼品兑换统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 礼品兑换统计.xls 成功");
    }

    /**
     * 转介绍积分总数统计
     */
    private void exportFileType4(){

        //获取时间区间
        initTimeValue();

        //哈希表内容：姓名、身份证号、总积分数
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE date >=? AND date<=? AND intro_flag = ? ORDER BY points DESC");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            statement.setString(3,"是");
            ResultSet rs = statement.executeQuery();

            //用于将积分记录按照身份证号划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //积分记录哈希表，用于存放不同用户的总积分
            Integer tempTotalPoints; //临时的总分（从哈希表中取出的）
            Enumeration cardNumber; //哈希表的Key值

            List<CSRPointsRecord> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                Integer points = rs.getInt("points");
                System.out.print("ID：" + id + "   客户名：" + csr_name + "   身份证号：" + card_number + "   积分数：" + points);

                //构造一条记录  需要的属性：姓名、身份证号、总积分数
                CSRPointsRecord csrPointsRecord = new CSRPointsRecord();
                csrPointsRecord.setCsr_name(csr_name);
                csrPointsRecord.setGender(getGenderByCertId(card_number)); //到Csr表中获取各户性别
                csrPointsRecord.setAge(getAgeByCertId(card_number));
                csrPointsRecord.setCard_number(card_number);
                csrPointsRecord.setTotalPoints(points);

                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(card_number)){//若表中没有此身份证，则直接放进去
                    System.out.println("  表中==没有===添加新表项");
                    pointsHashtable.put(card_number,csrPointsRecord);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalPoints = ((CSRPointsRecord)pointsHashtable.get(card_number)).getTotalPoints();
                    csrPointsRecord.setTotalPoints(csrPointsRecord.getTotalPoints()+tempTotalPoints);
                    System.out.println("  表中==有=====更新积分   取出表中积分：" +  tempTotalPoints + "   当前积分总数：" + csrPointsRecord.getTotalPoints());
                    pointsHashtable.put(card_number, csrPointsRecord);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            cardNumber = pointsHashtable.keys();
            while (cardNumber.hasMoreElements()){
                str = (String)cardNumber.nextElement();
                list.add((CSRPointsRecord)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<CSRPointsRecord> util = new ExportExcelUtil<CSRPointsRecord>();
            String[] columnNames = { "客户姓名","性别", "身份证号","年龄", "转介绍积分总数"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "转介绍积分总数统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 转介绍积分总数统计.xls 成功");
    }

    /**
     * 转介绍业务笔数统计
     */
    private void exportFileType5(){

        //获取时间区间
        initTimeValue();

        //哈希表内容：姓名、身份证号、总积分数
        PreparedStatement statement = null;
        try {
            //获取到指定时间段内所有记录
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT * FROM RECORD WHERE date >=? AND date<=? AND intro_flag = ? ORDER BY points DESC");
            statement.setString(1,dataStartString);
            statement.setString(2,dataEndString);
            statement.setString(3,"是");
            ResultSet rs = statement.executeQuery();

            //用于将积分记录按照身份证号划分存储的哈希表
            Hashtable pointsHashtable = new Hashtable(); //积分记录哈希表，用于存放不同用户的总积分
            Integer tempTotalPoints; //临时的总分（从哈希表中取出的）
            Integer tempTradingVolume; //转介绍业务笔数
            Enumeration cardNumber; //哈希表的Key值
            List<CSRIntroPointsRecord> list = new ArrayList<>();//用于导出Excel的数据

            //对获取到的记录进行处理
            while (rs.next()) {
                String id = rs.getString("id");
                String csr_name = rs.getString("csr_name");
                String card_number = rs.getString("card_number");
                Integer points = rs.getInt("points");

                //构造一条记录  需要的属性：姓名、身份证号、总积分数
                CSRIntroPointsRecord csrIntroPointsRecord = new CSRIntroPointsRecord();
                csrIntroPointsRecord.setCsr_name(csr_name);
                csrIntroPointsRecord.setGender(getGenderByCertId(card_number)); //到Csr表中获取各户性别
                csrIntroPointsRecord.setAge(getAgeByCertId(card_number));
                csrIntroPointsRecord.setCard_number(card_number);
                csrIntroPointsRecord.setTotalPoints(points);
                csrIntroPointsRecord.setTradingVolume(1); //每条记录 转介绍业务笔数记1

                //System.out.println(csrIntroPointsRecord.getTradingVolume());
                //将记录加入哈希表中
                if (!pointsHashtable.containsKey(card_number)){//若表中没有此身份证，则直接放进去
                    pointsHashtable.put(card_number,csrIntroPointsRecord);
                }else{//若表中有此身份证号，把此条记录拿出来，加上新的积分记录，再放进去
                    tempTotalPoints = ((CSRIntroPointsRecord)pointsHashtable.get(card_number)).getTotalPoints();
                    csrIntroPointsRecord.setTotalPoints(csrIntroPointsRecord.getTotalPoints()+tempTotalPoints);
                    tempTradingVolume = ((CSRIntroPointsRecord)pointsHashtable.get(card_number)).getTradingVolume();
                    csrIntroPointsRecord.setTradingVolume(csrIntroPointsRecord.getTradingVolume()+tempTradingVolume);
                    pointsHashtable.put(card_number, csrIntroPointsRecord);
                }
            }

            String str;
            System.out.println("=================导出数据文件================");
            //导出数据文件
            cardNumber = pointsHashtable.keys();
            while (cardNumber.hasMoreElements()){
                str = (String)cardNumber.nextElement();
                list.add((CSRIntroPointsRecord)pointsHashtable.get(str));
            }
            // 按积分总数降序排序
            Collections.sort(list);
            ExportExcelUtil<CSRIntroPointsRecord> util = new ExportExcelUtil<CSRIntroPointsRecord>();
            String[] columnNames = { "客户姓名","性别", "身份证号","年龄", "积分数量","转介绍笔数"};//表格头部标题集合
            util.exportExcel("报表导出", columnNames, list, new FileOutputStream(savePath.getText() +"\\"+ "转介绍业务笔数统计.xls"), ExportExcelUtil.EXCEL_FILE_2003);
            Runtime.getRuntime().gc();//util类关闭有问题，在此处手动垃圾回收
        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        warning.setTextFill(Color.GREEN);
        warning.setText("导出 转介绍业务笔数统计.xls 成功");
    }



    /**
     * 选择导出路径
     * @param event
     */
    @FXML
    public void chooseFolder(ActionEvent event) {
        DirectoryChooser directoryChooser =new DirectoryChooser();
        directoryChooser.setTitle("选择要导出的路径");
        File directory = directoryChooser.showDialog(new Stage());

        if (directory != null) {
            //将选取的路径显示在面板上
            savePath.setText(directory.getAbsolutePath());
            System.out.println(directory.getAbsolutePath());
        }
    }




    /**
     * 获取客户性别
     * @param csr_cardNumber 客户身份证号
     * @return gender 客户性别
     */
    private String getGenderByCertId(String csr_cardNumber){
        PreparedStatement statement = null;
        try {
            statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                    "SELECT gender FROM CSR WHERE card_number=?");
            statement.setString(1,csr_cardNumber);
            ResultSet rs = statement.executeQuery();
            while (rs.next()){
                String gender = rs.getString("gender");
                return gender;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return "";
    }


    /**
     * 根据身份证号获取年龄
     * @param csr_cardNumber 客户身份证号
     * @return age 客户年龄
     */
    public static String getAgeByCertId(String csr_cardNumber) {
        String birthday = "";
        if (csr_cardNumber.length() == 18) {
            birthday = csr_cardNumber.substring(6, 10) + "/"
                    + csr_cardNumber.substring(10, 12) + "/"
                    + csr_cardNumber.substring(12, 14);
        }
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd");
        Date now = new Date();
        Date birth = new Date();
        try {
            birth = sdf.parse(birthday);
        } catch (ParseException e) {
        }
        long intervalMilli = now.getTime() - birth.getTime();
        int age = (int) (intervalMilli/(24 * 60 * 60 * 1000))/365;
        //System.out.println(age);
        return age +"";
    }

}//class
