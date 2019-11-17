# ViewImg

View images on a remote server through your web browser.

Forked from [rexlee/ImgView](https://github.com/rexlee/ImgView), `next` and `prev` button added in template file.

---

ViewImg provides an alternative to `ssh -X` and other hacks to view a list of images in a directory on a remote server.  It should provide a base level of functionality for researchers in computer vision and image processing.  

To run ViewImg first clone the repo and `cd` into the directory:
```
git clone https://github.com/nicodjimenez/ImgView.git
cd ImgView
```

Then, install the requirements:
```
pip install -r requirements.txt
```

To view images on port `8000` in `path/to/images/` do:
```
python run.py -d path/to/images/
```
To run on a different port, use the `-p` command line argument, for example:
```
python run.py -d path/to/images/ -p 8080
```

To view the images you will need to access your remote server's port.  You can either open up the port, or you can use ssh tunnelling.  If you are running ImgView on port 8000 on remote server `remote` accessible via your ssh config file as `ssh remote`, do:
```
ssh remote -N -L localhost:8000:localhost:8000
```
and point your browser to <http://0.0.0.0:8000/>.


