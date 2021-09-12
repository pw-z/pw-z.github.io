package pwz.bcmslg.main;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.paint.Color;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;
import javafx.util.StringConverter;

import java.io.File;
import java.net.URL;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ResourceBundle;

public class MainController implements Initializable {

    @FXML
    public TextField cpuCode;  //机器码
    public TextArea licenseCode;
    public Button generateButton; //导出许可证按钮
    public DatePicker tlimit; //截止日期
    public Label warning; //底部提示信息
    public Button chooseFolderButton; //选择保存路径
    public TextField savePath; //许可证导出路径

    //日期格式 ： 年月日
    private final String pattern = "yyyy-MM-dd";

    //申请码 = CPU码 + 截止时间
    private static String licensestatic ;

    //RSA私钥
    private static final String publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCnl0r9Q3Il4WOBFmCUWYS+B2Bu2eTbhB+LRrK\n" +
            "We6gMPT2ZCVqyn4RMoRLCyOO8YZGNkA8RpmIJnaqyZvCtPTPSYNkJoDIbdHQqZEjI+wb1TyXpPp7\n" +
            "C1hiFnZ21bE41oitzTTEtj3g1Zsyw+rg8j/o/82iasFtupZ8NqJuOujGEwIDAQAB";

    //RSA公钥
    public static final String privateKey = "MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIKeXSv1DciXhY4EWYJRZhL4HYG7\n" +
            "Z5NuEH4tGspZ7qAw9PZkJWrKfhEyhEsLI47xhkY2QDxGmYgmdqrJm8K09M9Jg2QmgMht0dCpkSMj\n" +
            "7BvVPJek+nsLWGIWdnbVsTjWiK3NNMS2PeDVmzLD6uDyP+j/zaJqwW26lnw2om466MYTAgMBAAEC\n" +
            "gYAfAQAUowI2juDAqP+mEzQrZIF8fcNEF2gKyyIEzfv6QiSjJ3pKMu5hnqAQQACcuW+p0s7Ef+2J\n" +
            "h7e7Kkeym8lP48/EZDWwjmO0BCG0ZllbFlSVzWxAsLLm8aAYNSCvFYKTOVR6fAyqSzI+L3klSUGU\n" +
            "R0zPfZRygBCOG/3hBii4wQJBALcfqgPCk6iDNJac129buvlnV6XKMIxMDisg1yG/T/CuDsP1PJHw\n" +
            "LHspoYt+x86O0QcoiJrGjyRKMoI+x2fBQDkCQQC2mZHqfiTnuuu6IDGBY0NweZ323FPDHqIttB7t\n" +
            "AIURiR2fVoIklLFktClAdtDBoPDbEiE2JN2XXeTIiEznqeCrAkALvnkd0p27oeZ+fkKGvsBH/Guv\n" +
            "kz730GzcMTf6zxUmX1NNF+4xgdCoeWwF0TSpN5mKNvxDyNYnQqbomXQaYFdpAkBlFiVCdK0HoGJJ\n" +
            "evMNFx/Jj3pUpGq2lSnhNVr9h5EjQQ4mHKUVjT+baWWA64Xr+6X7EVFTgRsvZep23YX9pfzbAkA6\n" +
            "3kw6bbXjKtfW/Ovy/NE9Ecnn6VoWa/IvqL7+EXcO4ITTQlfRil5LwEU3gkzH+yD1LGazNPDcMM5x\n" +
            "0NaC83PI";


    @Override
    public void initialize(URL location, ResourceBundle resources) {
        tlimit.setShowWeekNumbers(false);
        StringConverter converter = new StringConverter<LocalDate>() {
            DateTimeFormatter dateFormatter =
                    DateTimeFormatter.ofPattern(pattern);
            @Override
            public String toString(LocalDate date) {
                if (date != null) {
                    return dateFormatter.format(date);
                } else {
                    return "";
                }
            }
            @Override
            public LocalDate fromString(String string) {
                if (string != null && !string.isEmpty()) {
                    return LocalDate.parse(string, dateFormatter);
                } else {
                    return null;
                }
            }
        };
        tlimit.setConverter(converter);
        tlimit.setPromptText(pattern.toLowerCase());
        generateButton.setDisable(true);

        myListener();
    }



    @FXML
    public void generateLicenseCode(ActionEvent event) throws Exception {
        warning.setText("");
        if (checkInput()){
            licensestatic = cpuCode.getText() + ";" + tlimit.getValue().format(DateTimeFormatter.ofPattern("yyyyMMdd"));
            byte[] data = licensestatic.getBytes();
            byte[] encodedData = RSAUtils.encryptByPrivateKey(data, privateKey);
            try {
                //窗口显示加密后的密文
                licenseCode.setText(new String(encodedData));
                //生成许可文件 license.dat
                Base64Utils.byteArrayToFile(encodedData, savePath.getText() + File.separator + cpuCode.getText()+"license.dat");
                warning.setTextFill(Color.GREEN);
                warning.setText("成功");
            }catch (Exception ex){
                warning.setTextFill(Color.RED);
                warning.setText("失败：" + ex.toString());
            }

            //测试输出
            byte[] decodedData = RSAUtils.decryptByPublicKey(encodedData, publicKey);
            String target = new String(decodedData);
            System.out.println("原文：" + licensestatic);
            System.out.println("RAS私钥加密后："+ new String(encodedData));
            System.out.println("RSA公钥解密后：" + target);
            System.out.println("license.dat：\r\n" + savePath.getText() + File.separator + "license.dat");

        }
    }

    /**
     * 选择日期之后激活生成按钮
     */
    public void myListener(){
        tlimit.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                generateButton.setDisable(false);
            }
        });
    }


    /**
     * 检查输入
     * @return
     */
    private boolean checkInput(){
        if (cpuCode.getText().isEmpty()){
            warning.setTextFill(Color.RED);
            warning.setText("未输入申请码");
            return false;
        } else if (savePath.getText().isEmpty()) {
            warning.setTextFill(Color.RED);
            warning.setText("未选择路径");
            return false;
        } else {
            return true;
        }
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


}
