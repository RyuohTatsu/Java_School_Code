<%-- 
    Document   : welcome
    Created on : Nov 7, 2015, 10:20:47 AM
    Author     : jim
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link href="styles.css" rel="stylesheet" type="text/css">
        <title>Welcome</title>
    </head>
    <body>
        <div id="main">
            <%@include file="WEB-INF/jspf/menus.jspf" %> <!-- Includes navigation menu -->
            <p></p>
            <p></p>
            
            <!-- Retrieve and display user email -->
            <% 
            String User = (String) session.getAttribute("UMUCUserEmail");
            if (User == null) {
                response.sendRedirect("login.jsp"); // Redirect to login if session is not found
            }
            %>
            <h3>Hello <%= User %>!</h3>           
            
            <!-- Display error message if any -->
            <% 
            String e = (String) request.getAttribute("ErrorMessage");
            if (e != null) { 
                out.print("<h3>" + e + "</h3>");
            }
            %>

            <h3>Select from any of the menu items above.</h3>
            <table class="gridtable">
                <tr><th>Menu Item</th><th>Description</th></tr>
                <tr><td>Home</td><td>Return to the initial landing page.</td></tr>
                <tr><td>Sign-in</td><td>Sign in to the database.</td></tr>
                <tr><td>Your Account</td><td>Update your name and connection information.</td></tr>
                <tr><td>Sign-out</td><td>Sign out of the system. This invalidates your session.</td></tr>
            </table>
        </div>
    </body>
</html>