# troubleshoot
## trace packets to a domain
    //may need to install either
    traceroute [domain]
    mtr [domain]
## watch all packets
    [`wireshark`](https://wireshark.org/)
    [`tshark`](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html)
    [`ngrep`](http://ngrep.sourceforge.net/)


# netcat
conenct to ports
    //Listen on a port
        nc -l 1337
    //Connect to a port
        nc 192.168.33.2 1337
    //Transfer files
        //Listen on port and send any output recevied content to [filename]
            nc -l 1337 > [filename]
        //Connect to computer and send the content of myfile
            nc 192.168.33.2 1337 < [localFilename]
#SSH
secure conection to server
    //with credentials, add a custom port (default 22): -p
        ssh username@domain.com {}
    //If a keyfile is needed instead of a separate pw
        ssh -i /path/to/keyfile username@ipaddress
    //Copy local file/dir to remote server
        scp file.txt username@domain.com:/folder/file.txt
        scp -r dir username@domain.com:/folder/dir
    //Copy remote file to local PC 
        scp username@domain.com:/folder/file.txt file.txt

# https tools
## curl 
    //none: get request, --data "username=luffy&loggedin=true": post data, 
        curl https://example.com/index.php {} 			
## wget 
    //Blank: Download webpages, -c: Continue stopped download
        wget {} [url/file]

# domain tools
    whois domain
    //DNS info
        dig [domain]
    //Reverse lookup host
        dig -x host

# net-tools pkg
considered deprecated, but widely avaliable
## network interfaces
### ifconfig
    list/config network interfaces
        ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
        ifconfig ifup eth0
        ifconfig ifdown eth0
    bring interface up/down
        ifconfig eth0 up
        ifconfig eth0 down
    give interface ip
        ifconfig eth0 192.168.1.1
### iwconfig
    config wireless network interfaces
    iwconfig eth0 freq 2422000000
## route
    //display routing table (= netstat -r)
        route
    //add/remove routes with net-tools
    sudo route add -net 192.168.2.1/23 gw 10.11.12.3
    sudo route del -net 192.168.2.1/23
## arp cache
    arp
## read ports, netstat 
check open/listening ports for socket connections
    //-a: all sockets, -u: udp, -t: tcp, -x: unix pipe sockets 
    //-l: listening sockets, -p: PID and program name, -n: dont resolve names 
    //-A [addressFamilyName, aFN2, ...]: inet, inet6, ax25, netrom, ipx, ddp, x25
    //-c continuous mode
    //-g: multi-cast group info
        netstat {}...
    //EG
        //listening tcp and udp with pid
        netstat -lptu
        //inet protocol with pid
        netstat -A inet -p

# iproute2 pkg
newer net-tools alt
    //n: arp, route: netstat -r
    //-s [cmd]: ip stats (more info)
        ip {}..
## addresses
    //addr, a, address: ipv4 addrs, maddr, ma: ipv6 addrs (netstat -g)
        ip {}
## interfaces
    // all interfaces info/stats (netstat -i)
        ip link
        ip -s link
    //specific interface info
        ip link show eth0
    //show ip addresses allocated to interfaces
        ip addr show
    //bring interfaces up/down
        ip link set eth0 up
        ip link set eth0 down
    //add/del an ip address to an interface
        ip addr add 192.168.1.1/24 dev eth0
        ip addr del 192.168.1.1/24 dev eth0
    //iwconfig ethernet options
        iw
## route 
    ip route add 192.168.2.1/23 via 10.11.12.3
    ip route delete 192.168.2.1/23
## arp cache
    //n, neigh, neighbour
        ip {} 
## neighbour cache
    ip ntables
## read ports, ss
    //netstat options
    //-a: all sockets, -u: udp not in listen mode (servers), -t: tcp not in LM, -x: unix pipes
    //-l: listening sockets, -p: PID and program name, -n: dont resolve names
    //-o: options (timers, more flexible), //-s: prints statstics, --ipv4: ip version 4
        ss {}...
    //show all sockets connecting to 192.168.1.10 on port 443
        ss -t dst 192.168.1.10:443
    //show all ssh related connection
        ss -t state established '( dport = :ssh or sport = :ssh )'


# run a local file server
    python server
        python -m SimpleHTTPServer 7777 #py2 
        python -m http.server 7777 #py3

# to check
    //Point to point conenction between two nodes, encapsulate packets in IP packets and send over IP infrastructure
        iptunnel {}...
    nameif
