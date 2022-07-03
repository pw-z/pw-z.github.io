package com.pwz.wiki.session_and_cookie.cookie;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/testCookie")
public class CookieDemo extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        // 获取cookie
        // 由于浏览器会将一个域下的所有cookie全部发送过来，需要遍历处理
        Cookie[] cookies = req.getCookies();
        for (Cookie cookie : cookies) {
            System.out.println(cookie.getName());
            System.out.println(cookie.getValue());
        }

        // 新建cookie并添加到响应中
        Cookie cookie = new Cookie("test_key", "test_value");
        resp.addCookie(cookie);
    }
}
