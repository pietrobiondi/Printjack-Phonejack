iptables -A FORWARD -p UDP -d PhoneAddress --dport 5060 -j NFQUEUE --queue-num 1

iptables -A FORWARD -p UDP -s IPPhoneAddress --sport rangeRTPport -j NFQUEUE --queue-num 2  

iptables -A FORWARD -p UDP -d PhoneAddress --dport rangeRTPport -j NFQUEUE --queue-num 3   
