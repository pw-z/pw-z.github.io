package pwz.bcms.po;

public class Gift {

    private String id; //礼品编号
    private String name; //礼品名称
    private String type; //产品型号
    private String value; //采购价格
    private String flag; //过期标识 （默认否）
    private String note; //备注  （可空）

    public Gift() {
    }

    public Gift(String id, String name, String type, String value, String flag, String note) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.value = value;
        this.flag = flag;
        this.note = note;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public String getValue() {
        return value;
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

    public void setType(String type) {
        this.type = type;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }

    public void setNote(String note) {
        this.note = note;
    }
}
