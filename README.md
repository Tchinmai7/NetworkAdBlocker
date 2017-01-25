A simple network wide ad blocker using dnsmasq and a lighthttpd server. 
It fetches the a list of adservers from a number of sources, and cooks up the
dnsmasq.conf file and places them in the /etc/ path.

The adservers get resolved to the ip address of the `eth0` interface of the device.
The lighthttpd service running on the device handles the requests and will return a 404 to all requests


Inspired heavily from the Pi-Hole
