import hashlib
import json

def hash_string_256(string):
    return hashlib.sha256(string).hexdigest();
def hash_block(block):
    """
    :param block:
    :return: hash version of that block
    """
    # return "-".join([str(block[key]) for key in block])

    return hash_string_256(json.dumps(block, sort_keys=True).encode()) # we need to ensure that the dictionary is ordered; this way we will have same input string for hash
