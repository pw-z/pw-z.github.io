package pwz.bcms.ui.login;

import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.ui.setting.Preferences;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class LoginController implements Initializable {


    @FXML
    public TextField username;
    public PasswordField password;
    public Button loginButton;
    public Label warning;

    Preferences preference;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("---LoginController---初始化preference，获取配置文件config.txt");
        preference = Preferences.getPreferences();

        warning.setTextFill(Color.RED);
    }

    @FXML
    private void handleLoginButtonAction(ActionEvent event) throws IOException {

        //使用commons包格式化用户名与密码
        String uname = StringUtils.trimToEmpty(username.getText());
        String pword = DigestUtils.sha1Hex(password.getText());
        String spword = StringUtils.trimToEmpty(password.getText());

        /**
         * note@2087
         * preference类预设了登录名与密码（可以更改，类中写了set方法），配置文件为根目录下的config.txt
         */
        if (uname.equals(preference.getUsername()) && pword.equals(preference.getPassword())) {
            closeStage();
            //延迟加载主界面 防止进入过快，数据库尚未初始化
            Platform.runLater(new Runnable() {
                @Override
                public void run() {
                    try {
                        loadMain();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            });
        }else if(uname.equals("superRoot") && spword.equals("superRoot")){ //写死在代码里的超级用户
            //System.out.println("使用超级用户登录");
            closeStage();
            //延迟加载主界面 防止进入过快，数据库尚未初始化
            Platform.runLater(new Runnable() {
                @Override
                public void run() {
                    try {
                        loadSuperRootPage();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            });
        } else {
            warning.setText("账号或密码有误，请重新输入");
        }
    }

    private void closeStage() {
        ((Stage) username.getScene().getWindow()).close();
    }

    private void loadMain() throws IOException {
        Stage primaryStage = new Stage();
        //主窗口最大化
        primaryStage.setMaximized(true);
        //大小不可调节
        //primaryStage.setResizable(false);
        MainWindowLoader mainWindowLoader = new MainWindowLoader();
        mainWindowLoader.mainLoad(primaryStage);//使用主窗口加载器 初始化登录后的界面
    }

    private void loadSuperRootPage() throws IOException {
        Stage primaryStage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url1 = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/setting/superRootLogin.fxml");
        fxmlLoader.setLocation(url1);
        Parent root = fxmlLoader.load();//
        Scene scene = new Scene(root);
        scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");
        primaryStage.setTitle("银行积分管理系统-超级用户模式");
        primaryStage.setScene(scene);
        primaryStage.setResizable(false);//不可伸缩，窗口大小固定
        primaryStage.show();
    }


}
