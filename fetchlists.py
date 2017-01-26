import urllib
import urllib.request
import sys

urllib.request.urlretrieve('https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts','stevenBlack.txt')
urllib.request.urlretrieve('http://mirror1.malwaredomains.com/files/justdomains','justdomains.txt')
urllib.request.urlretrieve('http://sysctl.org/cameleon/hosts','cameleon.txt')
urllib.request.urlretrieve('https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist','zeus.txt');
urllib.request.urlretrieve('https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt','disconnect.txt');
config_file=open('config_file.conf','w')
prefix='address=/'
suffix='/'+sys.argv[1]+'\n'

def writeConfigToFile(line):
	line=prefix+line+suffix
	config_file.write(line)
	return;

def removeIP(count,line):
	line= line[count:]
	return line;

with open('stevenBlack.txt') as f:
	for line in f:
		if line.find('#')!=-1 or line == '\n' or line.find('localhost')!= -1 or line.find('127.0.0.1')!=-1 or line.find('255.255.255.255')!=-1:
			continue;
		else :
			line=line.rstrip();
			new_line=removeIP(8,line)
			writeConfigToFile(new_line)

files=['zeus.txt','disconnect.txt','justdomains.txt','cameleon.txt']
for i in files:
	with open(i) as f:
		for line in f:
			if line.find('#')!=-1 or line == '\n' or line.find('localhost')!= -1:
				continue;
			line=line.rstrip()
			if i == 'cameleon.txt':
				line=removeIP(11,line)
			writeConfigToFile(line)
