/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SDEV425_HW4;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import org.apache.derby.jdbc.ClientDataSource;

/**
 *
 * @author jim
 */
public class Authenticate extends HttpServlet {

    // variables    
    private String username;
    private String pword;
    private Boolean isValid;
    private int user_id;
    private HttpSession session;

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet Authenticate</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet Authenticate at " + request.getContextPath() + "</h1>");
            out.println("<h1>Results are " + username + "," + isValid + "</h1>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Get the post input 
        this.username = request.getParameter("emailAddress");
        this.pword = request.getParameter("pfield");
        this.isValid = validate(this.username, this.pword);
         response.setContentType("text/html;charset=UTF-8");
        // Set the session variable
        if (isValid) {
            // Create a session object if it is already not  created.
            session = request.getSession(true);
            session.setAttribute("UMUCUserEmail", username);         
            session.setAttribute("UMUCUserID", user_id);

            // Send to the Welcome JSP page              
            RequestDispatcher dispatcher = request.getRequestDispatcher("welcome.jsp");
            dispatcher.forward(request, response);

        } else {
            // Not a valid login
            // refer them back to the Login screen
            request.setAttribute("ErrorMessage", "Invalid Username or Password. Try again."); //Take Contact Jim out!
            RequestDispatcher dispatcher = request.getRequestDispatcher("login.jsp");
            dispatcher.forward(request, response);
        }
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

    // Method to Authenticate
    public boolean validate(String name, String pass) {
        boolean status = false;
        // int hitcnt=0; <-- Not used anymore!!!!

        try {
            ClientDataSource ds = new ClientDataSource();
            ds.setDatabaseName(getServletContext().getInitParameter("DB_NAME"));
            ds.setServerName(getServletContext().getInitParameter("DB_SERVER"));
            ds.setPortNumber(Integer.parseInt(getServletContext().getInitParameter("DB_PORT")));
            ds.setUser(getServletContext().getInitParameter("DB_USER"));
            ds.setPassword(getServletContext().getInitParameter("DB_PASSWORD"));
            ds.setDataSourceName("jdbc:derby");

            Connection conn = ds.getConnection();

            // Use PreparedStatement to prevent SQL injection
            // First query to get user_id
            String sql = "SELECT user_id FROM sdev_users WHERE email = ?";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, this.username);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                user_id = rs.getInt("user_id");

                // Second query to verify password
                String sql2 = "SELECT user_id FROM user_info WHERE user_id = ? AND password = ?";
                PreparedStatement pstmt2 = conn.prepareStatement(sql2);
                pstmt2.setInt(1, user_id);
                pstmt2.setString(2, this.pword);
                ResultSet rs2 = pstmt2.executeQuery();

                // Should be using some sort of hashing!!!!!! 
                // Database is plain text so check is plain text.
                if (rs2.next()) {
                    status = true;
                }
            }

            } catch (NumberFormatException | SQLException e) {
                System.out.println(e);
        }
    return status;
    }
}
