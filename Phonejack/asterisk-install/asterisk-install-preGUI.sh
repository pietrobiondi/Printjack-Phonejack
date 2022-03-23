cd /opt
git clone -b 18 https://gerrit.asterisk.org/asterisk asterisk-18

cd asterisk-18/ 
contrib/scripts/get_mp3_source.sh 
contrib/scripts/install_prereq install

./configure

make menuselect