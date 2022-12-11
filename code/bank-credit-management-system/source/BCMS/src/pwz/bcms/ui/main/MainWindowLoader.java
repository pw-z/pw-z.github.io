package pwz.bcms.ui.main;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.util.LicenseCheckUtils;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.TabPane;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

import java.io.IOException;
import java.net.URL;
import java.sql.DriverManager;
import java.sql.SQLException;


/***
 * 主窗口加载器
 */
public class MainWindowLoader {

    public static MainController mainController =null;

    public void mainLoad(Stage primaryStage) throws IOException {

        /***
         * 导航栏主菜单按钮组（常驻根节点）
         * 总共6个按钮 对应功能区6种界面
         */
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url1 = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/main/mainWindow.fxml");
        fxmlLoader.setLocation(url1);
        TabPane root = fxmlLoader.load();//导航栏主菜单
        Scene scene = new Scene(root);

        //添加样式表
        scene.getStylesheets().add("/pwz/bcms/css/bcms-style.css");

        if (LicenseCheckUtils.checkInfo()!=1){
            primaryStage.setTitle("XXX银行积分管理系统 (未注册)");
        }else {
            primaryStage.setTitle("XXX银行积分管理系统");
        }
        primaryStage.setScene(scene);
        //primaryStage.setResizable(false);//不可伸缩，窗口大小固定
        primaryStage.show();

        mainController = (MainController)fxmlLoader.getController();
        mainController.myListener();

        //关闭程序，关闭数据库连接
        primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            @Override
            public void handle(WindowEvent event) {
//                System.out.println("DatabaseHandler.getConnection()!=null 需要关闭");
                if (DatabaseHandler.getConnection()!=null){
                    try {
                        DatabaseHandler.getConnection().close();
                        DriverManager.getConnection("jdbc:derby:;shutdown=true");
                    } catch (SQLException e) {
                        //e.printStackTrace();
                        if (((e.getErrorCode() == 50000) && ("XJ015".equals(e
                                .getSQLState())))) {
                            // we got the expected exception
                            System.out.println("Derby shut down normally");
                            // Note that for single database shutdown, the expected
                            // SQL state is "08006", and the error code is 45000.
                        } else {
                            System.err.println("Derby did not shut down normally");
                        }
                    }
                }else {
//                    System.out.println("DatabaseHandler.getConnection()==null  数据库连接不存在");
                }
                System.exit(0);
            }
        });
    }


    public static MainController getMainController() {
        if (mainController == null) {
            mainController = new MainController();
        }
        return mainController;
    }

}


