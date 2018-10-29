#!/usr/bin/env python 
import binascii
import struct
# import crypto
from Crypto.Cipher import AES 
import md5
import pprint

def main(database_path, password):
    #lets open the database
    with open(database_path) as file:
        print("Attempting to read the database %s" % database_path)
        pp = pprint.PrettyPrinter(indent=2)

        print("Read the full database file.")
        print("Decrypting ...")

        pp.pprint(decrypt_database(read_encrypted_database(file), password))
        # pp.pprint(database)

def read_encrypted_database(file):
    return {
        'header': _read_header(file),
        'encrypted_data': _read_all_key_value_pairs(file)
    }

def _read_header(file):
    _read_magic(file)
    return {
        "salt": _read_salt(file),
        "iv": _read_iv(file),
        "checksum": _read_encrypted_checksum(file)
    }

def _read_magic(file):
    bytes = file.read(4)
    magic_string = binascii.hexlify(bytes.format())
    if str(magic_string) != "badcab00":
        raise ValueError("Magic bytes %s, were not badcab00, which means its not the correct file type" % magic_string)

def _read_salt(file):
    # < stands for little-endian s = string  (https://docs.python.org/2/library/struct.htm)
    return ''.join(struct.unpack(">4c", file.read(4)))

def _read_iv(file):
    return file.read(16)

def _read_encrypted_checksum(file):
    return file.read(64)

def _read_all_key_value_pairs(file):
    db = {}
    while not file.closed:
        value = _read_key_value(file)
        if(value == None):
            break
        db[value[0]] = {
            "value": value[1],
            "md5-sum": value[2]
        }

    return db

def _read_key_value(file):
    fuck_you = file.read(4)
    if(len(fuck_you) < 4):
        return None
    key_length = struct.unpack(">i", fuck_you)[0]
    # print("Key Length: %d" % key_length)
    # TODO: this is kinda fucked up, i need to fix this.
    key = file.read(key_length-1).decode("utf-8").rstrip()
    # cause why the fuck not.
    file.read(1)
    value_length = struct.unpack(">i", file.read(4))[0]
    value = file.read(value_length) 
    md5_sha = file.read(16)
    return (key, value, binascii.hexlify(md5_sha))

def decrypt_database(database, password):
    if 'header' not in database:
        raise TypeError("File header is needed for database decryption")
    if 'encrypted_data' not in database:
        raise TypeError("Encrypted data is missing for decryption")

    decryptor = _new_decryptor(database['header'], password)

    result = {}

    for key, value in database['encrypted_data'].items():
        try:
            result[key] = _decrypt_value(decryptor, value)
        except ValueError as err:
            print("ERR: hit a snag trying to decrypt [%s] because of %s" % (key, err))

    return result

def _new_decryptor(header, password):
    if 'salt' not in header:
        raise TypeError("4 byte password salt was not found in the header struct")
    if 'iv' not in header:
        raise TypeError("IV bytes were not found in the header struct")
    if 'checksum' not in header:
        raise TypeError("64 byte checksum was not present in the header for decryptor validation")

    decryptor = AES.new(_get_aes_key(header["salt"], password), AES.MODE_CBC, header["iv"])

    _verify_decryptor(checksum= header['checksum'], decryptor= decryptor)

    return decryptor

def _get_aes_key(salt, password): 
    return md5.new(salt + '$' + password).digest()

def _verify_decryptor(checksum, decryptor):
    if len(checksum) is not 64:
        raise ValueError("Checksum NEEDS to be 64 bytes but instead was %d" % len(checksum))

    data = decryptor.decrypt(checksum)
    random_str = data[0 : 32] # 32 byte random string
    digest = data[32 : 48]    # 16 byte digest
    zeroes = data[48 : 64]    # 16 bytes worth of nothing (padding)

    new_digest = md5.new(random_str).digest()
    if new_digest != digest:
        raise ValueError("Either the hash, iv or password is incorrect, because digest %s was not equal to %s" % (new_digest, digest))
    if filter(lambda x: x == 0, zeroes):
        raise ValueError("Either the hash, iv or password is incorrect, because we expected the last 16 bytes of checksum to be all 0 %s" % binascii.hexlify(zeroes))

def _decrypt_value(decryptor, value):
    if 'md5-sum' not in value:
        raise TypeError("Value is missing the md5 digest, for decryption validation")
    if 'value' not in value:
        raise TypeError("Remember that Value is a dict with extra data in it (besides the encrypted part)")
    
    result = decryptor.decrypt(value["value"]).rstrip() # get rid of right padding, because its not in md5
    _verify_md5_digest(value['md5-sum'], result)

    return result

def _verify_md5_digest(expected, value):
    hash = binascii.hexlify(md5.new(value).digest())
    if hash is not expected:
        raise ValueError("The checksum %s, was not equal to %s" % (hash, expected))

if __name__ == "__main__":
    main(database_path="problem/extreme_secret.db", password="uberpass")