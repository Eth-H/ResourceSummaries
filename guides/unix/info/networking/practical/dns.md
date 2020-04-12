# DNS (Domain Name System)
    distributed database of human readable hostnames to machine IP addrs
    ppl manage ther db, so domains can then talk and form a internet contact list

    name server
        load DNS settings/configs and ans questions from clients asking what domain is what ip
        server has the dns records?
        if a name server is {}
            authoritative: holds the actual dns records you want
            recursive: redirect to anouther name server, or caches dns records obtained from anouther server
    zone file
        how to info about domain or how to get to it if it doesnt know
        comprised of entries of resource records
            each line is a record
                fields

    patty  00:60:00  IN  A      192.168.0.4 
    record name
    TTL - time after which we refresh a record, in DNS TTL is denoted by time, react to hosts constantly changing ip addrs maps
    Class - Namespace of the record info, IN = Internet
    Type - Type of info stored in the record data. A=address, MX=mail exchanger, ...
    Data - can contain an IP address if it's an A record or something else depending on the record type

    DNS Process
        Local DNS Server (generally isp)
            sends to root server
        root server
            13 exist, mirrored and distributed worldwide
            send us to top level domain server matching dns name
        Top-Level Domain
            .org, .com, .net, ...
            provide us cached record or send us to anouther name server
        Authoritative DNS Server
            has zone file for target domain and there is a resource record for its host            returns matched ip addr


## /etc/hosts
    contains mappings of some hostnames to IP addresses
    block/allow
        can map domain to 0.0.0.0, or add to /etc/hosts.deny or /etc/hosts.allow
        better to use firewall
    /etc/resolv.conf 
        used to contain dns name servers for quicker lookups, now irrelevant as dns is fast

## dns servers

BIND (Berkeley Internet Name Domain)
    most popular DNS server, linux distro standard, powerfull and flexibilble
DNSmasq
    Lightweight and easier to configure than BIND, comes with needed tools to setup DHCP and DNS

PowerDNS
    Full-featured but some more options than BIND, reads info from multiple dbs (MySQL, psql, ...)

DNS Tools
    lookup name servers
        nslookup (name server lookup)
            nslookup www.google.com
        dig (domain info groper)
            //more options
            dig www.google.com
        whois
            //lookup whois database
            whois www.google.com


