package pwz.bcms.po;

import java.util.Date;

public class GiftRecord {

    private String id; //礼品编号
    private String name; //礼品名称
    private Date date; //礼品兑换时间
    private Integer number; //数量


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
    }
}
