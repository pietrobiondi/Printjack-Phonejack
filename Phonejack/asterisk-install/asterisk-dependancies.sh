apt-get install build-essential git autoconf wget subversion pkg-config libjansson-dev libxml2-dev uuid-dev libsqlite3-dev libtool -y

cd /opt 
git clone -b next git://git.asterisk.org/dahdi/linux dahdi-linux

cd dahdi-linux 
make 
make install

cd /opt 
git clone -b next git://git.asterisk.org/dahdi/tools dahdi-tools

cd dahdi-tools 
autoreconf -i 
./configure 
make install 
make install-config 
dahdi_genconf modules

git clone https://gerrit.asterisk.org/libpri libpri 
cd libpri

make
make install