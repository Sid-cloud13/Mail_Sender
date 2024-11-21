import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox


def send_email():
    try:
        # Gather email details
        sender_email = sender_entry.get()
        receiver_email = receiver_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END)
        password = password_entry.get()

        # Setup MIME
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server (use your server here, e.g., Gmail's SMTP)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        # Success message
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {e}")


# Set up the main window
root = tk.Tk()
root.title("Email Sender")
root.geometry("400x400")

# Create and place the widgets
sender_label = tk.Label(root, text="Your Email:")
sender_label.pack(pady=5)
sender_entry = tk.Entry(root, width=40)
sender_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

receiver_label = tk.Label(root, text="Recipient Email:")
receiver_label.pack(pady=5)
receiver_entry = tk.Entry(root, width=40)
receiver_entry.pack(pady=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.pack(pady=5)
subject_entry = tk.Entry(root, width=40)
subject_entry.pack(pady=5)

body_label = tk.Label(root, text="Body:")
body_label.pack(pady=5)
body_text = tk.Text(root, width=40, height=10)
body_text.pack(pady=5)

send_button = tk.Button(
    root, text="Send Email", command=send_email, bg="lightblue", width=20
)
send_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
