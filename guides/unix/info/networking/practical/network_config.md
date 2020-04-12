# Network Interfaces
how the kernel links up the software side of networking to the hardware side (device drivers and network)
## ifconfig 
    config net interfaces
    runs on bootup and reads config files for interfaces
    eth0 (first Ethernet card), wlan0 (wireless interface)
    lo (loopback interface): represents this computer, good to debug or use local servers
    //create interface, assign ip/netmask, set up
    ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
    //bring up/down
        ifup eth0
        ifdown eth

## ip (from iproute2)
    more modern alternative to ifconfig (from net-tools)
    // all interfaces info/stats
        ip link
        ip -s link
    //specific interface info
        ip link show eth0
    //show ip addresses allocated to interfaces
        ip address show
    //bring interfaces up/down
        ip link set eth0 up
        ip link set eth0 down
    //add an ip address to an interface
        ip address add 192.168.1.1/24 dev eth0

## route
    //add/remove routes with net-tools/ip
    sudo route add -net 192.168.2.1/23 gw 10.11.12.3
    sudo route del -net 192.168.2.1/23
    ip route add 192.168.2.1/23 via 10.11.12.3
    ip route delete 192.168.2.1/23

## dhclient
    on boot sets up list of interfaces from dhclient.conf
    dhclient.leases file is read to let it know what leases it's already assigned.
    //get fresh ip
        sudo dhclient

# Network Manager
    NetworkManager daemon to configures networks automatically
    get network hardware information, search for conns to wireless/wired and activate
    nmapplet //on your desktop bar
    //get operational info (old)
        nm-tool 
    //control
        nmcli
        nmtui
## arp cache
    not persistent between reboots
    if packet sent to dest not in arp
        boadcast frame containing arp req packet asking for dest mac
        adds the ip to mac mapping to the arp cache and then proceeds with sending the packet

    check local arp cache
        arp
        ip neighbour show
