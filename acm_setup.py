#!/usr/bin/env python3
import os, sys, logging
from time import sleep
#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
                filename='cvpn.log', level=logging.INFO)

#reusable code
def check_item(item):
    ''' checks if file/folder exist '''
    try:
        output = os.popen('ls').read() #expect the following easyrsa
        if 'easyrsa' in output:
            print(f'{item} found in folder...')
            logging.info(f'{item} found in folder...')
        else:
            print(f'{item} not found in folder...')
            logging.info(f'{item} not found in folder...')
            quit()

    except Exception as err:
        print(f'This error {err} occurred...')
        logging.info(f'This error {err} occurred...')

#tasks start here
#create ACM folder
os.system('mkdir ACM-CA')
#clone repo
os.system('git clone https://github.com/OpenVPN/easy-rsa.git')
#cd to easy-rsa folder
os.chdir('easy-rsa/easyrsa3')
#initialize a new PKI environment
os.system('./easyrsa init-pki')
#build new certificate
#output_view = Common Name (eg: your user, host, or server name) [Easy-RSA CA]: 
#Confirm request details:
os.system('./easyrsa build-ca nopass')
#generate server certificate
os.system('./easyrsa build-server-full server nopass')
#generate client certificate
os.system('./easyrsa build-client-full client1.domain.tld nopass')

#copying certificates to new folder
os.system('cp pki/ca.crt ../../ACM-CA/')
os.system('cp pki/issued/server.crt ../../ACM-CA/')
os.system('cp pki/private/server.key ../../ACM-CA/')
os.system('cp pki/issued/client1.domain.tld.crt ../../ACM-CA/')
os.system('cp pki/private/client1.domain.tld.key ../../ACM-CA/')

#ls #expect the following: ca.crt, client1.domain.tld.crt, client1.domain.tld.key, server.crt, server.key
#check if ca.crt exists
check_item('../../ACM-CA/ca.crt')
#check if client1.domain.tld.crt exists
check_item('../../ACM-CA/client1.domain.tld.crt')
#check if client1.domain.tld.key
check_item('../../ACM-CA/client1.domain.tld.key')
#check if server.crt exists
check_item('../../ACM-CA/server.crt')
#check if server.key exists
check_item('../../ACM-CA/server.key')

os.chdir('../../ACM-CA/')
os.getcwd()
#upload server and client certificates to AWS certificate Manager
cert_output = os.system('aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt --region us-east-1')

# ------------------------ End ----------------------------
