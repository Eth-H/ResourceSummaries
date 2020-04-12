ISP - Your internet service provider, the company you pay to get Internet at your house.
Router - The router allows each machine on your network to connect to the Internet. In most modern routers, you can connect via wireless or an Ethernet cable.
WAN - Wide Area Network, this is what we call the network that encompasses everything between your router and a wider network such the Internet.
WLAN - Wireless Local Area Network, this is the network between your router and any wireless devices you may have such as laptops.
LAN - Local Area Network, this is the network between your router and any wired devices such as Desktop PCs.
Hosts - Each machine on a network is known as a host.

OSI Model (Open Systems Interconnection)
    shows us how a packet traverses through a network in seven different layers
TCP/IP Model
    based off OSI
    specify how data should be gathered, addressed, transmitted and routed through a network
    packet
        header
        payload
        each layer adds to packet
        called different thing at different layer
            transport: segment, link: frame
    Application Layer
        top layer, allows high level apps to interface with transport layer services to view the data that gets sent or received
        HTTP (Hypertext Transfer Protocol) - used for the webpages on the Internet.
        SMTP (Simple Mail Transfer Protocol) - electronic mail (email) transmission

        EG email application sents data to transport layer

    Transport Layer
        how data will be transmitted, checking the correct ports and integrity of the data, delivering our packets
        ports: communication channels
        TCP (Transmission Control Protocol)
            reliable connection-oriented stream of data
            establish connection with TCP handshake
                The client (connecting process) sends a SYN segment to the server to request a connection
                Server sends the client a SYN-ACK segment to acknowledge the client's connection request
                Client sends an ACK to the server to acknowledge the server's connection request
            dat sent tracked with seq nums to arrange at target location
        UDP (User Datagram Protocol): unreliable but fast data delivery

        encapsulates applicaition data into a TCP/UDP header with ports to form a segment -> send to network layer
    Network Layer
        how to move packets between hosts and across networks
        IP (Internet Protocol) - route packets across machines
        ICMP (Internet Control Message Protocol) - tell us whats going on, EG err messages and debugging info

        encapsulates segement from transport layer into ip packet, attaches source/dest addr to header -> route to link layer

    Link Layer
        how to send data across a physical piece of hardware. EG data travelling through Ethernet, fiber, ...
        packet encapsualted into frame, frame header holds source/dest mac addr, chcksums, packet separators
    ARP (Address Resolution Protocol)
        find MAC addr associated with IP
        only work iwthin same network, so need to route through other network first
        check ARP look-up which has ips linked to macs
            if not found ARP broadcast all machines asking for mac to ip, a machine will reply with both
    after ARP add ip and mac to frame, then send the frame out of the NIC and route to target network
    
    on the targets network each layer is performed in reverse with data integrity checks

Network Addressing
    MAC addr
        unique identifier used as a hardware address, never change
        comes from NIC (network interface card) 
        OUI (organizationally unique identifier): specific to manufacturer, first 3 bytes, EG Dell: 00-14-22 00-14-22-34-B2-C2  
    IP addr
        identify a device on a network, IPv4 or IPv6, unique to internet outside local NAT
    Hostnames
        ties IP to human readable name, EG myhost.com

DHCP Overview (Dynamic Host Configuration Protocol)
    assigns IP addresses, subnet masks and gateways to our machines
    network administrator: takes time to manually assign ip and can do duplicates
    network dhcp server (generally the router): can assign ip to any requsting machine

    DHCP DISCOVER: msg broadcasted to search for a DHCP server.
    DHCP OFFER - The DHCP server in the network replies with an offer message. The offer contains a packet with DHCP lease time, subnet mask, IP address, etc.
    DHCP REQUEST - The client sends out another broadcast to let all DHCP servers know which offer it accepted.
    DHCP ACK - Acknowledgement is sent by the server.
