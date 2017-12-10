import socket
import sys
import threading
import os
import shutil
import webbrowser

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('localhost', 13000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)


def response_teks():
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/plain\r\n" \
		"Content-Length: 7\r\n" \
		"\r\n" \
		"PROGJAR"
	return hasil

def response_no1():
	files = os.listdir(os.curdir)

	isi = ''

	for f in files:
		isi += f
		isi += "\n"

	isi = "<input type=\"text\" name=\"input\" placeholder=\"Masukkan Folder yang akan dipindah\" />"

	panjang = len(isi)

	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(panjang, isi)

	return hasil

def response_no6():

	mydir= ("<input type=\"text\" name=\"input\" id=\"folder\" placeholder=\"Masukkan Folder yang akan dihapus\" /> <input type=\"submit\" value=\"submit\"/> ")
	panjang = len(mydir)

	try:
		shutil.rmtree(mydir)
	except OSError, e:
		print ("Error: %s - %s." % (e.filename,e.strerror))

	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, mydir)
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

def response_list2():
	filename = "test1"
	webbrowser.open('file://' + os.path.realpath(filename))

def response_redirect():
	hasil = "HTTP/1.1 301 Moved Permanently\r\n" \
		"Location: {}\r\n" \
		"\r\n"  . format('http://www.its.ac.id')
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

		if (url=='/favicon.ico'):
			respon = response_icon()
		elif (url=='/doc'):
			respon = response_dokumen()
		elif (url=='/teks'):
			respon = response_teks()
		elif (url=='/1'):
			respon = response_no1()
		elif (url=='/6'):
			respon = response_no6()
		elif (url=='/list'):
			respon = response_list()
		elif (url=='/list2'):
			respon = response_list2()
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

