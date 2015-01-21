#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

routeSys = "/etc/hosts"
routeBlack = "hostsBlacklisted"
routeWhite = "hostsBuckup"
rutaHostsOriginal = "/etc/hosts"

def banner():
	print("""
	####################################
	#                                  #
	#      Script para estudiar        #
	#   Hecho por @SalvaCorts cuando   #
	#   deberia estar estudiando...    #
	#                                  #
	####################################


	[1] Empezar a estudiar.
	[2] Dejar de estudiar.
	[3] Salir.

	""")

def hostBuckup():
	file = open(routeSys, "r")
	file2 = open(routeWhite, "w")
	file2.writelines(file)
	file.close()
	file2.close()

def writeHostsBlack():
	file = open(routeSys, "w")
	file2 = open(routeBlack, "r")
	file.writelines(file2)
	file.close()
	file2.close()

def hostsRecovery():
	file = open(routeSys, "w")
	file2 = open(routeWhite, "r")
	file.writelines(file2)
	file.close()
	file2.close()

def apacheStart():
	os.system("clear")
	os.system("/etc/init.d/apache2 start")
	os.system("clear")
	print("Started!")

def apacheStop():
	os.system("clear")
	os.system("/etc/init.d/apache2 stop")
	os.system("clear")
	print("Stoped!")

def killProcesses():
	os.system("clear")
	print("\nKilling Services that are using hosts file!")
	os.system("killall firefox")
	os.system("killall google-chrome")
	os.system("killall chromium-browser")
	os.system("killall midori")
	os.system("clear")
	print("Killed!")

def restartProcesses():
	os.system("clear")
	os.system("/etc/init.d/networking restart")
	os.system("killall -hup inetd")
	os.system("clear")
	print("Stoped!")

def main():
	if (os.geteuid()==0): # check root permissions
		def purpose():
			banner()
			purpose = raw_input("[1,2,3]-->   ")
			if (purpose == "1"):
				# code here!
				hostBuckup()
				writeHostsBlack()
				apacheStart()
				killProcesses()
				restartProcesses()
				os.system("clear")
				print("\nStudying...")
				main()

			elif (purpose == "2"):
				# code here!
				hostsRecovery()
				apacheStop()
				killProcesses()
				restartProcesses()
				os.system("clear")
				print("\nRestored!")
				main()				
			elif (purpose == "3"):
				exit()
				
			else:
				os.system("clear")
				print("\nOption 1, 2 or 3.")
				os.system("clear")
				main()
		
		purpose()

	else:
		# Must be root!
		os.system("clear")
		print("\nYou must be root")
		exit()

main()
