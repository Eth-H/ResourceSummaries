# Extract zip files> -----------------------------
import zipfile
# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        print(e)
        pass

zipfilename = 'data.zip'
zip_file = zipfile.ZipFile(zipfilename)
password = "password"
if extractFile(zip_file, password.encode('utf-8')):
	print('*' * 20)
    print('Password found: %s' % password)
    print('Files extracted...')
