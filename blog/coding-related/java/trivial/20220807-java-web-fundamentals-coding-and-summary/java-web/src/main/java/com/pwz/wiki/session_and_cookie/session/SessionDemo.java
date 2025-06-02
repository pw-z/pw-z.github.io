package com.pwz.wiki.session_and_cookie.session;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/testSession")
public class SessionDemo extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        // 获取session对象，添加或者获取属性
        HttpSession session = req.getSession();
        session.setAttribute("test_key", "test_key");
        session.getAttribute("test_key");
    }
}
