import json
import sys

import requests

ipaddr = ''

def menu():
	print('\nMenu\n\n' +
		'1: Show containers\n' + 
		'2: Create container\n' +
		'3: Delete container\n' +
		'4: Show images\n' +
		'5: Pull Image\n' +
		'6: Delete image\n' +
		'9: Quit')

def showContent(data):
	if str(data) != '<Response [200]>':
		print('Error: ' + str(data))
		return
	for i in data.json():
		print i

def getContainers():
	showContent(requests.get(ipaddr + '/containers/json?all=1'))

def getImages():
	showContent(requests.get(ipaddr + '/images/json?all=1'))

def createImage():
	name = raw_input('Insert the image name: ')
	tag = raw_input('Insert tag name: ')
	print('Pulling image...')
	ret = requests.post(ipaddr + '/images/create?fromImage=' + name + '&tag=' + tag)

def createContainer():
	image = raw_input('Insert image:tag name: ')
	cont_name = raw_input('Insert container name: ')

	payload = {"Image":image, 'Entrypoint':'bash'}

	ret = requests.post(ipaddr + '/containers/create?name=' + cont_name, json=payload)
	print str(ret)

if len(sys.argv) != 2:
	print('Usage: python docker.py <ip of the docker daemon>')
	sys.exit(1)

# default port used is 2375
ipaddr = 'http://' + sys.argv[1] + ':2375'

while True:
	menu()
	
	opt = raw_input('Choise: ')
	if opt == '1':
		getContainers()
	elif opt == '2':
		createContainer()
	elif opt == '3':
		removeImage()
	elif opt == '4':
		getImages()
	elif opt == '5':
		createImage()
	elif opt == '9':
		break

print('Bye!')
