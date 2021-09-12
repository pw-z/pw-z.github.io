package pwz.bcms.po;


//客户模型
public class Csr {

    private String id; //自增序号
    private String name; //客户姓名
    private String gender; //性别
    private String card_type; //证件类型
    private String card_number; //证件号码  (身份证号)  （提供校验）
    private String phone; //手机号 （提供校验）
    private String company; //工作单位  （可空）
    private String homelocation; //家庭住址  （可空）
    private String note; //备注  （可空）
    private String points; //积分余额 （没用到）

    public Csr(){

    }

    public Csr(String id, String name, String gender) {
        this.id = id;
        this.name = name;
        this.gender = gender;
    }

    public Csr(String id,String name, String gender, String card_number, String phone, String homelocation, String company, String note) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.card_number = card_number;
        this.phone = phone;
        this.homelocation = homelocation;
        this.company = company;
        this.note = note;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public String getCard_type() {
        return card_type;
    }

    public String getCard_number() {
        return card_number;
    }

    public String getPhone() {
        return phone;
    }

    public String getCompany() {
        return company;
    }

    public String getHomelocation() {return homelocation;}
    public String getNote() {
        return note;
    }

    public String getPoints() {
        return points;
    }



    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setCard_type(String card_type) {
        this.card_type = card_type;
    }

    public void setCard_number(String card_number) {
        this.card_number = card_number;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public void setHomelocation(String homelocation) { this.homelocation = homelocation; }
    public void setNote(String note) {
        this.note = note;
    }

    public void setPoints(String points) {
        this.points = points;
    }

}
