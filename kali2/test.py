
string = """ace-voip amap automater braa casefile cdpsnarf cisco-torch \
cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk \
dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher \
golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng \
set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester \
tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed \
cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config \
doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm \
openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser \
siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia \
aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass \
fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 \
mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap \
wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze \
dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth \
padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap \
sqlninja sqlsus ua-tester uniscan w3af webscarab websploit wfuzz wpscan xsser \
zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood \
ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound \
rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip \
thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy \
cryptcat cymothoa dbd dns2tcp httptunnel intersect nishang \
polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile \
cutycapt dos2unix dradis keepnote metagoofil nipper-ng pipal \
armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter \
cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester \
maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk \
bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete \
foremost galleta guymager p0f pdf-parser \
pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood \
inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 \
termineter thc-ipv6 thc-ssl-dos burpsuite cewl chntpw \
cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt \
hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor \
multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack \
rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack \
webscarab wordlists zaproxy apktool dex2jar python-distorm3 \
edb-debugger jad javasnoop jd ollydbg smali valgrind yara \
android-sdk apktool arduino dex2jar sakis3g smali"""

import re
apts = re.findall("([\w-]+)", string)

# print(len(apts))
# print(len(set(apts)))

LIMIT = 8
with open("apt_pkg.txt", "w+") as f:
    _temp_apts = []
    f.write("apt-get -yf install \\\n")
    for x in set(apts):
        if len(_temp_apts) > LIMIT:
            f.write(" ".join(_temp_apts) + " \\\n")
            _temp_apts = []
        _temp_apts.append(x)
    f.write(" ".join(_temp_apts) + " \\\n")
    f.close()



