# Printjack-Phonejack
This repository contains the source code of the printjack and phonejack attacks.

The Printjack directory contains the script to carry out the attack and its support files, that is the file of the ip addresses to be attacked and an example file containing the text that will be printed.

The Phonejack directory contains several scripts. Specifically, the floodDoS.py script is required to carry out the attack on VoIP devices.
To mitigate the DoS attack we have provided the antiDoS.py script, while to mitigate the "audio call eavesdropping" attack there is the enc-dec.py script.

Finally, we provide the iptables.sh file which provides the IPtables configurations for managing packet queues.
