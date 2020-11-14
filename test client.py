import socket

def upload():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 123))
    file_name = "../a.csv"
    with open(file_name, "r") as text:
        a = text.read()
    s.send(a.encode())
    s.send(file_name.encode())
    r = (str(s.recv(1)))[2:-1]
    if r == "1":
        print("Erreur d'envoi")
def gete():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 123))

    print("Le nom du fichier que vous voulez récupérer:")
    file_name = "hey.csv"
    s.send(file_name.encode())
    s.send(file_name.encode())
    file_name = 'data/%s' % (file_name,)
    r = s.recv(9999999)
    with open(file_name, 'wb') as _file:
        _file.write(r)
    print("Le fichier a été correctement copié dans : %s." % file_name)
upload()