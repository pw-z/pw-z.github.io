package pwz.bcms.util;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;


/**
 * 较严格的校验工具
 */
public class IdentityUtils {

    /** 身份证号码格式校验
     *
     * 参考博客： https://blog.csdn.net/qq_35484410/article/details/90234651
     *
     * 1、号码的结构
     * 公民身份号码是特征组合码，由十七位数字本体码和一位校验码组成。从左至右依次为：六位数字地址码，
     * 八位数字出生日期码，三位数字顺序码和一位数字校验码。
     * 2、地址码(前六位数）
     * 表示编码对象常住户口所在县(市、旗、区)的行政区划代码，按GB/T2260的规定执行。
     * 3、出生日期码（第七位至十四位）
     * 表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。
     * 4、顺序码（第十五位至十七位）
     * 表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，
     * 顺序码的奇数分配给男性，偶数分配给女性。
     * 5、校验码（第十八位数）
     * （1）十七位数字本体码加权求和公式 S = Sum(Ai Wi), i = 0, , 16 ，先对前17位数字的权求和 ;
     * Ai:表示第i位置上的身份证号码数字值; Wi:表示第i位置上的加权因子 Wi: 7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2
     * （2）计算模 Y = mod(S, 11)
     * （3）通过模( 0 1 2 3 4 5 6 7 8 9 10)得到对应的校验码 Y:1 0 X 9 8 7 6 5 4 3 2
     *
     */
    // 身份证校验码
    private static final int[] COEFFICIENT_ARRAY = {7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2};
    // 身份证号的尾数规则
    private static final String[] IDENTITY_MANTISSA = {"1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"};
    private static final String IDENTITY_PATTERN = "^[0-9]{17}[0-9Xx]$";
    public static boolean isLegalIDNumber(String identity) {
        if (identity == null) {
            return false;
        }
        if (identity.length() != 18) {
            return false;
        }
        if (!identity.matches(IDENTITY_PATTERN)) {
            return false;
        }
        char[] chars = identity.toCharArray();
        long sum = IntStream.range(0, 17).map(index -> {
            char ch = chars[index];
            int digit = Character.digit(ch, 10);
            int coefficient = COEFFICIENT_ARRAY[index];
            return digit * coefficient;
        }).summaryStatistics().getSum();

        // 计算出的尾数索引
        int mantissaIndex = (int) (sum % 11);
        String mantissa = IDENTITY_MANTISSA[mantissaIndex];

        String lastChar = identity.substring(17);
        if (lastChar.equalsIgnoreCase(mantissa)) {
            return true;
        } else {
            return false;
        }
    }


    /** 手机号格式校验
     *
     * 参考博客：https://www.cnblogs.com/wangzn/p/7212587.html
     *          https://www.cnblogs.com/go4mi/p/6426215.html
     *          https://www.cnblogs.com/haoyul/p/9701085.html
     *
     * 运营商号段如下：
     * 中国联通号码：130、131、132、145（无线上网卡）、155、156、185（iPhone5上市后开放）、186、176（4G号段）、
     *               175（2015年9月10日正式启用，暂只对北京、上海和广东投放办理）
     * 中国移动号码：134、135、136、137、138、139、147（无线上网卡）、150、151、152、157、158、159、182、183、187、188、178
     * 中国电信号码：133、153、180、181、189、177、173、149 虚拟运营商：170、1718、1719
     * 手机号前3位的数字包括：
     * 1 :1
     * 2 :3,4,5,7,8
     * 3 :0,1,2,3,4,5,6,7,8,9
     * 总结： 目前java手机号码正则表达式有：
     * a :"^1[3|4|5|7|8][0-9]\\d{4,8}$"    一般验证情况下这个就可以了
     * b :"^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(17[013678])|(18[0,5-9]))\\d{8}$"
     * Pattern和Matcher详解（字符串匹配和字节码）http://blog.csdn.net/u010700335/article/details/44616451
     *
     */
    public static boolean isLegalPhoneNumber(String identity){
        String phone = identity;
        String regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(17[013678])|(18[0,5-9]))\\d{8}$";
        if(phone.length() != 11){
            System.out.println("手机号应为11位数");
            return false;
        }else{
            Pattern p = Pattern.compile(regex);
            Matcher m = p.matcher(phone);
            boolean isMatch = m.matches();
            if(isMatch){
                return true;
            } else {
                return false;
            }
        }
    }
    /** 补充说明
     * Pattern类用于创建一个正则表达式,生成一个Pattern对象并且编译一个正则表达式,也可以说创建一个匹配模式,
     * 它的构造方法是私有的,不可以直接创建,    但可以通过Pattern.complie(String regex)简单工厂方法创建一个正则表达式,
     * 轮到Matcher类登场了,Pattern.matcher(CharSequence input)返回一个Matcher对象.
     *
     *  Matcher类的构造方法也是私有的,不能随意创建,只能通过Pattern.matcher(CharSequence input)方法得到该类的实例
     *  String.matches() 这个方法主要是返回是否匹配指定的字符串，如果匹配则为true,否则为false;
     */


    /** 客户积分管理页面所需要的：账号校验
     *
     * 账号分两种：
     * 1. 普通账号全部为数字，长度 17位 或 18位
     * 2. 拥有子账户的账号：
     *      格式：  【普通账号 - 子账号】  ，中间是一短横线
     *      长度：   （9|18）+ 3
     */
    public static boolean isLegalAccount(String identity){
        String account = identity;
        String regex = "^((\\d{17})|(\\d{18})|(\\d{9}-\\d{3})|(\\d{18}-\\d{3}))$";

        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(account);
        boolean isMatch = m.matches();
        if(isMatch){
            return true;
        } else {
            return false;
        }

    }









}
