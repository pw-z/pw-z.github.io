package pwz.bcms.ui.setting;

import com.google.gson.Gson;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Preferences {

    public static final String CONFIG_FILE = "config.txt";

//    int nDaysWithoutFine;
//    float finePerDay;
    String username;
    String password;

    public Preferences() {
//        nDaysWithoutFine = 14;
//        finePerDay = 2;
        username = "admin";
        setPassword("admin");
    }

//    public int getnDaysWithoutFine() {
//        return nDaysWithoutFine;
//    }
//
//    public void setnDaysWithoutFine(int nDaysWithoutFine) {
//        this.nDaysWithoutFine = nDaysWithoutFine;
//    }
//
//    public float getFinePerDay() {
//        return finePerDay;
//    }
//
//    public void setFinePerDay(float finePerDay) {
//        this.finePerDay = finePerDay;
//    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        if (password.length() < 16) {
            this.password = DigestUtils.sha1Hex(password);
        }else
            this.password = password;
    }

    //创建配置文件
    public static void initConfig() {
        Writer writer = null;
        try {
            Preferences preference = new Preferences();
            Gson gson = new Gson();
            writer = new FileWriter(CONFIG_FILE);
            gson.toJson(preference, writer);
        } catch (IOException ex) {
            Logger.getLogger(Preferences.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            try {
                writer.close();
            } catch (IOException ex) {
                Logger.getLogger(Preferences.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

    //获取配置文件 （没有则创建）
    public static Preferences getPreferences() {

        Gson gson = new Gson();
        Preferences preferences = new Preferences();
        try {
            preferences = gson.fromJson(new FileReader(CONFIG_FILE), Preferences.class);
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Preferences.class.getName()).info("Config file is missing. Creating new one with default config");
            initConfig();
        }
        return preferences;
    }

    //写入新配置
    public static void writePreferenceToFile(Preferences preference) {
        Writer writer = null;
        try {
            Gson gson = new Gson();
            writer = new FileWriter(CONFIG_FILE);
            gson.toJson(preference, writer);

        } catch (IOException ex) {
            Logger.getLogger(Preferences.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            try {
                writer.close();
            } catch (IOException ex) {
                Logger.getLogger(Preferences.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

}
