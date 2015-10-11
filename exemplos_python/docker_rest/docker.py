import json
import sys

import requests

ipaddr = ''

def menu():
	print('\nMenu\n\n' +
		'1: Show containers\n' + 
		'2: Create container\n' +
		'3: Delete container\n' +
		'4: Delete all containers\n' +
		'5: Show images\n' +
		'6: Pull Image\n' +
		'7: Delete image\n' +
		'8: Delete all images\n' +
		'9: Quit')

def verifyError(data, code, show_error = True):
	if str(data) == '<Response [' + code + ']>':
		if show_error:
			print('Command OK')
		return True
	if show_error:
		print('ERROR: ' + code)
	return False

def getContainers(show = True):
	ret = requests.get(ipaddr + '/containers/json?all=1')
	if verifyError(ret, '200'):
		if show:
			for i in ret.json():
				print i
		else:
			return ret.json()

def deleteContainer(uid = None):
	if uid:
		cont = uid
	else:
		cont = raw_input("Insert the container UID: ")
	ret = requests.delete(ipaddr + '/containers/' + cont)
	return verifyError(ret, '204')

def createContainer():
	image = raw_input('Insert image:tag name: ')
	cont_name = raw_input('Insert container name: ')

	payload = {"Image":image, 'Entrypoint':'bash'}
	ret = requests.post(ipaddr + '/containers/create?name=' + cont_name, json=payload)
	verifyError(ret, '201')

def deleteAllContainers():
	err = []
	lst = getContainers(False)
	for i in lst:
		deleteContainer(i['Id'])

def getImages(show = True):
	ret = requests.get(ipaddr + '/images/json?all=0')
	if verifyError(ret, '200'):
		if show:
			for i in ret.json():
				print i
		else:
			return ret.json()

def createImage():
	name = raw_input('Insert the image name: ')
	tag = raw_input('Insert tag name: ')
	print('Pulling image...')
	ret = requests.post(ipaddr + '/images/create?fromImage=' + name + '&tag=' + tag)
	verifyError(ret, '200')

def deleteImage(iname = None):
	if iname:
		name = iname
	else:
		name = raw_input('Insert the image name to be removed: ')

	ret = requests.delete(ipaddr + '/images/' + name)
	verifyError(ret, '200')

def deleteAllImages():
	err = []
	lst = getImages(False)
	for i in lst:
		deleteImage(i['RepoTags'][0])

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
		deleteContainer()
	elif opt == '4':
		deleteAllContainers()
	elif opt == '5':
		getImages()
	elif opt == '6':
		createImage()
	elif opt == '7':
		deleteImage()
	elif opt == '8':
		deleteAllImages()
	elif opt == '9':
		break

print('Bye!')
