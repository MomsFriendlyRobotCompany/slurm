# some code taken from here:
# https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python/blob/master/Download-Large-File-from-Google-Drive.ipynb
import requests
import mimetypes


class GoogleDrive:
    # get list of mime types
    mimes = list(mimetypes.types_map.values())

    def url_to_id(self, url):
        x = url.split("/")
        return x[5]

    def download(self, link, destination=None, dumpHeader=False, download=True):
        id = self.url_to_id(link)
        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()
        response = session.get(URL, params = { 'id' : id }, stream = True)

        if dumpHeader:
            print("-------------------------")
            for k,v in response.headers.items():
                print(f"{k}: {v}")
            print("-------------------------")

        if "Content-Length" in response.headers:
            bits = int(response.headers["Content-Length"])
        else:
            bits = None

        if destination is None:
            ct = response.headers["Content-Type"]
            if ct in self.mimes:
                ff = response.headers["Content-Disposition"]
                for s in ff.split(";"):
                    if s.find("filename=") >= 0:
                        destination = s.split("=")[1].replace('"',"")
                if destination is None:
                    raise Exception("No file name found in file")
            elif "Content-Encoding" in response.headers:
                if response.headers["Content-Encoding"] == "gzip":
                    destination = "download.zip"

        token = self.get_confirm_token(response)

        if destination is None:
            raise Exception("File name is None")

        print(f">> file: {destination}  bits: {bits}")

        if not download:
            return

        if token:
            params = { 'id' : id, 'confirm' : token }
            response = session.get(URL, params = params, stream = True)

        self.save_response_content(response, destination)

        return destination

    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
