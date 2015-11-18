# ViewImg

ViewImg provides an alternative to `ssh -X` and other hacks to view a list of images on a remote server.
To run ViewImg first clone the repo:
```
git clone https://github.com/nicodjimenez/ImgView.git
```

Then install the requirements:
```
pip install -r requirements.txt
```

To view images on port `8000` in `path/to/images/` do:
```
python run.py -d path/to/images/
```
which runs by default on port 8000.  To run on a different port, use the `-p` command line argument, for example:
```
python run.py -d path/to/images/ -p 8080
```

To view the images you will need to access your remote server's port.  You can either open up the port, or you can use ssh tunnelling.  If you are running ImgView on port 8000 on remote server `remote` accessible via your ssh config file as `ssh remote`, do:
```
ssh remote -N -L localhost:8000:localhost:8000
```
and point your browser to <http://0.0.0.0:8000/>.


