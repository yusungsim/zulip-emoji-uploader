# Zulip emoji bulk uploader

This script uploads all emoji files in a given directory to
the [Zulip](https://zulip.com/) server.

# Prerequisitory

## Zulip API key

Get your Zulip API key referring to the 
guide [here](https://zulip.com/api/api-keys).
Download the `zuliprc` config file and save somewhere accessible
(e.g. `~/zuliprc`).

**Always be careful to securely save your own API key!**

## Python dependencies

The script requires several Python dependencies such as 
[Zulip API Python bindings](https://zulip.com/api/configuring-python-bindings).
Refere to the Usage section to use the venv and install the dependencies.

# Usage

1. Clone this repository.

```sh
git clone git@github.com:yusungsim/zulip-emoji-uploader.git
cd zulip-emoji-uploader
```

2. Initialize the Python venv and install dependencies.

```sh
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

3. Configure the parameters in `main.py`.

Set `BASE_DIR` as path to the directory your emoji files exist.
Set `ZULIPRC_PATH` as path to the Zulip configure file (`~/zuliprc`).
If you want to skip the success messages, set the `PRINT_ON_SUCCESS` to `False`.

```python
# PARAMS 
# base directory of emoji files
BASE_DIR = 'path/to/emoji_dir'
# path to the zulip config file (zuliprc)
ZULIPRC_PATH = '~/zuliprc'
# print success message on successful emoji upload
PRINT_ON_SUCCESS = True
```

4. Run the script

```sh
python3 main.py
```
