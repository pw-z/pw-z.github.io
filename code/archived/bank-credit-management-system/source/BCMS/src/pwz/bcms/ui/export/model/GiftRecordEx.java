package pwz.bcms.ui.export.model;

/**
 * 用于Excel导出的po
 */
public class GiftRecordEx implements Comparable<GiftRecordEx> {

    private String name; //礼品名称
    private Integer number; //数量

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
    }

    @Override
    public int compareTo(GiftRecordEx o) {
        return o.getNumber() - this.number ;   // 根据积分总数降序排列，升序修改相减顺序即可
    }
}
