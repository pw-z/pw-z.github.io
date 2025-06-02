package pwz.bcms.util;

import pwz.bcms.util.rsa.Base64Utils;
import pwz.bcms.util.rsa.FileUtil;
import pwz.bcms.util.rsa.RSAUtils;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class LicenseCheckUtils {

    //RSA公钥
    private static final String publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCnl0r9Q3Il4WOBFmCUWYS+B2Bu2eTbhB+LRrK\n" +
            "We6gMPT2ZCVqyn4RMoRLCyOO8YZGNkA8RpmIJnaqyZvCtPTPSYNkJoDIbdHQqZEjI+wb1TyXpPp7\n" +
            "C1hiFnZ21bE41oitzTTEtj3g1Zsyw+rg8j/o/82iasFtupZ8NqJuOujGEwIDAQAB";


    /**
     * 注册信息检查
     * @return 0 ： 证书不存在   1：证书没问题  2： 非本机器的证书  3：证书已过期  4：证书格式有误
     */
    public static int checkInfo() throws StringIndexOutOfBoundsException{

        byte[] encodedData;  //从许可证中读取到的密文
        byte[] decodedData;  //从许可证中解码出的明文
        String cpuCode;  //机器码
        String tlimit; //截止日期
        String licensePath = FileUtil.getBasePath()+ File.separator+"license"+File.separator+"license.dat";

        //先判断许可证是否存在
        File licenseFile = new File(licensePath);
        if(!licenseFile.exists()) {
            System.out.println("许可证文件不存在");
            return 0;
        }
        //判断许可证是否过期
        try {
            //从安装根目录下的license文件夹中寻找license.dat
            encodedData  = Base64Utils.fileToByte(FileUtil.getBasePath()+ File.separator+"license"+File.separator+getCPUCode()+"license.dat");
            //System.out.println("获取到的密文："+new String(encodedData));
            //使用公钥解码license.dat中的密文
            decodedData = RSAUtils.decryptByPublicKey(encodedData,publicKey);
            //System.out.println("使用公钥解密得到明文："+new String(decodedData));
            //分割明文： 机器码 + 截止日期
            String tempString = new String(decodedData);
            cpuCode = tempString.substring(0,tempString.indexOf(";"));
            tlimit = tempString.substring(tempString.indexOf(";")+1);
            //验证机器
            if (getCPUCode().equals(cpuCode)){
                //当前时间
                Date now = new Date();
                SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd");//设置日期格式
                String createTime = dateFormat.format(now);//格式化然后放入字符串中
                //比较当前时间与证书中的时间
                if(createTime.compareTo(tlimit) < 0){
                    return 1;//证书没问题
                }else {
                    return 3;//许可证已过期
                }
            }else {
                return 2;//非本机器的证书
            }
        } catch (Exception e) {
            e.printStackTrace();
            return 4;//证书格式有误
        }
    }
    public static int checkInfoWithPath(String filePath) {

        byte[] encodedData;  //从许可证中读取到的密文
        byte[] decodedData;  //从许可证中解码出的明文
        String cpuCode;  //机器码
        String tlimit; //截止日期
        String licensePath = filePath;

        //先判断许可证是否存在
        File licenseFile = new File(licensePath);
        if(!licenseFile.exists()) {
            //System.out.println("许可证文件不存在");
            return 0;
        }
        //判断许可证是否过期
        try {
            //从安装根目录下的license文件夹中寻找license.dat
            encodedData  = Base64Utils.fileToByte(licensePath);
            //System.out.println("获取到的密文："+new String(encodedData));
            //使用公钥解码license.dat中的密文
            decodedData = RSAUtils.decryptByPublicKey(encodedData,publicKey);
            //System.out.println("使用公钥解密得到明文："+new String(decodedData));
            //分割明文： 机器码 + 截止日期
            String tempString = new String(decodedData);
            cpuCode = tempString.substring(0,tempString.indexOf(";"));
            tlimit = tempString.substring(tempString.indexOf(";")+1);
            //验证机器
            if (getCPUCode().equals(cpuCode)){
                //当前时间
                Date now = new Date();
                SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd");//设置日期格式
                String createTime = dateFormat.format(now);//格式化然后放入字符串中
                //比较当前时间与证书中的时间
                if(createTime.compareTo(tlimit) < 0){
                    return 1;//证书没问题
                }else {
                    return 3;//许可证已过期
                }
            }else {
                return 2;//非本机器的证书
            }
        } catch (Exception e) {
            e.printStackTrace();
            return 4;//证书格式有误
        }
    }



    public static void main(String[] args) {
        System.out.println(checkInfo());
    }

    /**
     * 获取CPU码，（不是从文件中获取，是直接从电脑得到，用于验证或者申请证书）
     * https://blog.csdn.net/zhangdaiscott/article/details/74345501
     *
     * CPU都有一个唯一的ID号，称CPUID，是在制造CPU的时候，由厂家置入到CPU内部的
     * 使用cmd输入wmic CPU get ProcessorID ，就可以得到ID
     *
     * 由于CPU外在的所有标记、符号，都是可以人为打磨，而CPUID却是终身不变的，只能用软件读出ID号；
     * 因此，利用这个原理，CPU ID工具可以显出CPU的确切信息，包括移动版本、主频、外频、二级缓存等关键信息，从而查出超频的CPU，并且醒目地显示出来。
     * @return serial CUP码    出错：返回空串
     */
    public static String getCPUCode(){
        try {
            //long start = System.currentTimeMillis();
            Process process = Runtime.getRuntime().exec(
                    new String[] { "wmic", "cpu", "get", "ProcessorId" });  //在单独的进程中执行指定的字符串命令。
            process.getOutputStream().close(); //关闭子进程的输出流
            Scanner sc = new Scanner(process.getInputStream()); //获取子进程的输入流
            String property = sc.next();
            String serial = sc.next();  //CPU码
            //System.out.println(property + ": " + serial);
            //System.out.println("time:" + (System.currentTimeMillis() - start));
            return serial;
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            return "";
        }
    }

    /**
     * 从证书文件中获取截止日期
     * 注意：要先确定证书文件存在再调用此方法
     * @return 证书截止日期
     */
    public static String getTLimit(){
        byte[] encodedData;  //从许可证中读取到的密文
        byte[] decodedData;  //从许可证中解码出的明文
        String tlimit; //截止日期
        try {
            //从安装根目录下的license文件夹中寻找license.dat
            encodedData  = Base64Utils.fileToByte(FileUtil.getBasePath()+ File.separator+"license"+File.separator+"license.dat");
            //使用公钥解码license.dat中的密文
            decodedData = RSAUtils.decryptByPublicKey(encodedData,publicKey);
            String tempString = new String(decodedData);
            tlimit = tempString.substring(tempString.indexOf(";")+1);
            return tlimit;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "";
    }
}
