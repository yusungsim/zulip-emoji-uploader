import os
import zulip
from pathlib import Path
from pprint import pprint

# PARAMS 
# base directory of emoji files
BASE_DIR = '/path/to/emojis'
# path to the zulip config file (zuliprc)
ZULIPRC_PATH = '~/zuliprc'
# print success message on successful emoji upload
PRINT_ON_SUCCESS = True

# preprocess the filename to emoji name
def make_emoji_name(filename):
    return filename


############################################################

# get all emoji file list
# return list of tuples, (path, name)
def get_emojis():
    # iterate over files
    emojis = []
    for filename in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, filename)
        if os.path.isfile(path):
            emojis.append((path, filename))

    # filter out non-image files by extension(.gif, .png)
    emojis = [(path, make_emoji_name(name)) for (path, name) in emojis 
             if (path.endswith('.gif') or path.endswith('.png'))]

    return emojis


# add emojis to zulip server
def upload_emoji_list(emojis):
    client = zulip.Client(config_file=ZULIPRC_PATH)

    for (path, emoji_name) in emojis:
        # use zulip REST API to add
        # refer to https://zulip.com/api/upload-custom-emoji
        with open(path, "rb") as fp:
            result = client.call_endpoint(
                f"realm/emoji/{emoji_name}",
                method="POST",
                files=[fp],
            )
            if result['result'] != 'success':
                print('ERROR on uploading emoji file: ', path)
                print(result)
            else:
                if PRINT_ON_SUCCESS:
                    print('SUCCESS uploading emoji file: ', path)

############################################################

# main
if __name__ == '__main__':
    emojis = get_emojis()

    # prompt
    print('Will upload emojis : ')
    for s in [f"->Path: {str(path)}\n  Name: {name}\n" for (path, name) in emojis]:
        print(s)

    a = input("Type 'y' to continue, other to abort : ") 
    if a == 'y':
        upload_emoji_list(emojis)
    else:
        print('Aborting...')
