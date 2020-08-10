# theory
## filters packets based on
    tables: files that join similar actions. consists of several chains
    chains: string of rules. when a packet is received
    rules: statement that tells the system what to do with a packet. rules can block/forward different types of packets
    targets/actions/jumps
        decision of what to do with a packet after it matches a rule.
        non-terminating: keep matching packets against rules even if they have matched
        terminating: immediately evaluate and dont match again
            accept it (allow through) / drop it (ignore) / reject it (sends an err back to the sender), return (send back to originating chain to match other rules)
    iptables finds the appropriate table, then runs it through the chain of rules until it finds a match

## default tables
    filter
        most used, decide on allowed packets
        chains
            input: received packets
            output: outbound traffic
            forward: routed packets
    NAT (Network Address Translation)             
        routing to networks that cannot be accessed directly, dest/src of packets needs altering
        prerouting – assigns packets as soon as the server receives them
        output – same as filters output
        postrouting – allow making changes to packets after they leave the output chain
    mangle
        adjusts IP header props of packets
        prerouting, postrouting, output, input, forward
    raw
        exempt packets from connection tracking 
        prerouting, output
    security (optional)
        manage special access rules
        input, output, forward
        

# setup
## get
sudo apt-get install iptables
sudo apt-get install iptables-persistent
## disable firewalld iptables frontend if installed (rhel)
    sudo systemctl stop firewalld
    sudo systemctl disable firewalld
    sudo systemctl mask firewalld

# use
    //cmds default to the filters table
    // append / check requirements / delete - rule to/against/from chain
    iptables [-t table]? [-A|-C|-D] chain rule-specification

    //list
    iptables -L --line-numbers

## EGs
//enable loopback traffic
sudo iptables –A INPUT –i lo –j ACCEPT
// only allow traffic from specific port
sudo iptables –A INPUT –p tcp ––dport 22 –j ACCEPT
// drop specific ip
sudo iptables –A INPUT –s 192.168.0.27 –j DROP
// reject range of ips
//-m: match specified option, -iprange: expect range of ip addrs
sudo iptables –A INPUT –m iprange ––src–range 192.168.0.1–192.168.0.255 -j REJECT
//drop all traffic not matched by other rules
sudo iptables –A INPUT –j DROP

// del all rules
    sudo iptables -F
// del a rule
    sudo iptables -D INPUT [ruleNum]
// save changes debian/redhat
    sudo /sbin/iptables–save
    sudo /sbin/service iptables save
