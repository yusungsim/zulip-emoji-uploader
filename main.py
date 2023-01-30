import os
import zulip
from pathlib import Path
from pprint import pprint

# PARAMS 
# base directory of emoji files
BASE_DIR = 'path/to/emoji_dir'
# path to the zulip config file (zuliprc)
ZULIPRC_PATH = '~/zuliprc'
# print success message on successful emoji upload
PRINT_ON_SUCCESS = True

# preprocess the filename to emoji name
# this example preprocesses the name of blob emojis,
# downloaded from here : https://nqn.blue/packs/BlobEmoji
def make_emoji_name(filename):
    # strip extension
    name = str(Path(filename).with_suffix(''))

    if name.startswith('ablob'):
        return name.replace('ablob', 'ablob ', 1)
    elif name.startswith('blob'):
        return name.replace('blob', 'ablob ', 1)
    else:
        return 'ablob_' + name

############################################################

# get all emoji file list
def read_files():
    # iterate over files
    files = []
    for filename in os.listdir(BASE_DIR):
        if os.path.isfile(filename):
            files.append(filename)

    # filter out non-image files by extension(.gif, .png)
    files = [f for f in files if (f.endswith('.gif') or f.endswith('.png'))]

    return files


# add emojis to zulip server
def upload_emoji_list(files):
    client = zulip.Client(config_file=ZULIPRC_PATH)

    for filename in files:
        # use function to make emojiname from filename
        emoji_name = make_emoji_name(filename)

        # use zulip REST API to add
        # refer to https://zulip.com/api/upload-custom-emoji
        with open(filename, "rb") as fp:
            result = client.call_endpoint(
                f"realm/emoji/{emoji_name}",
                method="POST",
                files=[fp],
            )
            if result['result'] != 'success':
                print('ERROR on uploading emoji file : ', filename)
                print(result)
            else:
                if PRINT_ON_SUCCESS:
                    print('SUCCESS uploading emoji file : ', filename)

############################################################

# main
if __name__ == '__main__':
    files = read_files()
    upload_emoji_list(files)
