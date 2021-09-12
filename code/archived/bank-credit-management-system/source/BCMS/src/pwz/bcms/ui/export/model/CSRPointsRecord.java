package pwz.bcms.ui.export.model;


//报表导出，客户积分记录模型
public class CSRPointsRecord implements Comparable<CSRPointsRecord>{

    private String csr_name;
    private String gender;
    private String card_number;
    private String age;
    private Integer totalPoints;  //积分总数
    //private Integer pointsNotUse;  //未兑换积分
    //private Integer pointsUsed;  //已兑换积分


    @Override
    public int compareTo(CSRPointsRecord o) { //重写Comparable接口的compareTo方法，
        return o.getTotalPoints() - this.totalPoints ;   // 根据积分总数降序排列，升序修改相减顺序即可
    }

    public Integer getTotalPoints() {
        return totalPoints;
    }

    public void setTotalPoints(Integer totalPoints) {
        this.totalPoints = totalPoints;
    }


    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
//    public Integer getPointsNotUse() {
//        return pointsNotUse;
//    }
//
//    public void setPointsNotUse(Integer pointsNotUse) {
//        this.pointsNotUse = pointsNotUse;
//    }
//
//    public Integer getPointsUsed() {
//        return pointsUsed;
//    }
//
//    public void setPointsUsed(Integer pointsUsed) {
//        this.pointsUsed = pointsUsed;
//    }

    public String getCsr_name() {
        return csr_name;
    }

    public void setCsr_name(String csr_name) {
        this.csr_name = csr_name;
    }

    public String getCard_number() {
        return card_number;
    }

    public void setCard_number(String card_number) {
        this.card_number = card_number;
    }



}
