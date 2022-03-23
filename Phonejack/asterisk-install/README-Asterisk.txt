Exec asterisk-dependancies.sh

Exec asterisk-install-preGUI.sh


FROM THE GUI:

Select enable-addons --> select chan_mobile and + chan_ooh323

Select core sound packages --> Select CORE-SOUNDS-EN-WAV + ULAW + ALAW + GSM + G729 + G722

Select MOH package --> Select MOH-OPSOUND-WAV + ULAW + ALAW + GSM + G729 + G722

Select extra sound packages --> Select EXTRA-SOUNDS-EN-WAV + ULAW + ALAW + GSM + G729 + G722

Select Save and exit.

Exec asterisk-install-afterGUI.sh


___AFTER INSTALL__

cd /etc/asterisk

And copy sip.conf , pjsip.conf, extension.conf form the directory /conf TO /etc/asterisk

Then restart asterisk with sudo systemctl restart asterisk


