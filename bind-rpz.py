import re
import requests

ret_noerror = 1
outfilename = 'db.banlist'

links=['https://easylist.to/easylist/easylist.txt',
'https://easylist.to/easylist/easyprivacy.txt',
'https://easylist.to/easylist/fanboy-social.txt',
'https://easylist.to/easylistgermany/easylistgermany.txt',
'https://easylist-downloads.adblockplus.org/easylistitaly.txt',
'https://easylist-downloads.adblockplus.org/easylistdutch.txt',
'https://easylist-downloads.adblockplus.org/liste_fr.txt',
'https://easylist-downloads.adblockplus.org/easylistchina.txt',
'https://raw.githubusercontent.com/bongochong/CombinedPrivacyBlockLists/master/cpbl-abp-list.txt',
'https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt',
'https://easylist-downloads.adblockplus.org/fanboy-notifications.txt',
'https://raw.githubusercontent.com/Spam404/lists/master/adblock-list.txt']

try:
    with open(outfilename, "w") as fd:
        fd.write('$TTL\t1H\n\n@\tSOA\tLOCALHOST. localhost (1 1h 15m 30d 2h)\n\tNS\tLOCALHOST.\n')

        unique_lines = set()
        for url in links:
            try:
                page = requests.get(url).content.decode('utf-8')
                for line in page.splitlines():
                    if line.startswith('||') & line.endswith('^') & (re.search('\/', line) is None):
                        line = re.sub('[^a-zA-Z0-9_\-\.\~]+','', line)
                        line = re.sub('\.\.+','.', line)
                        if ret_noerror:
                            unique_lines.add(line + '\tCNAME\t*.\n')
                        else:
                            unique_lines.add(line + '\tCNAME\t.\n')
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")

        for line in sorted(unique_lines):
            fd.write(line)

except IOError as e:
    print(f"Error writing to {outfilename}: {e}")
