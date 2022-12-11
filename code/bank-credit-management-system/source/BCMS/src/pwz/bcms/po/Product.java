package pwz.bcms.po;


//积分产品模型
public class Product {

    private String id; //产品编号
    private String name; //产品名称
    private String points; //单位产品积分数
    private String tlimit;  //产品期限 （日期）
    private String flag; //转介绍标识 （默认否）
    private String note; //备注  （可空）


    public Product() {
    }

    public Product(String name) {
        this.name = name;
    }

    public Product(String id, String name, String points, String tlimit, String flag, String note) {
        this.id = id;
        this.name = name;
        this.points = points;
        this.tlimit = tlimit;
        this.flag = flag;
        this.note = note;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getPoints() {
        return points;
    }

    public String getTlimit() {
        return tlimit;
    }

    public String getFlag() {
        return flag;
    }

    public String getNote() {
        return note;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPoints(String points) {
        this.points = points;
    }

    public void setTlimit(String tlimit) {
        this.tlimit = tlimit;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }

    public void setNote(String note) {
        this.note = note;
    }
}
