# 📧 Send Email Using Python

This Python script allows you to send emails programmatically using Gmail's SMTP server. Customize the recipient, subject, and message content to send emails effortlessly!

---

## ✨ Features

- Send emails programmatically through Python.
- Uses Gmail's SMTP server for reliable delivery.
- Securely authenticates using your Gmail credentials.

---

## 📋 Prerequisites

- **Python**: Ensure Python is installed on your system.
- **smtplib**: This is a built-in Python library, so no additional installation is needed.
- **Google App Password**: Required to securely authenticate with Gmail.

---

## 🚀 How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project folder:

   ```bash
   cd your-repo-name
   ```

3. Edit the script to include your Gmail address and App Password:
   Replace `Your Email` with your Gmail address and `Your Password` with the App Password you generate (see instructions below).

4. Run the script:

   ```bash
   python send_email.py
   ```

5. Enter the recipient's email address and your message when prompted.

---

## 🖥️ Code Overview

```python
# Email Sender

import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Password')
    server.sendmail('Your Email', to, content)
    server.close()

if __name__ == "__main__":
    try:
        content = input("Type your Message \n")
        to = input("Whom to send the Email? , enter their email address\n")
        sendEmail(to, content)
        print("Email has been sent! 😉")
    except Exception as e:
        print(e)
        print("Sorry, email not sent 😥")
```

---

## 🔐 Setting Up Google App Password

Google has disabled direct access using passwords for security reasons. Follow these steps to generate an **App Password** for secure authentication:

1. Go to your **Google Account**: [https://myaccount.google.com/](https://myaccount.google.com/)
2. Navigate to **Security** in the left sidebar.
3. Ensure **2-Step Verification** is enabled. If not, set it up first.
4. Under **"Signing in to Google"**, locate **App Passwords** and click on it.
5. Log in again if prompted.
6. Choose the app (`Mail`) and the device (`Other`) for which you are generating the password. Name it something like `Python Script`.
7. Click **Generate**. Copy the 16-character App Password shown.
8. Replace the `Your Password` placeholder in the script with this App Password.

---

## ⚙️ Example Usage

### Input:
```bash
Type your Message 
Hello, this is a test email!

Whom to send the Email? , enter their email address
example@example.com
```

### Output:
```bash
Email has been sent! 😉
```

If there’s an error (e.g., incorrect credentials), it will display the error message.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements or suggestions.

---

## ✍️ Author

- **Dhairya Vora**  
  - GitHub: [DR-Vora](https://github.com/DR-Vora)  
  - LinkedIn: [Dhairya Vora](https://www.linkedin.com/in/dhairya-vora-475577275)  

---

## 📞 Contact Me

For any questions or support:  
📧 **Email**: voradhairya22@gmail.com  
