import socket
import sys
import threading
import os
import shutil
import webbrowser
import select
from ConfigParser import SafeConfigParser
import subprocess

# import SimpleHTTPServer
# import SocketServer

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#PORT = 11000
#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#httpd = SocketServer.TCPServer(("", PORT), Handler)
#httpd.serve_forever()

#proses binding
address = '10.151.253.51'
server_address = (address, 11000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)


def response_teks():
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/plain\r\n" \
		"Content-Length: 7\r\n" \
		"\r\n" \
		"PROGJAR HTTP Guys "
	return hasil


def response_gambar():
	filegambar = open('gambar.png','r').read()
	panjang = len(filegambar)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: image/png\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filegambar)
	return hasil

def response_icon():
	filegambar = open('myicon.png','r').read()
	panjang = len(filegambar)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: image/png\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filegambar)
	return hasil

def response_dokumen():
	filedokumen = open('dok.pdf','r').read()
	panjang = len(filedokumen)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: application/pdf\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedokumen)
	return hasil

def response_list():
	#panjang = len(filedokumen)
	os.system("python dir.py")
	filedokumen = open('list.txt','r').read()
	panjang = len(filedokumen)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedokumen)
	return hasil


def download(url):
	filedokumen = open(url, 'r').read()
	panjang = len(filedokumen)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: application/multipart\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedokumen)
	return hasil


def response_list2():
	path = "./"
	dirList = os.listdir(path)
	konten = []
	for files in dirList:
			konten.append('<a href="'+format(files)+'">'+format(files)+'</a>')
	response_data = "<br>".join(konten)
	print response_data
	content_length = len(response_data)
	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(content_length, response_data)
	#sock.sendall(response_header + response_data)
	return response_header

def response_listdir(directory):
	path = "."+directory
	dirList = os.listdir(path)
	konten = []
	for files in dirList:
			konten.append('<a href="'+format(files)+'">'+format(files)+'</a>')
	response_data = "<br>".join(konten)
	print response_data
	content_length = len(response_data)
	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(content_length, response_data)
	#sock.sendall(response_header + response_data)
	return response_header

def mkdir():
	filedokumen = open('mkdir.html','r').read()
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	return response_header

def mkdirnow(namafolder):
	os.system("mkdir "+ namafolder)
	filedokumen = "mkdir " + namafolder + " telah dijalankan :)"
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	#sock.sendall(response_header + response_data)
	return response_header

def rmdir():
	filedokumen = open('rmdir.html','r').read()
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	return response_header

def rmdirnow(namafolder):
	os.system("rm -rf "+ namafolder)
	filedokumen = "rmdir " + namafolder + " telah dijalankan :)"
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	#sock.sendall(response_header + response_data)
	return response_header

def rmfile():
	filedokumen = open('rmfile.html','r').read()
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	return response_header

def rmfilenow(namafile):
	os.system("rm "+ namafile)
	filedokumen = "rm " + namafile + " telah dijalankan :)"
	panjang = len(filedokumen)

	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	#sock.sendall(response_header + response_data)
	return response_header

def response_redirect():

	filedokumen = open('404.html','r').read()
	panjang = len(filedokumen)
	hasil = "HTTP/1.1 404 Not Found\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedokumen)
	return hasil




#fungsi melayani client
def layani_client(koneksi_client,alamat_client):
	try:
		print >>sys.stderr, 'ada koneksi dari ', alamat_client
		request_message = ''
		while True:
			data = koneksi_client.recv(64)
			data = bytes.decode(data)
			request_message = request_message+data
			if (request_message[-4:]=="\r\n\r\n"):
				break

		baris = request_message.split("\r\n")
		baris_request = baris[0]
		print baris_request

		a,url,c = baris_request.split(" ")

		
		print "ini a " + a + "\n"
		print "ini url " + url + "\n"
		print "ini c " + c + "\n"

		alamat1 = url.split("?")
		print "alamat1 " , alamat1 , "\n"
#		print "alamat2 " + alamat2 + "\n"

		if (url=='/favicon.ico'):
			respon = response_gambar()
		elif (url=='/doc'):
			respon = response_dokumen()
		elif (url=='/teks'):
			respon = response_teks()
		elif (url=='/list'):
			respon = response_list()
		elif (url=='/list2'):
			respon = response_list2()
		elif (url=='/makefolder.me'):
			respon = mkdir()
		elif (url=='/removefolder.me'):
			respon = rmdir()
		elif (url=='/removefile.me'):
			respon = rmfile()
		elif (alamat1[0]=='/buatfolder'):
			namafolder = alamat1[1]
			test, masuk = namafolder.split("=")
			respon = mkdirnow(masuk)
		elif (alamat1[0]=='/hapusfolder'):
			namafolder = alamat1[1]
			test, masuk = namafolder.split("=")
			respon = rmdirnow(masuk)
		elif (alamat1[0]=='/hapusfile'):
			namafolder = alamat1[1]
			test, masuk = namafolder.split("=")
			respon = rmfilenow(masuk)
		elif os.path.isfile("."+url) == True:
			buang, masuk = url.split("/")
			respon = download(masuk)
		elif os.path.isdir("."+url) == True:
			respon = response_listdir(url)
		else:
			respon = response_redirect()

		koneksi_client.send(respon)
	finally:
		# Clean up the connection
		koneksi_client.close()


while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	koneksi_client, alamat_client = sock.accept()
	s = threading.Thread(target=layani_client, args=(koneksi_client,alamat_client))
	s.start()


