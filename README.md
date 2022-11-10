# maendeleolab_cvpn

<img src="/images/banner.png" width=400>

├── acm_setup.py
├── README.md
├── LICENSE

## [Context](#Context)

- This script helps generate a server, client certificates and keys to use with AWS Client VPN.


## [Prerequisites](#Prerequisites)

- Must have awscli version 2 and Python 3.6.9 (or higher) installed.


## [Walk-through](#Walk-through)

**1**  - Make sure to comply with the prerequisites mentioned above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to your host machine using the syntax below.

```
git clone https://github.com/maendeleolab/maendeleolab_cvpn.git
```

**4**  - cd to folder maendeleolab_cvpn

```
cd maendeleolab_cvpn
```

**5**  - List the file in the folder with the **ls** command.

**6**  - Execute the script

```
./acm_setup.py
```

**Note:** The following will happen, when you execute the script.

1) A file named **cvpn.log** will be created to store the script logs. 

2) Install [easy-rsa utility](https://easy-rsa.readthedocs.io/en/latest/)

3) Generate a server, client keys and certificates.

4) Create folder ACM-CA and copy server, client keys and certificates to the folder.

5) Then import the server certificate to AWS ACM. 

```
README.md
LICENSE
ACM-CA
acm_setup.py
easy-rsa
cvpn.log
```

## [Support](#Support)
If you find this script useful, please support it with a shout out on your favorite social media platform!

![Twitter](https://img.shields.io/twitter/follow/maendeleolab?style=social)
```
Twitter : @maendeleolab
Instagram : @maendeleolab
TitTok : @pat_maendeleolab
```
## [License](#License)
GNU GENERAL PUBLIC LICENSE

