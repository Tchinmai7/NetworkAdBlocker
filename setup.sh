sudo apt-get update
sudo apt-get install -y dnsmasq lighthttpd
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"
python3 fetchlists.py $ip
rm -rf *.txt
sort config_file.conf | uniq >/etc/dnsmasq.conf 
rm -rf config_file.conf
