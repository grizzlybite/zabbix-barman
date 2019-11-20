# zabbix-barman-python3

Barman monitoring template for Zabbix

Fork from repo https://github.com/Open-Future-Belgium/zabbix-barman
I modified the code a bit for compatibility with python 3

Requirements:

In order to work you need to configure following option for Zabbix 

* In your sudoers file add following option:
zabbix  ALL=(barman) NOPASSWD: /usr/bin/barman list-server
zabbix  ALL=(barman) NOPASSWD: /usr/bin/barman check *
zabbix  ALL=(barman) NOPASSWD: /etc/zabbix/scripts/barman_discovery.py

* Copy the userparameter_barman.con file to your zabbix agent on the barman server 

* Restart zabbix-agent

* Import Template Barman.xml in the Zabbix Server

* Link Template to your Barman Server

* Auto Discovery will do the rest
