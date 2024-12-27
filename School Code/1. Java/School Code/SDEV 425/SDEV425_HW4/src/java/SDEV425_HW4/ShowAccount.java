/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SDEV425_HW4;

import java.io.IOException;
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
 * Servlet to display user account details securely.
 */
public class ShowAccount extends HttpServlet {

    /**
    * Processes requests for both HTTP GET and POST methods.
    *
    * @param request  the HttpServletRequest object that contains the request the client has made to the servlet
    * @param response the HttpServletResponse object that contains the response the servlet sends to the client
    * @throws ServletException if an input or output error is detected when the servlet handles the request
    * @throws IOException if the request for the GET or POST could not be handled
    */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");

        // Check for an existing session without creating a new one
        HttpSession session = request.getSession(false); 
        if (session == null || session.getAttribute("UMUCUserEmail") == null) {
            // Redirect to login page if session is invalid or doesn't exist
            response.sendRedirect("login.jsp");
        } else {
            // Fetch user data from the database
            getData(request);
            
            // Forward the request to the account.jsp page
            RequestDispatcher dispatcher = request.getRequestDispatcher("account.jsp");
            dispatcher.forward(request, response);       
        }
    }

    /**
     * Fetch user data securely using PreparedStatement.
     */
    private void getData(HttpServletRequest request) {
        HttpSession session = request.getSession(false);

        try {
            // Configure the data source using context parameters
            ClientDataSource ds = new ClientDataSource();
            ds.setDatabaseName(getServletContext().getInitParameter("DB_NAME"));
            ds.setServerName(getServletContext().getInitParameter("DB_SERVER"));
            ds.setPortNumber(Integer.parseInt(getServletContext().getInitParameter("DB_PORT")));
            ds.setUser(getServletContext().getInitParameter("DB_USER"));
            ds.setPassword(getServletContext().getInitParameter("DB_PASSWORD"));
            ds.setDataSourceName("jdbc:derby");

            try (Connection conn = ds.getConnection()) {
                // Use PreparedStatement to avoid SQL injection
                String sql = "SELECT user_id, Cardholdername, Cardtype, ServiceCode, CardNumber, CAV_CCV2, expiredate, FullTrackData, PIN FROM customeraccount WHERE user_id = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setInt(1, (Integer) session.getAttribute("UMUCUserID"));

                ResultSet rs = pstmt.executeQuery();
                if (rs.next()) {
                    // Mask sensitive data
                    String cardNumberMasked = maskCardNumber(rs.getString("CardNumber"));
                    String pinMasked = maskPIN(rs.getString("PIN"));

                    // Set attributes to be forwarded to the JSP
                    request.setAttribute("Cardholdername", rs.getString("Cardholdername"));
                    request.setAttribute("CardType", rs.getString("Cardtype"));
                    request.setAttribute("ServiceCode", rs.getString("ServiceCode"));
                    request.setAttribute("CardNumber", cardNumberMasked);
                    request.setAttribute("CAV_CCV2", rs.getInt("CAV_CCV2"));
                    request.setAttribute("expiredate", rs.getDate("expiredate"));
                    request.setAttribute("FullTrackData", rs.getString("FullTrackData"));
                    request.setAttribute("PIN", pinMasked);
                }
            }
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
            request.setAttribute("ErrorMessage", "Database error occurred. Please contact support.");
        }
    }

    /**
     * Masks all but the last four digits of a card number for security.
     */
    private String maskCardNumber(String cardNumber) {
        if (cardNumber == null || cardNumber.length() < 4) {
            return "****";
        }
        return "**** **** **** " + cardNumber.substring(cardNumber.length() - 4);
    }

    /**
     * Masks the PIN, if it exists.
     */
    private String maskPIN(String pin) {
        if (pin == null || pin.length() == 0) {
            return "****";
        }
        return "****";
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP GET method.
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
     * Handles the HTTP POST method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
    // </editor-fold>

    @Override
    public String getServletInfo() {
        return "ShowAccount Servlet";
    }
}