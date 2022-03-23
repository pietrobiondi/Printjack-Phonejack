cd /opt/asterisk-18
make -j2

make install

make samples 
make basic-pbx

make config

ldconfig

systemctl start asterisk

systemctl enable asterisk