# Email Sender Application

This is a Python-based Email Sender application built using the `tkinter` library for the GUI interface and `smtplib` for sending emails. The application allows users to send emails with a subject and body by providing the sender's email, password, recipient's email, and other required details.

## Features
- Simple GUI for sending emails.
- Fields to input sender's email, recipient's email, subject, and body.
- Secure email sending using `smtplib` with TLS encryption.
- Success and error notifications for user feedback.

---

## Prerequisites

1. **Python 3.x** installed on your system.
2. Install the following required libraries if not already installed:
   ```bash
   pip install tk
   ```
   *(Note: `tkinter` is usually pre-installed with Python on most systems.)*

3. Use an email account that supports SMTP (e.g., Gmail, Yahoo). For Gmail:
   - Enable **"Allow less secure apps"** on your Google account. *(Note: This is not recommended for production use. Use app-specific passwords or OAuth2 for better security.)*
   - Alternatively, generate an **App Password** from your Google account settings if two-factor authentication (2FA) is enabled.

---

## How to Run the Application

1. Save the code in a Python file, for example, `email_sender.py`.

2. Open a terminal or command prompt and navigate to the directory containing the file.

3. Run the script:
   ```bash
   python email_sender.py
   ```

4. The application window will open. Fill in the following fields:
   - **Your Email**: The email address from which you are sending the email.
   - **Password**: Your email account password (or app-specific password if 2FA is enabled).
   - **Recipient Email**: The email address of the recipient.
   - **Subject**: The subject of the email.
   - **Body**: The body/content of the email.

5. Click the **Send Email** button to send the email.

---

## Application Layout

1. **Your Email**: Field to enter the sender's email address.
2. **Password**: Field to enter the sender's password (hidden for privacy).
3. **Recipient Email**: Field to enter the recipient's email address.
4. **Subject**: Field to enter the subject of the email.
5. **Body**: Multi-line text box for composing the email body.
6. **Send Email Button**: Button to send the email.

---

## Error Handling
- If an error occurs (e.g., invalid credentials, incorrect recipient address, or SMTP connection failure), an error message will be displayed in a pop-up window.

---

## Notes
- **Security Warning**: This application stores and sends sensitive data (email and password). It is meant for educational purposes only. Do not use it with personal or sensitive accounts in production without proper security enhancements.
- Use app-specific passwords or OAuth2 authentication for better security when using services like Gmail.

---

## Sample Screenshots
(Not included. You can take screenshots of the application after running it to include here.)

---


Feel free to modify and enhance it as needed!
