package pwz.bcms.ui.productsmanage;

import pwz.bcms.db.DatabaseHandler;
import pwz.bcms.db.ProductDataHelper;
import pwz.bcms.po.Product;
import pwz.bcms.ui.main.MainController;
import pwz.bcms.ui.main.MainWindowLoader;
import pwz.bcms.util.AccountValidatorUtil;
import pwz.bcms.util.AlertUtils;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.paint.Color;
import org.apache.commons.lang3.StringUtils;

import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class ProductsManageController implements Initializable {

    @FXML
    public TableView tableView;
    public TableColumn id;
    public TableColumn name;
    public TableColumn points;
    public TableColumn tlimit;
    public TableColumn flag;
    public TableColumn note;
    public TextField searchInfo; //搜索关键词：使用名称
    public Button searchButton;  //搜索按钮
    public Label searchWarning;


    @FXML
    public Button deleteButton;  //删除按钮，非编辑模式下不可用
    public Button saveButton;  //保存按钮，非编辑模式下不可用
    public Button manageButton;  // 编辑按钮，选中一项产品后可以编辑
    public Button newButton;  //新增产品信息
    public Button reloadButton;  //重置按钮

    @FXML
    public Group r_group;
    public Label r_noteLabel;
    public TextArea r_note;
    public ChoiceBox r_flag;
    public TextField r_tlimit;
    public TextField r_points;
    public TextField r_name;
    public Label r_idLabel;
    public TextField r_id;
    public Label r_warning;

    //自定义属性
    public static Product product = null;
    public static ProductDataHelper productDataHelper = null;
    ObservableList<Product> list = FXCollections.observableArrayList();//持久化数据列表
    Product newProduct = new Product();

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("---实例化---ProductsManageConrtoller---initialize");

        r_flag.getItems().addAll("是","否");
        r_flag.getSelectionModel().select("否");

        manageButton.setDisable(true);
        saveButton.setDisable(true);
        deleteButton.setDisable(true);
        initCol();
        loadData();
        myListener();
    }


    /**
     * 绑定工厂 ：用于支持实时排序
     * 动态设置TableView中的单元格
     */
    public void initCol() {
        id.setCellValueFactory(new PropertyValueFactory<>("id"));
        name.setCellValueFactory(new PropertyValueFactory<>("name"));
        points.setCellValueFactory(new PropertyValueFactory<>("points"));
        tlimit.setCellValueFactory(new PropertyValueFactory<>("tlimit"));
        flag.setCellValueFactory(new PropertyValueFactory<>("flag"));
        note.setCellValueFactory(new PropertyValueFactory<>("note"));
    }

    /**
     * Product(String id, String name, String points, String tlimit, String flag, String note)
     * 加载数据 （Gift）
     */
    public void loadData() {
        list.clear();

        DatabaseHandler handler = DatabaseHandler.getInstance();//拿到已经创建的实例引用 （最开始是在Main中的主函数里创建的）
        String qu = "SELECT * FROM PRODUCT";
        ResultSet rs = handler.execQuery(qu);
        try {
            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                String points = rs.getString("points");
                String tlimit = rs.getString("tlimit");
                String flag = rs.getString("flag");
                String note = rs.getString("note");
                list.add(new Product( id,  name,  points,  tlimit,  flag,  note));
            }
        } catch (SQLException ex) {
            System.err.println(ex + "------加载Tableview客户数据过程中的loadData()方法");
        }
        tableView.setItems(list);
    }


    /**
     * 监听选择客户：选中TableView的一行，并在界面右侧【信息处理区】显示
     */
    private void myListener(){

        tableView.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                //得到选择的产品
                Product selectedProduct = (Product)newValue;
                r_id.setText(selectedProduct.getId());
                r_name.setText(selectedProduct.getName());
                r_points.setText(selectedProduct.getPoints());
                r_tlimit.setText(selectedProduct.getTlimit());
                r_flag.getSelectionModel().select(selectedProduct.getFlag());
                r_note.setText(selectedProduct.getNote());

                //不点击编辑按钮，不可编辑
                for (Node node:r_group.getChildren()
                ) {
                    node.setDisable(true);
                }

                //每次新选中一条信息，退出编辑模式
                newButton.setDisable(true);
                manageButton.setDisable(false);
                saveButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
                deleteButton.setDisable(true);//默认状态下这个按钮不可用，点击编辑之后才可以
            }
        });
    }

    /**
     * 新增产品信息
     * @param event
     */
    @FXML
    public void newProduct(ActionEvent event) {

        r_warning.setText("");

        newProduct.setName(r_name.getText());
        newProduct.setPoints(r_points.getText());
        newProduct.setTlimit(r_tlimit.getText());
        newProduct.setFlag(r_flag.getSelectionModel().getSelectedItem().toString());
        newProduct.setNote(r_note.getText());

        if (checkInput(newProduct)){
            if (ProductDataHelper.insertNewProduct(newProduct)){
                //System.out.println("保存新【积分产品】信息成功");
                AlertUtils.newAlert();
                //新增产品之后刷新界面
                MainController mainController = MainWindowLoader.getMainController();
                mainController.loadProductsManageTab();

            }else {
                r_warning.setText("警告：该产品已在数据库中");
                //System.out.println("保存新【积分产品】信息失败");
            }
        }
    }


    /**
     * 进入编辑模式
     * @param event
     */
    @FXML
    public void manageProduct(ActionEvent event) {

        //不点击编辑按钮，不可编辑
        for (Node node:r_group.getChildren()
        ) {
            node.setDisable(false);
        }
        r_id.setDisable(true);
        r_noteLabel.setDisable(true);


        newButton.setDisable(true);
        saveButton.setDisable(false);
        deleteButton.setDisable(false);
    }

    /**
     * 编辑模式下：保存（更新）产品信息
     * @param event
     */
    public void saveProduct(ActionEvent event) {
        newProduct.setId(r_id.getText());
        newProduct.setName(r_name.getText());
        newProduct.setPoints(r_points.getText());
        newProduct.setTlimit(r_tlimit.getText());
        newProduct.setFlag(r_flag.getSelectionModel().getSelectedItem().toString());
        newProduct.setNote(r_note.getText());

        if (checkInput(newProduct)){
            if (ProductDataHelper.updateProduct(newProduct)){
//                System.out.println("修改产品信息成功");
                AlertUtils.editAlert();
                //保存产品信息之后刷新界面
                MainController mainController = MainWindowLoader.getMainController();
                mainController.loadProductsManageTab();

            }else {
//                System.out.println("修改产品信息失败");
                AlertUtils.editWrongAlert();
            }
        }
    }


    /**
     * 编辑模式下：删除一条（更新）产品信息
     * @param event
     */
    public void deleteProduct(ActionEvent event) {
        newProduct.setId(r_id.getText());
        if (ProductDataHelper.deleteProduct(newProduct)){
//            System.out.println("删除产品信息成功");
            AlertUtils.deleteAlert();
            //新增之后刷新界面
            MainController mainController = MainWindowLoader.getMainController();
            mainController.loadProductsManageTab();
        }else {
//            System.out.println("删除产品信息失败");
            AlertUtils.deleteWrongAlert();
        }
    }


    /**
     * 查询礼品信息：使用产品名称作为关键字
     * @param event
     */
    @FXML
    public void searchProduct(ActionEvent event) {

        r_id.setText("");
        r_name.setText("");
        r_points.setText("");
        r_tlimit.setText("");
        r_note.setText("");
        for (Node node:r_group.getChildren()
        ) {
            node.setDisable(false);
        }

        r_warning.setTextFill(Color.RED);
        r_warning.setText("");
        if ( searchInfo.getText().equals("") ){
            r_warning.setText("警告：请输入产品名称再进行搜索");
        }else {
            searchWarning.setText("");
            try {
                PreparedStatement statement = DatabaseHandler.getInstance().getConnection().prepareStatement(
                        "SELECT * FROM PRODUCT WHERE name = ? ");
                statement.setString(1,StringUtils.trimToEmpty(searchInfo.getText()));
                //System.out.println("使用产品名：" + searchInfo.getText() + "进行查询   - - - searchProduct");
                ResultSet rs = statement.executeQuery();

                while (rs.next()){  //查找结果是唯一的，此代码块只执行一次
                    System.out.println(rs.getString("name"));
                    String id = rs.getString("id");
                    String name = rs.getString("name");
                    String points = rs.getString("points");
                    String tlimit = rs.getString("tlimit");
                    String flag = rs.getString("flag");
                    String note = rs.getString("note");
                    Product selectedProduct = new Product(id, name,  points,  tlimit,  flag, note);


                    //在选中模式下选中TableView的一行，manageGift.fxml页面中显示
                    r_id.setText(selectedProduct.getId());
                    r_name.setText(selectedProduct.getName());
                    r_points.setText(selectedProduct.getPoints());
                    r_tlimit.setText(selectedProduct.getTlimit());
                    r_flag.getSelectionModel().select(selectedProduct.getFlag());
                    r_note.setText(selectedProduct.getNote());

                    r_warning.setTextFill(Color.GREEN);
                    r_warning.setText("查找成功");

                    //不点击编辑按钮，不可编辑
                    for (Node node:r_group.getChildren()
                    ) {
                        node.setDisable(true);
                    }
                    manageButton.setDisable(false);

                }
                if (!r_name.isDisable())r_warning.setText("警告：未查询到指定产品,请确认产品名称是否有误");

            } catch (SQLException ex) {
                System.err.println(ex.getMessage() + " - - - searchGift");
            }
        }

    }


    @FXML
    public void reloadTab(ActionEvent event) {
        MainController mainController = MainWindowLoader.getMainController();
        mainController.loadProductsManageTab();
    }

    /**
     * 输入检查
     * @param newProduct
     * @return
     */
    public boolean checkInput(Product newProduct){
        r_warning.setTextFill(Color.RED);

        //产品名称
        if (!AccountValidatorUtil.isUsername(newProduct.getName())){
            r_warning.setText("警告：产品名称有误");
            return false;
        }
        //单位产品积分数
        if (!AccountValidatorUtil.isNumber(newProduct.getPoints())) {
            r_warning.setText("警告：单位产品积分数格式有误");
            return false;
        }

        //产品期限
        if (!AccountValidatorUtil.isNumber(newProduct.getTlimit())){
            r_warning.setText("警告：产品期限格式有误");
            return false;
        }else {
            return true;
        }
    }

}
