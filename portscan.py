import socket

dominio = input('Digite o ip ou dominio: ')
portas = [21, 22, 23, 25, 53, 80, 110, 143, 3389, 5631, 43, 80, 8080, 81,
110, 118, 5555, 156, 366, 443, 902, 992, 993, 990, 989, 1521]

for porta in portas:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(1)
	codigo = client.connect_ex((dominio, porta))
	if codigo == 0:
		print(porta, "Aberto")
