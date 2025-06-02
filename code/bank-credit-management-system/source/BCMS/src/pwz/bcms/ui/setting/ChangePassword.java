package pwz.bcms.ui.setting;

import pwz.bcms.util.AccountValidatorUtil;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import org.apache.commons.codec.digest.DigestUtils;

public class ChangePassword {

    @FXML
    public TextField newUserName;
    public PasswordField newPassword;
    public PasswordField newPasswordCheck;
    public Button saveButton;
    public Label warning;
    public Button reloadButton;
    public PasswordField oldPassword;

    Preferences preference;

    @FXML
    public void handleSaveButtonAction(ActionEvent event) {
        warning.setTextFill(Color.RED);
        if (oldPassword.getText().isEmpty()){
            warning.setText("请输入旧密码");
        }else if (newPassword.getText().isEmpty()){
            warning.setText("请输入新密码");
        }else if (newPasswordCheck.getText().isEmpty()){
            warning.setText("请确认旧密码");
        }else {
            preference = Preferences.getPreferences();
            String uname = newUserName.getText();
            String pass = newPassword.getText();
            String pass_check = newPasswordCheck.getText();
            String oldpass = oldPassword.getText();
            if (AccountValidatorUtil.isUsername(uname)){
                if (!DigestUtils.sha1Hex(oldpass).equals(preference.getPassword())){
                    warning.setTextFill(Color.RED);
                    warning.setText("旧密码错误");
                }else {
                    if (pass.equals(pass_check)){
                        Preferences preferences = Preferences.getPreferences();
                        preferences.setUsername(uname);
                        preferences.setPassword(pass);
                        Preferences.writePreferenceToFile(preferences);

                        warning.setTextFill(Color.GREEN);
                        warning.setText("修改成功");

                        oldPassword.setText("");
                        newUserName.setText("");
                        newPassword.setText("");
                        newPasswordCheck.setText("");

                    }else {
                        warning.setTextFill(Color.RED);
                        warning.setText("两次密码不一致");
                    }
                }

            }else {
                warning.setTextFill(Color.RED);
                warning.setText("用户名格式有误");
            }
        }
    }

    public void handleReloadButtonAction(ActionEvent event) {
        oldPassword.setText("");
        newPassword.setText("");
        newPasswordCheck.setText("");
        warning.setText("");
    }
}
