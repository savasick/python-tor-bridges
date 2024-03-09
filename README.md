# python through tor with bridges

### install
```bash
sudo apt update -y
sudo apt install tor torsocks torbrowser-launcher obfs4proxy -y
```

start torbrowser-launcher and install browser\
configure time/timezone at machine\
start tor browser -> configure connection -> request a bridge or write this bot <a href="https://t.me/GetBridgesBot"> @GetBridgesBot</a> to get BRIDGES\

start tor
```bash
sudo systemctl status tor
sudo systemctl start tor
```

go to /etc/tor/torrc
```bash
sudo nano /etc/tor/torrc
```

and add this to file with ur bridges
```bash
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
UseBridges 1
Bridge obfs4 IP:PORT FINGERPRINT cert=CERTIFICATE iat-mode=0
Bridge obfs4 IP:PORT FINGERPRINT cert=CERTIFICATE iat-mode=0

# more like this

ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
UseBridges 1
Bridge obfs4 49.13.85.208:43809 B60644EF12A01CEE1ED38E3FA90FC42A4C787E6B cert=5q8QalWBRIF5uBiCpiTdEBwAqboWSr21GqG2aiqr7NJe+vO8XUFsxsziZ6vmUDBMBaodQQ iat-mode=0
Bridge obfs4 49.13.85.208:43809 B60644EF12A01CEE1ED38E3FA90FC42A4C787E6B cert=5q8QalWBRIF5uBiCpiTdEBwAqboWSr21GqG2aiqr7NJe+vO8XUFsxsziZ6vmUDBMBaodQQ iat-mode=0
```

restart tor
```bash
sudo systemctl restart tor
```


#

### usage

get requests lib
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```


check tor connection from https://check.torproject.org/
```bash
torsocks python3 tor.py
```

get page
```bash
torsocks python3 page.py
```

### change ip to tor
```bash
sudo systemctl restart tor
```

for experiment use without torsocks
```bash
python3 tor.py
```