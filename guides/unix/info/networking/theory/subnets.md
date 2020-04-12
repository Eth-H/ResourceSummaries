IPv4
    204.23.124.23
        4 octets size, 1 octet = 8 bits = 1 byte
            2^8 combinations per octet (0-255)
        first 2 bytes = network prefix/portion: network its on
        last 2 bytes = host portion: which host on that network

subnet
    group of hosts with similar ips, generally in same area
    divided into a network prefix and a subnet mask
    subnet mask
        used to work out network prefix size so can find out what devices is on what subnet
        255.255.255.0
        denote (with network prefix)
            123.234.0.0/255.255.0.0 
    to connect to hosts on anouther subnet need to connect them
        talk to router 192.168.1.1 (generally addr 1 of subnet)
        one of the routers port will connect to anouther subnet
        though for private networks NAT is needed
    adv
        segment networks and control local traffic flow

    subnet math (num hosts can connect to)
        each 1 masks (hides) the corresponding ip bit
        num of 1s dictates size of network prefix (so the remaining is hosts)
        EG
            192.168.1.165  = 11000000.10101000.00000001.10100101
            255.255.255.0  = 11111111.11111111.11111111.00000000
            256 options-broadcast addr host and subnet addr host = 254
            possible ips
                192.168.1.1 - 192.168.1.254.
        quicker conversions (for by hand intervew questions)
            2^4 = 16, 2^8 = 256, 2^12 = 4096
            1   1  1  1  1 1 1 1
            128 64 32 16 8 4 2 1
            use chart for binary <-> decimal

CIDR (classless inter-domain routing)
    represent a subnet mask compactly
    10.42.3.0/255.255.255 -> 10.42.3.0/24 first 24 bits masked
    32 total num bots - 24 = 8
    num possible connections
        so 2^24 subnets 2^8 hosts

NAT (network address translation)
router act as an intermediary between the Internet and private network
    so its ip repersents a lot of computers
    router opens a connection to your req domain and sends your req

IPv6
    2dde:1235:1256:3:200:f8ed:fe23:59cf
    8 groups of 16bits/2bytes, 128bits/16bytes sizes
    2001:d00::/24 
        24 bits of under subnet mask
    values
        2001:d00:: to 2001:0dff:ffff:ffff:ffff:ffff:ffff:ffff 	
        possible connections
        1,099,511,627,776 subnets
        20,282,409,603,651,670,423,947,251,286,016 hosts
