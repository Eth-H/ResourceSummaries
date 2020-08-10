# linux networking config concepts
    interfaces
        routing table enteries
            policy routeing
    namespaces

# network interfaces
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
        ifdown eth0

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

# arp cache
    not persistent between reboots
    if packet sent to dest not in arp
        boadcast frame containing arp req packet asking for dest mac
        adds the ip to mac mapping to the arp cache and then proceeds with sending the packet

    check local arp cache
        arp
        ip neighbour show

# Network Manager
    startup daemon, automatically find and bring up network interface, scan for wifi/wired networks and conn
    get network hardware information
    nmapplet //on your desktop bar
    //get operational info (old)
        nm-tool 
    //control
        nmcli
        nmtui

# network namspaces
    by default only have a unnamed/default/global namespace that is directly connected to the physcial interfaces
    having different namespaces allow for seperate/independant instances of network interfaces, routing tables, firewall rules
    ip netns add blue
    ip netns list
    //assign interfaces to namespaces
        cant assign physcial interfaces to namespaces
        veth (virtual ethernet) interfaces come in pairs
            can use to connect a namespace to the internet via the global namespaces that contain the physcial interfaces
        //create pair
            ip link add veth0 type veth peer name veth1
        //connect global namespace to blue namespace, via sending one end to that namespace
            ip link set veth1 netns blue
        //run cmd in blue namespace, if namespaces setup correctly this should be the only way
            ip netns exec blue ip link list
        // config veth{} interfaces
            ip addr add 10.0.0.1/24 dev veth0
            ip link set up veth0
            ip netns exec blue ip addr add 10.0.0.2/24 dev veth1
            ip netns exec blue ip link set dev veth1 up
            // add a default route inside the blue namespace
                ip netns exec blue ip route add default via 10.0.0.1
            //add routing to the internet
                sudo iptables -I FORWARD -s 10.0.0.0/24 -j ACCEPT # Forward packets for IPs from inside the namespace
                sudo iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -j MASQUERADE # Use NAT for packets from the zoom network
        //run cmd within namespace without root
            netns-exec blue firefox
        //directly connect physical interface to namespace, not recomended
            ip link set dev <device> netns <namespace>
