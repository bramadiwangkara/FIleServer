import socket
import sys
import threading
import os
import shutil
import webbrowser
import select
import BaseHTTPServer
import urllib
import cgi
import mimetypes
import re
from ConfigParser import SafeConfigParser
import subprocess

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('10.151.253.114', 12000)
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

def response_upload():
    filename = open ('form_upload2.html','r').read()
    panjang = len(filename)
    hasil = "HTTP/1.1 200 OK\r\n" \
        "Content-Type: text/html\r\n" \
        "Content-Length: {}\r\n" \
        "\r\n" \
        "{}" . format(panjang, filename)
    return hasil

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

def response_movedir(url):
	method, namafile, tujuan = url.split(':')
	filedokumen = os.system('mv ' + namafile + ' ' + tujuan)
	filedokumen = "mv folder " + namafile + " telah dijalankan :)"
	panjang = len(filedokumen)
	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	return response_header

def response_movefile(url):
	method, namafile, tujuan = url.split(':')
	filedokumen = os.system('mv file ' + namafile + ' ' + tujuan)
	filedokumen = "mv " + namafile + " telah dijalankan :)"
	panjang = len(filedokumen)
	response_header = "HTTP/1.1 200 OK\r\n" \
					"Content-Type: text/html\r\n" \
					"Content-Length:{}\r\n" \
					"\r\n" \
					"{}" . format(panjang, filedokumen)
	return response_header

def response_php(get_path):
	proc = subprocess.Popen("php " + get_path, shell=True, stdout=subprocess.PIPE)
	script_response = proc.stdout.read()
	content_length = len(script_response)
	response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length:' + str(content_length) + '\r\n\r\n' 
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


def response_upload3(req):
	#formData = cgi.FieldStorage()
	#print formData
	a,req=req.split("name=\"fileToUpload\"; ")
	#req,a,c=req.split(" -----------------------------")
	req=req.split("-----------------------------")	
	b=req[0].split("Content-Type: ")
	#get isi
	x=b[1].split("\n\r")
	print len(x)
	print "menghilangkan content type"
	print x
	#menciptakan judul
	now = datetime.datetime.now()
	now = str(now)
	now = now.replace(".","")
	now = now.replace(" ","")
	a=b[0].split("Content-Type: ")
	flnm=a[0].split("filename=\"")
	flnm=flnm=flnm[1].split("\"")
	flnm=now+flnm[0]
	print flnm
	file = open(flnm,"w")
	for xy in range(len(x)):
		if xy!=0:
			print "print"
			file.write(x[xy])
	file.close()
	#b[1]isi file
	msg="Sukses"
	panjang = len(msg)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(panjang, msg)
	return hasil


#fungsi melayani client
def layani_client(koneksi_client,alamat_client):
	try:
		print >>sys.stderr, 'ada koneksi dari ', alamat_client
		request_message = ''
		while True:
			data = koneksi_client.recv(64)
			#data = bytes.decode(data)
			request_message = request_message+data
			#print "ini adalah request message" ,  request_message
			if (request_message[-4:]=="\r\n\r\n" or request_message[-4:]=="--\r\n") :
				break



		#print "INI ADALAH A", a
		baris = request_message.split("\r\n") 
		#print "INI ISI BARIS", baris
		baris_request = baris[0]
		print baris_request

		a,url,c = baris_request.split(" ")

		if (a == 'POST' ):
			#print baris
			length = len(baris)
			name_file = baris[length-10]
			isi_file = baris[length-7]
			a= name_file.split("filename=")
			b = a[1].replace("\"", "")
			#b = nama file
			#isi_file = isi file
			#print "nama file ", b 
			#print "isi file ", isi_file
			#print "isi adalah baris", baris
			buat_file = os.system('touch ' + b )
			masukan_file = os.system('echo "'+ isi_file +  '" >> '  + b)
			respon = response_list2()			
		
		print "ini a " + a + "\n"
		print "ini url " + url + "\n"
		print "ini c " + c + "\n"

		alamat1 = url.split("?")
		print "alamat1 " , alamat1 , "\n"
#		print "alamat2 " + alamat2 + "\n"

		get_php = None
		if ".php" in url:
			strip_php = url.strip('php')
			get_php = strip_php + str('php')
			get_path = os.getcwd() + get_php
			print "ini adalah path" + get_path



		if (url=='/favicon.ico'):
			respon = response_gambar()
		elif(url == get_php):
			respon = response_php(get_path)
		elif (url=='/doc'):
			respon = response_dokumen()
		elif (url=='/teks'):
			respon = response_teks()
		elif (url=='/list'):
			respon = response_list()
		elif (url=='/list2'):
			respon = response_list2()
		elif (url== '/upload3'):
			respon = response_upload3(request_message)
		#elif ('/upload' in url):
		#	respon = response_upload()
		elif ('/movedir' in url):
			respon = response_movedir(url)
		elif ('/movefile' in url):
			respon = response_movefile(url)
		elif ('/upload2' in url):
			respon = response_upload()
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


