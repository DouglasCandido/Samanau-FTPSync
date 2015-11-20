# Author: Douglas Cândido
# coding: UTF-8

def downloadFile(file_name):

    # Use file_name = file_name + ".txt" if the file has an extension .txt

    localFile = open(file_name, "wb")

    ftp.retrbinary("RETR " + file_name, localFile.write, 1024) # Remove the file from the server and write it to a local file

    localFile.close()

	#ftp.quit()

    decidir()

def uploadFile(file_name):

    # Use file_name = file_name + ".txt" if the file has an extension .txt

    ftp.storbinary("STOR " + file_name, open(file_name, "rb")) # Armazena o arquivo no servidor e o abre

    decidir()
	
def acionar():
	acao = input("To catch a file from the server type pickup; to send a file to the server type send:")

	if(acao == "pickup"):
		nome_do_arquivo = input("Enter the file name you want to delete from the server:")
		downloadFile(nome_do_arquivo)
	
	else:
		nome_do_arquivo = input("Enter the file name you want to send to the server:")
		uploadFile(nome_do_arquivo)
		
def mudarDiretorio():
	diretorio_escolhido = input("Enter the directory name you want to change:")
	ftp.cwd(diretorio_escolhido)
	ftp.retrlines("LIST")
	decidir()
	
def retornarDiretorio():
	ftp.cwd("..")
	decidir()
	
def sairDaComunicacao():
	ftp.quit()
	
def decidir():
	decisao = input("To move to another directory type changedir; to return to the previous directory type returndir; to execute others actions in this directory type staydir; to exit the FTP communication type sairftp.")

	if(decisao == "changedir"):
		mudarDiretorio()

	if(decisao == "returndir"):
		retornarDiretorio()

	if(decisao == "staydir"):
		acionar()
		
	if(decisao == "sairftp"):
		sairDaComunicacao()

from ftplib import FTP

print("Welcome to the FTP client communication! IMPORTANT: All commands must be entered in quotation marks or apostrophes.")

hospedeiro = input("Enter the FTP server address:")

ftp = FTP(hospedeiro)

usuario = input("Enter your username to log in. NOTE: If you want to log in as an anonymous leave it blank.")
senha = input("Enter your password to log in. NOTE: If you want to log in as an anonymous leave it blank.")

ftp.login(user = usuario, passwd = senha) # To log in as an anonymous user the variables user and passwd must be satisfied with an empty string
                                          
ftp.getwelcome()

ftp.retrlines("LIST")

diretorio = input("Enter the directory name you want to change:")

ftp.cwd(diretorio) # Change the directory

ftp.retrlines("LIST")

decisao = input("To move to another directory type changedir; to return to the previous directory type returndir; to execute others actions in this directory type staydir; to exit the FTP communication type sairftp.")

if(decisao == "changedir"):
	mudarDiretorio()

if(decisao == "returndir"):
	retornarDiretorio()

if(decisao == "staydir"):
	acionar()
		
















