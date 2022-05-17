# import smtplib

# sender = 'amirqulamirqulov9@gmail.com'
# receiver = 'redmi9566@gmail.com'
# password = "wjrtejlnpwprjfxj"
# smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(sender, password)
# msg = """
#     <h2>Python development course</h2>
#     This message from developer of PDP
# """
# smtpserver.sendmail(sender, receiver, msg)
# print('Sent')
# smtpserver.close()


import socket

HOST = '10.10.14.192'  # Standard loopback interface address (localhost)
PORT = 8181       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b"vaalaykum")