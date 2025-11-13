# LEVEL UP! Bonus Challenge
# Challenge: Write and Save a Simple Log File

from datetime import datetime

def write_log():
    message = input("Enter a message to log: ")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("log.txt", "a") as file:
        file.write(f"{timestamp} {message}\n")
    print("Message logged!")


write_log()
