import smtplib
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "allaboutpythontestacc2@outlook.com"
TO_EMAIL = "allaboutpythoninfo@gmail.com"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: Mail sent using python
Hi allaboutpython, 

This email is sent using a test account.

Thanks,
Test Account"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()