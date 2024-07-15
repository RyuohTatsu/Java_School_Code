/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * @description This program uses Java to send emails over the SSL protocol.
 * @author Eric
 * 
 *         Modified by Brian Walters
 *         Class: SDEV 425 / Spring 2024
 *         Professor : Justin Boswell
 *         Homework 2
 * *******This class is not working correctly. I can not connect with my email to send verification code.
 * *******With more time and effort I could configure all the setting to get it running properly.
 */
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

/**
 * Utility class for sending emails using JavaMail API.
 */
public class JavaMail {

	/**
	 * Sends an email message with the security code to the specified email address.
	 *
	 * @param toEmail      The recipient's email address.
	 * @param securityCode The security code to be sent.
	 * @throws Exception If an error occurs during email sending.
	 */
	public static void sendEmail(String toEmail, String securityCode) throws Exception {
		Properties props = new Properties();
		props.put("mail.smtp.host", "smtp.gmail.com");
		props.put("mail.smtp.socketFactory.port", "465");
		props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.port", "465");
		props.put("mail.smtp.auth", "true"); // Enable authentication
		props.put("mail.smtp.starttls.enable", "true"); // Enable STARTTLS
		props.put("mail.smtp.host", "smtp.gmail.com"); // SMTP host for Gmail
		props.put("mail.smtp.port", "587"); // Port for TLS/STARTTLS

		Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication("your_email@gmail.com", "your_password!");
			}
		});

		try {
			Message message = new MimeMessage(session);
			message.setFrom(new InternetAddress("from_email@gmail.com"));
			message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(toEmail));
			message.setSubject("Your Security Code");
			message.setText("Your security code is: " + securityCode);

			Transport.send(message);
		} catch (MessagingException e) {
			throw new RuntimeException(e);
		}
	}
}