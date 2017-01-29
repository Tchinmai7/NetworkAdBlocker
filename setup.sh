sudo apt-get update
sudo apt-get install -y python3 dnsmasq lighttpd
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"
python3 fetchlists.py $ip
rm -rf *.txt
sort config_file.conf | uniq >/etc/dnsmasq.conf 
rm -rf config_file.conf
sudo mv adblock.conf /etc/dnsmasq.d/
sudo mv /etc/lighttpd/lighttpd.conf /etc/lighttpd/lighttpd.conf.orig
sudo cp lighttpd.conf /etc/lighttpd/lighttpd.conf
sudo cp index.html /var/www/html/index.html
