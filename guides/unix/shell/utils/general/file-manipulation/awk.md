# notes
    each newline = a new input record
    each space/tab = a field
    access fields of current line with $0,$1,...

# examples
```awk
    # search 9th field for 404
    awk ‘$9 ~ /404/ { print }’ access.log

    awk ‘1 == 1 && (2 == 2 || 2 == 3) { print “True” }’ test.txt
    awk '$9 ~ /200/ && $6 ~ /GET/ { print }' access.log
    # print alternating true/false on each file line
    awk '{if (myvar == "True") {print "True"; myvar = “False”} else {print "False"; myvar = "True" }}' file.txt
    # run code before and after awk processes input records
    awk ‘BEGIN { CODE } /SEARCH/{ print STATEMENT } END { CODE }’ file.txt
    awk ‘BEGIN { ORS = ”\n\n”; print “Open ports found:”} /\/open/{print $5 portcount++} END {print “Parsing done. ” portcount “ ports found.”}’ portscan.gnmap

    awk 'BEGIN { for (x=0; x <= 255; x++) {print "192.168.1."x} }'
    awk 'BEGIN { x = 0 while (x <= 255) {print "192.168.1."x x++} }'
    do {actions} while (condition)

    # break innermost loop
    break
    # skip rest of code in current iteration
    continue
    # quit awk
    exit
    # arrays like python dictionaries
    array[index]
    delete array[index]
    awk '{name[$2]++} END{for (each in name) {print each " clicked " name[each] " time(s)"}}' phishlog.txt
    # sys vars
        #FS — field separator (default: space(s) or tabs)
        #RS — record separator (default: newline)
        #NF — number of fields in the record
        #NR — number of the current record
        #OFS — output field separator
        #ORS — output record separator
        # multiline matching (treat multiple lines as the same record)
            #FS=newline, RS=blank line
            awk 'BEGIN {FS="\n"; RS=""} {print $1}' textfile.txt
            awk 'BEGIN{RS=""; FS="\n"} {split($1,a," "); host[a[5]] = 0; for (i=1; i<=NF; i++) if (match($i,"open") != 0) host[a[5]]++} END{for (each in host) print each " - " host[each]}' scan.nmap
    # call script, allowing for multiple rulesets
        awk -f myscript.awk inputfile.txt




```
