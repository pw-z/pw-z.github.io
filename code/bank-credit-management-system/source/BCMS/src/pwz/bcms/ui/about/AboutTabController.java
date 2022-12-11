package pwz.bcms.ui.about;


import pwz.bcms.util.LicenseCheckUtils;
import pwz.bcms.util.rsa.Base64Utils;
import pwz.bcms.util.rsa.FileUtil;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.net.URL;
import java.util.ResourceBundle;

public class AboutTabController implements Initializable {

    @FXML
    public TextField cpuCode;
    public Button chooseFileButton;
    public TextField filePath;
    public Button getCPUCodeButton;
    public Button inputLicenseButton; //注册按钮
    public Label warning;
    public TextArea licenseInfo;
    public boolean isFileChosen=false;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        warning.setTextFill(Color.RED);
        try {
            initLicenseInfo();
        } catch (Exception e) {
            e.printStackTrace();
        }

        cpuCode.setText(LicenseCheckUtils.getCPUCode());
    }

    /**
     * 加载关于面板的注册信息
     */
    private void initLicenseInfo() throws Exception {
        int licenseStatus = LicenseCheckUtils.checkInfo();
        switch (licenseStatus){
            case 0://证书不存在
                licenseInfo.setText("证书不存在");
                break;
            case 1:{//证书没问题
                licenseInfo.setText("已注册\n\n\r" + "截止日期：" + LicenseCheckUtils.getTLimit());
                break;
            }
            case 2://非本机器的证书
                licenseInfo.setText("非本机器的证书");
                break;
            case 3://证书已过期
                licenseInfo.setText("证书已过期");
                break;
            case 4://证书格式有误
                licenseInfo.setText("证书格式有误");
                break;
        }

    }



    /**
     * 选择路径
     * @param event
     */
    @FXML
    public void chooseFile(ActionEvent event) {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("选择许可证文件：license.dat");
        fileChooser.getExtensionFilters().addAll(new FileChooser.ExtensionFilter("License Files", "*.dat"), new FileChooser.ExtensionFilter("All Files", "*.*"));
        File file = fileChooser.showOpenDialog(new Stage());
        if (file != null) {
            //将选取文件的绝对路径显示在面板上
            filePath.setText(file.getAbsolutePath());
             //System.out.println(file.getAbsolutePath());
            isFileChosen=true;
        }else {
            isFileChosen=false;
        }
    }

    @FXML
    /**
     * 获取机器码（作为申请码）
     */
    public void getCPUCode(ActionEvent event) {
        cpuCode.setText(LicenseCheckUtils.getCPUCode());
    }

    /**
     * 使用许可证文件进行注册
     * @param event
     */
    public void inputLicense(ActionEvent event) {
        //licenseInfo.setText("");
        //TODO 先验证是否选择了许可证文件
        //0 ： 证书不存在   1：证书没问题  2： 非本机器的证书  3：证书已过期  4：证书格式有误
        int licenseStatus = LicenseCheckUtils.checkInfoWithPath(filePath.getText()); //用户选择的许可证路径

        if (isFileChosen){//如果选择了证书文件，开始验证
            switch (licenseStatus){
                case 0://证书不存在
                    warning.setText("证书不存在");
                    break;
                case 1:{//证书没问题
                    warning.setTextFill(Color.GREEN);
                    warning.setText("证书没问题");
                    //导入证书到安装目录
                    try {
                        byte[] encodedData;
                        //从安装根目录下的license文件夹中寻找license.dat
                        encodedData  = Base64Utils.fileToByte(filePath.getText());
                        //System.out.println(new String(encodedData));
                        //System.out.println(FileUtil.getBasePath()+ File.separator+"license"+File.separator+"license.dat");
                        Base64Utils.byteArrayToFile(encodedData, FileUtil.getBasePath()+ File.separator+"license"+File.separator+ LicenseCheckUtils.getCPUCode()+"license.dat");
                        //验证是否注册成功
                        String licensePath = FileUtil.getBasePath()+ File.separator+"license"+File.separator+"license.dat"; //默认安装许可证路径
                        File licenseFile = new File(licensePath);
                        if(licenseFile.exists()) {
                            warning.setTextFill(Color.GREEN);
                            warning.setText("注册成功");
                            ((Stage)inputLicenseButton.getScene().getWindow()).setTitle("XXX银行积分管理系统");
                            initLicenseInfo();
                        }else {
                            warning.setTextFill(Color.RED);
                            warning.setText("未知错误");
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                }
                case 2://非本机器的证书
                    warning.setText("非本机器的证书");
                    break;
                case 3://证书已过期
                    warning.setText("证书已过期");
                    break;
                case 4://证书格式有误
                    warning.setText("证书格式有误");
                    break;
            }
        }else {
            warning.setText("请先选择证书文件");
        }


    }
}
