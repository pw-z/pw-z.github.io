package pwz.bcms.ui.main;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.control.Tab;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;

import java.io.IOException;
import java.net.URL;

public class MainController {

    //五个菜单
    @FXML
    public Tab csrManageTab;//客户管理
    public Tab pointsManageTab;//客户积分管理
    public Tab productsManageTab;//积分产品管理
    public Tab giftsManageTab;//礼品管理
    public Tab exportTab;//报表导出
    public Tab aboutTap;//关于
    public Tab welcomeTab; //欢迎页（首页）
    public AnchorPane welcomePane;
    public Tab settingTab; //设置页

    private Boolean isFirstIn = true;

    public MainController(){
    }

    public void loadCsrManageTab(){
        ((VBox) csrManageTab.getContent()).getChildren().clear();
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/csrmanage/csrManageTab.fxml");
        fxmlLoader.setLocation(url);
        Parent root = null;
        try {
            root = fxmlLoader.load();
        } catch (IOException e) {
            e.printStackTrace();
        }
        ((VBox) csrManageTab.getContent()).getChildren().add(root);
    }

    public void loadWelcomeTab(){
        ((VBox) welcomeTab.getContent()).getChildren().clear();
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/welcome/welcomeTab.fxml");
        fxmlLoader.setLocation(url);
        Parent root = null;
        try {
            root = fxmlLoader.load();
        } catch (IOException e) {
            e.printStackTrace();
        }
        ((VBox) welcomeTab.getContent()).getChildren().add(root);
    }
    public void loadGiftsManageTab(){
        ((VBox) giftsManageTab.getContent()).getChildren().clear();//清理之前的旧组件（回收、刷新）
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/giftsmanage/giftsManageTab.fxml");
        fxmlLoader.setLocation(url);
        Parent root = null;
        try {
            root = fxmlLoader.load();
        } catch (IOException e) {
            e.printStackTrace();
        }
        ((VBox) giftsManageTab.getContent()).getChildren().add(root);
    }
    public void loadProductsManageTab(){
        ((VBox) productsManageTab.getContent()).getChildren().clear();//清理之前的旧组件（回收、刷新）
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/productsmanage/productsManageTab.fxml");
        fxmlLoader.setLocation(url);
        Parent root = null;
        try {
            root = fxmlLoader.load();
        } catch (IOException e) {
            e.printStackTrace();
        }
        ((VBox) productsManageTab.getContent()).getChildren().add(root);
    }
    public void loadPointsManageTab(){
        ((VBox) pointsManageTab.getContent()).getChildren().clear(); //清理之前的旧组件（回收、刷新）
        FXMLLoader fxmlLoader = new FXMLLoader();
        URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/pointsmanage/pointsManageTab.fxml");
        fxmlLoader.setLocation(url);
        Parent root = null;
        try {
            root = fxmlLoader.load();
        } catch (IOException e) {
            e.printStackTrace();
        }
        ((VBox) pointsManageTab.getContent()).getChildren().add(root);
    }


    /**
     * 菜单按钮监听器
     * @throws IOException
     */
    public void myListener() throws IOException {

        //如果是刚刚打开软件，默认开启欢迎界面
        if (isFirstIn){
            loadWelcomeTab();
            isFirstIn = false;
        }

        welcomeTab.selectedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) welcomeTab.getContent()).getChildren().clear();
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/welcome/welcomeTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) welcomeTab.getContent()).getChildren().add(root);
            }
        });

        settingTab.selectedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) settingTab.getContent()).getChildren().clear();
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/setting/changePassword.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) settingTab.getContent()).getChildren().add(root);
            }
        });  //√

        csrManageTab.selectedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) csrManageTab.getContent()).getChildren().clear();
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/csrmanage/csrManageTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) csrManageTab.getContent()).getChildren().add(root);
            }
        });

        giftsManageTab.selectedProperty().addListener(new ChangeListener<Boolean>(){
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) giftsManageTab.getContent()).getChildren().clear();//清理之前的旧组件（回收、刷新）
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/giftsmanage/giftsManageTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) giftsManageTab.getContent()).getChildren().add(root);
            }
        });

        productsManageTab.selectedProperty().addListener(new ChangeListener<Boolean>(){
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) productsManageTab.getContent()).getChildren().clear(); //清理之前的旧组件（回收、刷新）
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/productsmanage/productsManageTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) productsManageTab.getContent()).getChildren().add(root);
            }
        });

        pointsManageTab.selectedProperty().addListener(new ChangeListener<Boolean>(){
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) pointsManageTab.getContent()).getChildren().clear(); //清理之前的旧组件（回收、刷新）
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/pointsmanage/pointsManageTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) pointsManageTab.getContent()).getChildren().add(root);

            }
        });

        exportTab.selectedProperty().addListener(new ChangeListener<Boolean>(){
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) exportTab.getContent()).getChildren().clear(); //清理之前的旧组件（回收、刷新）
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/export/exportTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) exportTab.getContent()).getChildren().add(root);

            }
        });


        aboutTap.selectedProperty().addListener(new ChangeListener<Boolean>(){
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {
                ((VBox) aboutTap.getContent()).getChildren().clear(); //清理之前的旧组件（回收、刷新）
                FXMLLoader fxmlLoader = new FXMLLoader();
                URL url = fxmlLoader.getClassLoader().getResource("pwz/bcms/ui/about/aboutTab.fxml");
                fxmlLoader.setLocation(url);
                Parent root = null;
                try {
                    root = fxmlLoader.load();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ((VBox) aboutTap.getContent()).getChildren().add(root);
            }
        });  //√
    }

}
