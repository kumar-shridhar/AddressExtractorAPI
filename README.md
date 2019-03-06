# AddressExtractorAPI
## Extract address using the API

Installation
------------

Before using the Python bindings, you must install the libpostal C library. Make sure you have the following prerequisites:

**On Ubuntu/Debian**
```
sudo apt-get install curl autoconf automake libtool python-dev pkg-config
```

**Installing libpostal**

```
git clone https://github.com/openvenues/libpostal
cd libpostal
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make
sudo make install

# On Linux it's probably a good idea to run
sudo ldconfig
```

To install the Python library, just run:

```
pip install postal
```


Usage
-----

```
python app.py
```
It will open the link at localhost:8081
Enter query as: localhost:8081/<query here>

Sample
-----
```
http://0.0.0.0:8081/ Anker Engelunds Vej 1 Bygning 101A, 2800 Kgs. Lyngby, Denmark

Response: [["anker engelunds vej","road"],["1 bygning 101a","house_number"],["2800","postcode"],["kgs. lyngby","city"],["denmark","country"]]
```
