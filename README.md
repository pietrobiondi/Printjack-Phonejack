# Printjack-Phonejack
This repository contains the source code of the printjack and phonejack attacks.

The Printjack directory contains the script to carry out the attack and its support files, that is the file of the ip addresses to be attacked and an example file containing the text that will be printed.

The Phonejack directory contains several scripts. Specifically, the floodDoS.py script is required to carry out the attack on VoIP devices.
To mitigate the DoS attack we have provided the antiDoS.py script, while to mitigate the "audio call eavesdropping" attack there is the enc-dec.py script.

Finally, we provide the iptables.sh file which provides the IPtables configurations for managing packet queues.



PRINTJACK:
DoS
1) Connect the device to the network where the network printer is present and change the IPs.txt file with the IP address of the printer.

2) Edit the bot.txt file with the text you want to print during the attack.



PHONEJACK:

DoS

0) N.B In the VM that we provide, the asterisk server and the configuration of voip phones (step 1 and 2 ) is already done.
1) Read "README-Asterisk.txt" and follow instructions.
2) After that, open the directory "conf voip phones" and read "conf-phones" and follow instructions.
3) Install dependencies of the voip phones dos attack.
4) Exec the script dos.py

Link to the IoTVM.ova [[Link]](https://mega.nz/file/nANFkA5D#WpUe4Tg-gTMbsqL40tF4ff9t95kI5anCr1BvCCHCp6k)
