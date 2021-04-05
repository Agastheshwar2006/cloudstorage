import dropbox
class upload_file :
    def __init__(self,access_token):
        self.access_token+access_token
    
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(filefrom,"rb") 
        dbx.files_upload(f.read(), fileto, mode=WriteMode('overwrite'))


def main():
    access_token="9taVwdSKzFUAAAAAAAAAAViqGHB_gOiLzdghbtwMzUtyUMZjEFpseec9RbncK__6"
    transferData=TransferData(access_token)
    filefrom=input("enter the file path to transfer: ")
    fileto=input("enter the path to upload to dropbox: ")
    transferData.upload_file(filefrom,fileto)
    print("file has been moved")
    
main()