import requests
import sys

try:
    input_func = raw_input
except:
    input_func = input


def menu():
    print('''
Menu\n
1: Show containers
2: Create container
3: Delete container
4: Delete all containers
5: Show images
6: Pull Image
7: Delete image
8: Delete all images
9: Quit
''')


def verify_error(response, code, show_error=True):
    if response.status_code == code:
        if show_error:
            print('Command OK')
        return True

    if show_error:
        print('ERROR: %d' % response.status_code)

    return False


def get_containers(ipaddr, show=True):
    ret = requests.get('%s/containers/json?all=1' % ipaddr)

    if verify_error(ret, 200):
        if show:
            for i in ret.json():
                print(i)
        else:
            return ret.json()


def delete_container(ipaddr, uid=None):
    if uid:
        cont = uid
    else:
        cont = input_func('Insert the container UID: ')

    ret = requests.delete('%s/containers/%s' % (ipaddr, cont))
    return verify_error(ret, 204)


def create_container(ipaddr):
    image = input_func('Insert image:tag name: ')
    cont_name = input_func('Insert container name: ')

    payload = {'Image': image, 'Entrypoint': 'bash'}
    ret = requests.post('%s/containers/create?name=%s' % (ipaddr, cont_name), json=payload)
    verify_error(ret, 201)


def delete_all_containers(ipaddr):
    lst = get_containers(False)

    for i in lst:
        delete_container(i['Id'])


def get_images(ipaddr, show=True):
    ret = requests.get('%s/images/json?all=0' % ipaddr)

    if verify_error(ret, 200):
        if show:
            for i in ret.json():
                print(i)
        else:
            return ret.json()


def create_image(ipaddr):
    name = input_func('Insert the image name: ')
    tag = input_func('Insert tag name: ')

    print('Pulling image...')

    ret = requests.post('%s/images/create?fromImage=%s&tag=%s' % (ipaddr, name, tag))
    verify_error(ret, 200)


def delete_image(ipaddr, iname=None):
    if iname:
        name = iname
    else:
        name = input_func('Insert the image name to be removed: ')

    ret = requests.delete('%s/images/%s' % (ipaddr, name))
    verify_error(ret, 200)


def delete_all_images(ipaddr):
    lst = get_images(False)

    for i in lst:
        delete_image(i['RepoTags'][0])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python docker.py <ip of the docker daemon>')
        sys.exit(1)

    # default port used is 2375
    ipaddr = 'http://%s:2375' % (sys.argv[1])

    while True:
        menu()

        opt = input_func('Choice: ')

        if opt == '1':
            get_containers(ipaddr)
        elif opt == '2':
            create_container(ipaddr)
        elif opt == '3':
            delete_container(ipaddr)
        elif opt == '4':
            delete_all_containers(ipaddr)
        elif opt == '5':
            get_images(ipaddr)
        elif opt == '6':
            create_image(ipaddr)
        elif opt == '7':
            delete_image(ipaddr)
        elif opt == '8':
            delete_all_images(ipaddr)
        elif opt == '9':
            break

    print('Bye!')
