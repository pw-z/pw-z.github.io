package pwz.bcms.util;

import javafx.scene.control.Alert;

public class AlertUtils {

    //新增成功
    public static void newAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("新增成功");
        alert.showAndWait();
    }

    //修改成功
    public static void editAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("修改成功");
        alert.showAndWait();
    }

    //删除成功
    public static void deleteAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("删除成功");
        alert.showAndWait();
    }

    //新增失败
    public static void newWrongAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("新增失败");
        alert.showAndWait();
    }

    //修改失败
    public static void editWrongAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("修改失败");
        alert.showAndWait();
    }

    //删除失败
    public static void deleteWrongAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("删除失败");
        alert.showAndWait();
    }

    //查询完成
    public static void searchAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("查询完成");
        alert.showAndWait();
    }
    //查询结果为空
    public static void searchWrongAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("未查询到结果");
        alert.showAndWait();
    }

    //保存礼品兑换记录成功
    public static void saveGiftRecordAlert(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("提示");
        alert.setHeaderText(null);
        alert.setContentText("保存礼品兑换记录完成");
        alert.showAndWait();
    }

}
