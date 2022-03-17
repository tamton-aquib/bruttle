
# Bruttle

A small script to bruteforce pdf, zip, and some popular hashes. <br />
You can find the improved rust version of this script [here](https://github.com/tamton-aquib/veldora).


### Installation:
```bash
git clone https://github.com/tamton-aquib/bruttle.git
cd bruttle
pip3 install -r requirements.txt
```

### Usage:
```bash
python3 bruttle.py <file/hash> <wordlist>
```

### Features:
- Less than 100 lines of code.
- List of hashes include md5,sha1,sha224,sha256,sha384,sha512 (for now).
- Filetypes include zip, pdf (for now)
- Automatic filetype and/or hash detection.

### Showcase:
![noice](https://user-images.githubusercontent.com/77913442/131712946-5aa50471-5b94-4f0c-97ff-08928c9e0316.gif)

### Notes:
* Get password lists from [here](https://github.com/kkrypt0nn/Wordlists)
* To create custom passlist, try: [cupp.py](https://github.com/Mebus/cupp)
* As always, not to be used for illegal purposes  : )
