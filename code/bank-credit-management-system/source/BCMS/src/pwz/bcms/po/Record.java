package pwz.bcms.po;


import javafx.beans.property.SimpleBooleanProperty;

import java.util.Date;


//积分记录
public class Record {

    private String id; //序号
    private String csr_name; //客户姓名
    private String card_number; //身份证号
    private String account;  //账号

    private String product_name; //产品名称
    private Integer product_points; //单位产品积分数
    private String value; //金额
    private Date date; //业务办理时间
    private String type; //交易渠道
    private Integer points;  //积分数


    private String intro_cardnumber; //转介绍人身份证号 （可空）
    private String intro_name; //转介绍人姓名
    private String intro_flag; //转介绍积分标识
    private String note; //备注 （是否已兑换）

    private String intro_pointsType; //积分计算方式
    public checkbox cb = new checkbox(); //封装的Checkbox类，返回可视化checkbox

    private SimpleBooleanProperty cbboolean = new SimpleBooleanProperty();

    public Record() {
    }

    //用于测试导出Excel用的构造器
    public Record(String csr_name, String card_number, Integer points) {
        this.csr_name = csr_name;
        this.card_number = card_number;
        this.points = points;
    }

    public Record(String id, String csr_name, String card_number, String account, String product_name, Integer product_points, String value, Date date, String type, Integer points , String intro_cardnumber, String note,String intro_flag) {
        this.id = id;
        this.csr_name = csr_name;
        this.card_number = card_number;
        this.account = account;
        this.product_name = product_name;
        this.product_points = product_points;
        this.value = value;
        this.date = date;
        this.type = type;
        this.points = points;

        this.intro_cardnumber = intro_cardnumber;
        this.note = note;
        this.intro_flag = intro_flag;

    }

    public Record(String id, String csr_name, String card_number, String account, String product_name, Integer product_points, String value, Date date, String type, Integer points , String intro_cardnumber, String note,String intro_flag,String intro_pointsType,String intro_name) {
        this.id = id;
        this.csr_name = csr_name;
        this.card_number = card_number;
        this.account = account;
        this.product_name = product_name;
        this.product_points = product_points;
        this.value = value;
        this.date = date;
        this.type = type;
        this.points = points;

        this.intro_cardnumber = intro_cardnumber;
        this.note = note;
        this.intro_flag = intro_flag;
        this.intro_pointsType = intro_pointsType;
        this.intro_name = intro_name;
    }


    public boolean isCbboolean() {
        return cbboolean.get();
    }

    public SimpleBooleanProperty cbbooleanProperty() {
        return cbboolean;
    }

    public void setCbboolean(boolean cbboolean) {
        this.cbboolean.set(cbboolean);
    }

    public String getIntro_name() {
        return intro_name;
    }

    public void setIntro_name(String intro_name) {
        this.intro_name = intro_name;
    }
    public String getIntro_pointsType() {
        return intro_pointsType;
    }

    public void setIntro_pointsType(String intro_pointsType) {
        this.intro_pointsType = intro_pointsType;
    }

    public String getIntro_flag() {
        return intro_flag;
    }

    public void setIntro_flag(String intro_flag) {
        this.intro_flag = intro_flag;
    }
    public String getId() {
        return id;
    }

    public String getCsr_name() {
        return csr_name;
    }

    public String getCard_number() {
        return card_number;
    }

    public String getAccount() {
        return account;
    }

    public String getProduct_name() {
        return product_name;
    }

    public String getValue() {
        return value;
    }

    public Date getDate() {
        return date;
    }

    public String getType() {
        return type;
    }

    public Integer getPoints() {
        return points;
    }



    public String getNote() {
        return note;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setCsr_name(String csr_name) {
        this.csr_name = csr_name;
    }

    public void setCard_number(String card_number) {
        this.card_number = card_number;
    }

    public void setAccount(String account) {
        this.account = account;
    }

    public void setProduct_name(String product_name) {
        this.product_name = product_name;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setPoints(Integer points) {
        this.points = points;
    }


    public void setNote(String note) {
        this.note = note;
    }

    public String getIntro_cardnumber() {
        return intro_cardnumber;
    }

    public void setIntro_cardnumber(String intro_cardnumber) {
        this.intro_cardnumber = intro_cardnumber;
    }

    public Integer getProduct_points() {
        return product_points;
    }

    public void setProduct_points(Integer product_points) {
        this.product_points = product_points;
    }

}
