import os
mb_or_gb = int(input("Required file size in\n1-GB\n2-MB\n\n"))
if mb_or_gb ==1 or mb_or_gb == 2:
	how_many = int(input("Quantity. eg: 20\n\n"))
	if mb_or_gb == 1:
		requried_bytes = how_many * 1024*1024*1024
	elif mb_or_gb == 2:
		requried_bytes = how_many*1024*1024
		with open('zeros_file.txt', 'w') as file:
			file.write('0'*requried_bytes)
		os.system("du -sh zeros_file.txt -b > temprory_file.txt")
		a = open("temprory_file.txt", 'r').read()
		bytes = int(a.split("\t")[0])
		mb = bytes / (1024*1024)
		print("\nbytes:  ", bytes)
		print("MB:\t", mb)
		print("GB:\t", mb/1024, '\n')
		os.system("rm temprory_file.txt")
		print("\n\n\n*************Your file name is zeros_file.txt located at your working direcotry*************\n\n\n")
else:
	print("Sorry, Enter either 1 or 2 not else")