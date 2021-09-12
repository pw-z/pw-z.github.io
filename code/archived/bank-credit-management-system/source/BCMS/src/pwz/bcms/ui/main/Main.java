package pwz.bcms.ui.main;

import pwz.bcms.db.DatabaseHandler;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.net.URL;

/***
 * 主窗口负责登录过程
 * 登录成功之后调用 主窗口加载器，加载主界面
 */
public class Main extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception{


        //加载登陆页面
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/login/login.fxml");
        fxmlLoader.setLocation(url);
        Parent root = fxmlLoader.load();
        Scene scene = new Scene(root);
        scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");
        primaryStage.setScene(scene);
        primaryStage.setResizable(false);//不可伸缩，窗口大小固定
        primaryStage.show();
        primaryStage.setTitle("XXX银行积分管理系统 登录");



        /**
         * note@2087
         * 开启新的后台线程：()->{}为lamuda表达式，{}为可执行的语句块，大致相当于：
         * Thread t = new Thread(new DatabaseHandler.getInstance);
         * t.start();
         */
        new Thread(() -> {
            //System.out.println("新线程开启:初始化数据库中");
            DatabaseHandler.getInstance();
        }).start();

    }

}
