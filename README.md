# Project Name

chrtme : chroot me (please!)

## Installation

Requirements :

1. Python 3.x

## Usage

```
usage: chrtme.py [-h] [-v] [-d] [-f] [-t TMP] [-l LOCATION] [-r] [-k]
                 image cmd [cmd ...]

chrtme - chroot me is a management tool for chroot enviroments.
    

positional arguments:
  image                 specify the image URL or location. The image should be
                        a .tar file, possibly compressed with gzip, bzip or xz
  cmd                   Specify command to be run inside the chroot. If "-"
                        chars are present use "--" before specifying the
                        command

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --debug           Enable debugging info
  -f, --force           Force script execution, besides warnings (eg: not
                        running script as root)
  -t TMP, --tmp TMP     Specify temp directory to be used during the image
                        download. Default "/tmp/rootfs.tmp"
  -l LOCATION, --location LOCATION
                        Specify the target directory to extract the downloaded
                        image. Default "./rootfs/"
  -r, --rm              Remove chroot directory after executing the task
  -k, --keeptmp         Keep the downloaded image temporary file after the
                        script exits
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

* 20160503 - 0.0.4 - Changed chroot cleaning behavior to support local existing files usage
* 20160503 - 0.0.3 - Fixed issues with tmp files/dir handling
* 20160502 - 0.0.2 - Added basic script functionality
* 20160501 - 0.0.1 - Initial commit - basic script structure and help message

## Credits

Author: Emanuele 'Lele' Calo' (eldios)

## License

The MIT License (MIT)

Copyright (c) 2016 - Emanuele 'Lele' Calo'

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
