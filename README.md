# Codepad

Codepad is a simple text editor built with Python and Qt.

- **Simple:** Easily edit text **without distractions**
- **Lightweight:** Clean UI **without unnecessary features**
- **Fast:** Built on Qt, a **fast and lightweight** UI framework

## Installation

Binaries for Codepad are currently only available for macOS. However, it is to build Codepad from source.

### macOS or Linux

```shell
$ git clone https://github.com/HereIsKevin/codepad.git
$ cd ./codepad/
$ python3 -m venv ./venv/
$ source ./venv/bin/activate
$ pip3 install --requirement ./requirements.txt
$ python3 ./build.py
```

### Windows

```powershell
> git clone https://github.com/HereIsKevin/codepad.git
> cd .\codepad\
> py -3 -m venv .\venv\
> .\venv\Scripts\Activate.ps1
> py -3 -m pip install --requirement .\requirements.txt
> py -3 ./build.py
```

After the build script finishes, you should find the executable in the `dist` folder.

## Contributing

Pull requests are welcome. For major changes or new features, please open an issue first.

## License

[GPLv3](https://github.com/HereIsKevin/codepad/blob/master/LICENSE)
