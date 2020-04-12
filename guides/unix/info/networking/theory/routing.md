router
    lan ports
        connect multiple devices on same network (LAN)
    uplink port
        connect to WAN

addr routes
    use network B to get to network A
    if not set route for specifc dest use default route
    get routes from routing table
hops
    measure rough distance source to dest for packet
    EG A -> router -> router -> B, 2 hops A to B

diff between Switching, Routing & Flooding

    packet switching: receiving, processing and forwarding data to the dest device
    routing: process of creating the routing table, allowing better switching
    flooding
        was used before routing
        if a router don't know which way to send a packet than every incoming packet is sent through every outgoing link except the one it arrived on

Routing Table
    sudo route -n
        Kernel IP routing table
        Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
        0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
        192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0

        0.0.0.0 = unknown addr, routing table dont know where it goes so routes to gateway

    gateway: gateway to anouther network
    genmask: subnet mask (figure out which ip addr match that dest)
    flags: UG, G: network is up - and is a gateway,
    Iface: interface packet will be going out of

Path of a Packet
    local network
        1 local machine compares the dest ip to see if its in the same subnet by looking at its subnet mask
        2 packet needs source/dest mac and ip to be sent, we need to dest mac
        3 use arp to broadcast a request on the local network to find the mac of the destination host
    outside network
        1 local machine compare dest ip, since its outside of our network: does not see the mac addr of the dest host and cant use arp
        2 packet looks at the routing table, need dest ip so gets it from default gateway (another router). Still need dest mac, sends an arp req to get mac of the default gateway
        3 the router confirms the packets dest mac, it keeps looking at the routing table (2) to forward the packet to another ip that can help the packet move along to its dest. everytime the packet moves, it strips the old source/dest macs and updates the packet with the new source/dest macs
        4 once packet forwarded to the same network, use arp to find the final dest mac address
        during this process, our packet doesn't change the source/dest ips.

Routing Protocols
    help sys adapt to network changes, learns different routes -> builds them -> routes packets that way
    RP types: distance vector and link state
    convergence: when using RPs routers exchange network info, once agreed every routing table maps out the complete network topology (converging). Changes tmp break it until all routers aware

    Distance Vector Protocols
        determine other network paths using hop count
        EG A -> router -> router -> B next to C, assume C 3 hops from A
        choose routes with least amount of hops
        dis adv
            over larger networks periodically sending entire routing table is slow
            inefficient, least hops may not be most efficient route
        RIP (Routing Information Protocol)
            broadcasts the routing table to every router in the network every 30 secs, RIP limits it's hop count to 15 to reduce strain
    Link State Protocols
        complex but converge quickly (suits larger networks)
only send updates to neighboring routes
use a diff algorithm to calc shortest path first and construct their network topology as a graph to show which routers are connected to other routers
        OSPF (Open Shortest Path First)
            only updates the routing tables on a network change, no hop limit

BGP (Border Gateway Protocol)
    collect and exchange routing information among autonomous systems (unis,isps,...)
    routes between these AS instead of inside
    to leave a AS network packet sent to BG router

