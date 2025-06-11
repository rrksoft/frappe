# Update and Upgrade
sudo apt update -y
sudo apt upgrade -y

# Add user
sudo adduser shaibal
sudo usermod -aG sudo shaibal
su shaibal 
cd /home/shaibal/

# Install Package
sudo apt install software-properties-common git curl whiptail -y

sudo apt -qq install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
        libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y && \
    wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz && \
    tar -xf Python-3.10.11.tgz && \
    cd Python-3.10.11 && \
    ./configure --prefix=/usr/local --enable-optimizations --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" && \
    make -j "$(nproc)" && \
    sudo make altinstall && \
    cd .. && \
    sudo rm -rf Python-3.10.11 && \
    sudo rm Python-3.10.11.tgz && \
    pip3.10 install --user --upgrade pip 
 
sudo apt install git python3-dev python3-setuptools python3-venv python3-pip redis-server -y

sudo apt install fontconfig libxrender1 xfonts-75dpi xfonts-base -y

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_amd64.deb
sudo apt-get install libjpeg-turbo8
sudo dpkg -i wkhtmltox_0.12.6.1-3.jammy_amd64.deb
sudo cp /usr/local/bin/wkhtmlto* /usr/bin/ 
sudo chmod a+x /usr/bin/wk*
sudo rm  wkhtmltox_0.12.6.1-3.jammy_amd64.deb
sudo apt --fix-broken install -y
sudo apt install fontconfig xvfb libfontconfig xfonts-base xfonts-75dpi libxrender1 -y

# Install MariaDB
sudo apt install mariadb-server mariadb-client -y

# Install Packages
sudo apt install pkg-config default-libmysqlclient-dev -y

# MariaDB Secure Installation
sudo mariadb-secure-installation

# MySQL script
sudo bash -c 'cat << EOF >> /etc/mysql/my.cnf
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
EOF'

# Restart MySQL
sudo service mysql restart

#Install more apps
sudo apt install curl
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.profile
nvm install 18
sudo apt-get install npm
sudo npm install -g yarn

#Setup Python environment
sudo python3 -m pip config --global set global.break-system-packages true
sudo apt install python3-pip -y

#Install Frappe Bench
sudo pip3 install frappe-bench

#Init Frappe branch Version 15
bench init --frappe-branch version-15 frappe-bench
cd frappe-bench/
sudo chmod -R o+rx /home/shaibal/

#Setup new site
bench new-site erpnet.rrksoft.com
redis-server --port 11000 --daemonize yes --bind 127.0.0.1
redis-server --port 12000 --daemonize yes --bind 127.0.0.1
redis-server --port 13000 --daemonize yes --bind 127.0.0.1

#Setup ERPNext
bench get-app --branch version-15 erpnext && \
bench --site erpnet.rrksoft.com install-app erpnext

bench get-app crm && \
bench --site rrksoft.local install-app crm

bench get-app hrms && \
bench --site rrksoft.local install-app hrms

bench version --format table



sudo bench setup production shaibal



bench --site rrksoft.local scheduler enable && \
bench --site rrksoft.local scheduler resume && \
bench --site rrksoft.local set-maintenance-mode off



sudo systemctl restart redis-server

bench setup nginx


sudo bench setup production shaibal


bench get-app https://github.com/frappe/lms && \
bench --site rrksoft.local install-app lms

bench get-app builder && \
bench --site rrksoft.local install-app builder

bench get-app https://github.com/frappe/helpdesk && \
bench --site rrksoft.local install-app helpdesk


bench get-app gameplan
bench --site rrksoft.local install-app gameplan
bench --site rrksoft.local add-to-hosts


bench get-app https://github.com/frappe/wiki && \
bench --site rrksoft.local install-app wiki
bench --site rrksoft.local add-to-hosts

bench get-app drive --branch main 
bench --site rrksoft.local install-app drive

bench get-app education
bench --site rrksoft.local install-app education

bench get-app print_designer
bench --site rrksoft.local install-app print_designer



