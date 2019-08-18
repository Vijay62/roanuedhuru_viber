# Roaneudhuru - Viber Beta:
This is a beta version of viber bot which has been done at the basis of roaneudhuru_bot on telegram.

## Prerequisits:
### Python3.7
```
apt install python3.7 -y && apt install python3-pip
```
### Viber-API:
```
pip3 install viberbot
```

### Flask:
```
pip3 install flask
```

### BeautifulSoup:
```
pip3 install BeautifulSoup4
pip install lxml
```

### Apache2
```
apt install apache2 -y
```

## Setting up SSL since viber webhook requires SSL:
We are going to use letsencrypt.com, why not since it is free and easy.

### Installing CertBot:
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python-certbot-apache

# Certbot needs to be able to find the correct virtual host in your Apache configuration for it to automatically configure SSL. 
# Specifically, it does this by looking for a ServerName directive that matches the domain you request a certificate for.
# Make sure it is defined on /etc/apache2/sites-available/your_domain.conf

sudo certbot --apache -d your_domain -d www.your_domain

# Let's Encrypt's certificates are only valid for ninety days.
# This is to encourage users to automate their certificate renewal process.
# The certbot package we installed takes care of this for us by adding a renew script to /etc/cron.d
# To test the renewal process, you can do a dry run with certbot

sudo certbot renew --dry-run
```

