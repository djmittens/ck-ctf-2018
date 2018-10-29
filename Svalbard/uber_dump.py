import uber_db
# Useful for command line arguments.
import argparse
import binascii

from functools import partial

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("FILE", help="uber database file to dump")
  parser.add_argument('-d', '--dirname', default="files", help="Output directory, to place the files in")
  parser.add_argument('-p', '--password', required=True, help="Password to use for database decryption")
  parser.add_argument('-V', '--validate', action="store_true", help="Validate the decrypted files before dumping")
  parser.add_argument('-u', action="store_true", help ="dump the files into a utf-16 encoding such as \\uxxxx\\uxxxx\\uxxxx")

  args = parser.parse_args()

  with open(args.FILE, mode='r') as file: 
    database = uber_db.read_encrypted_database(file)

    if 'header' not in database:
      raise ValueError("Parsed database is missing a header necessary for decryption")

    if 'encrypted_data' not in database:
      raise ValueError("Database is missing the encrypted data to dump")

    print("Loaded the database.")

    decryptor = uber_db._new_decryptor(database['header'], args.password)

    print("Verified the password")

    files = _map_encrypted_data(database['encrypted_data'], partial(_decrypt_data, args.validate, decryptor))

    print("Decrypted files that were found")
    _write_all_files(files, args.dirname)

    print("Finished dumping data to disk")


def _map_encrypted_data(data, func_decrypt):
  return map(lambda x: (x[0] + '-' + x[1]['md5-sum'] + '.json', func_decrypt(x[1])), data.items())

def _decrypt_data(shouldValidate, decryptor, data):
  result = decryptor.decrypt(data['value']) if not shouldValidate else uber_db._decrypt_value(decryptor, data)
  # try:
  #   result = str(result)
  # except UnicodeDecodeError as err:
  #   print("ERR: tried to decode file data as UTF-16 but failed %s" % err)

  return result 

def _write_all_files(files, directory):
  for file in files:
    _write_file(directory + '/' + str(file[0]), file[1])
  
def _write_file(file, data):
  with open(file, mode='w') as file:
    file.write(data)

if __name__ == "__main__":
  main()