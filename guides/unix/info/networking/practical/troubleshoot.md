# using TCP/IP ICMP
Each ICMP message contains a type, code (sub-type, msg des) and checksum (integrity) field
    Type 0 - Echo Reply
    Type 3 - Destination Unreachable
        16 code vals within
            Code 0 - Network Unreachable
            Code 1 - Host Unreachable
            ...
    Type 8 - Echo Request
    Type 11 - Time Exceeded

# ping
    test whether or not a packet can reach a host. Sends ICMP echo request packets and waits for an ICMP echo reply
    ping -c 3 www.google.com
    icmp_seq: seq num of sent packets
        nums missing: connectivety issue, nums out of order: slow connection
    ttl (Time To Live)
        hoop counter, decremented on each hop, at 0 packet dies
        at 0 router should return a ICMP Time Exceeded msg
    time
        roundtrip time
# traceroute
    see how packets are getting routed
    sends packets with increasing TTL values
    as it sends and drops packets it is build a list of routers that the packets traverse until it gets a ICMP 0
    //default 3 packets along the route
    traceroute google.com

# netstat 

    network related info: network connections, routing tables, network interfaces, ...
    ports in /etc/services
    socket
        interface that allows programs to send and receive data while a port is used to identify which application should send or receive data
        coninous connection channel per socket req that differentiates conns to same port
        socket addr: ip and port combo
        each conn needs a unique socket
            EG many concurrent http conns through port 80
    //listening and non-listening sockets 
        netstat -a
    Proto: TCP or UDP
    Recv-Q, Send-Q: Data queued to be received/sent
    Local Address, Foreign Address: Locally/Remotely connected host
    State: The state of the socket
        LISTENING: listening for incoming conns, for a TCP connection our destination has to be listening for us before we can connect
        SYN_SENT: actively attempting to establish a connection
        ESTABLISHED: has an established connection
        CLOSE_WAIT: waiting to close as the remote host has shutdown
        TIME_WAIT: waiting after close to handle packets still in the network

# Packet Analysis
    scan your network interfaces, capture the packet activity, parse the packages and output the info

    sudo apt install tcpdump
    //Capture packet data on an interface
        sudo tcpdump -i wlan0Packet Analysis
            11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
            11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
            fields
                timestamp of the network activity
                protocol info
                source/dest addr: icebox.lan > nuq04s29-in-f4.1e100.net
                seq, TCP packets's starting and ending sequence number
                length, length in bytes

            sudo tcpdump -w /some/file
