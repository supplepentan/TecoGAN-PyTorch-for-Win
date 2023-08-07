import os
import gdown
import zipfile
import sys


def download_file(data_dir, file_id, file_name):
    url = f"https://drive.google.com/uc?id={file_id}"
    output = os.path.join(data_dir, f"{file_name}.zip")
    gdown.download(url, output, quiet=False)


def check_md5(file_path, md5):
    import hashlib

    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    if md5 != hash_md5.hexdigest():
        print(f"!!! Fail to match MD5 sum for: {file_path}")
        print("!!! Please try downloading it again")
        exit(1)


def extract_zip(file_path, data_dir):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(data_dir)
    os.remove(file_path)


# Vid4 GT
if not os.path.exists("./data/Vid4/GT"):
    data_dir = "./data/Vid4"
    file_id = "1T8TuyyOxEUfXzCanH5kvNH2iA8nI06Wj"
    md5 = "d2850eccf30092418f15afe4a7ea27e5"

    print(">>> Start to download [Vid4 GT] dataset")

    os.makedirs(data_dir, exist_ok=True)
    download_file(data_dir, file_id, "GT")
    check_md5(os.path.join(data_dir, "GT.zip"), md5)
    extract_zip(os.path.join(data_dir, "GT.zip"), data_dir)

# ToS3 GT
if not os.path.exists("./data/ToS3/GT"):
    data_dir = "./data/ToS3"
    file_id = "1XoR_NVBR-LbZOA8fXh7d4oPV0M8fRi8a"
    md5 = "56eb9e8298a4e955d618c1658dfc89c9"

    print(">>> Start to download [ToS3 GT] dataset")

    os.makedirs(data_dir, exist_ok=True)
    download_file(data_dir, file_id, "GT")
    check_md5(os.path.join(data_dir, "GT.zip"), md5)
    extract_zip(os.path.join(data_dir, "GT.zip"), data_dir)

if sys.argv[1] == "BD":
    # Vid4 LR BD
    if not os.path.exists("./data/Vid4/Gaussian4xLR"):
        data_dir = "./data/Vid4"
        file_id = "1-5NFW6fEPUczmRqKHtBVyhn2Wge6j3ma"
        md5 = "3b525cb0f10286743c76950d9949a255"

        print(">>> Start to download [Vid4 LR] dataset (BD degradation)")

        download_file(data_dir, file_id, "Gaussian4xLR")
        check_md5(os.path.join(data_dir, "Gaussian4xLR.zip"), md5)
        extract_zip(os.path.join(data_dir, "Gaussian4xLR.zip"), data_dir)

    # ToS3 LR BD
    if not os.path.exists("./data/ToS3/Gaussian4xLR"):
        data_dir = "./data/ToS3"
        file_id = "1rDCe61kR-OykLyCo2Ornd2YgPnul2ffM"
        md5 = "803609a12453a267eb9c78b68e073e81"

        print(">>> Start to download [ToS3 LR] dataset (BD degradation)")

        download_file(data_dir, file_id, "Gaussian4xLR")
        check_md5(os.path.join(data_dir, "Gaussian4xLR.zip"), md5)
        extract_zip(os.path.join(data_dir, "Gaussian4xLR.zip"), data_dir)

elif sys.argv[1] == "BI":
    # Vid4 LR BI
    if not os.path.exists("./data/Vid4/Bicubic4xLR"):
        data_dir = "./data/Vid4"
        file_id = "1Kg0VBgk1r9I1c4f5ZVZ4sbfqtVRYub91"
        md5 = "35666bd16ce582ae74fa935b3732ae1a"

        print(">>> Start to download [Vid4 LR] dataset (BI degradation)")

        download_file(data_dir, file_id, "Bicubic4xLR")
        check_md5(os.path.join(data_dir, "Bicubic4xLR.zip"), md5)
        extract_zip(os.path.join(data_dir, "Bicubic4xLR.zip"), data_dir)

    # ToS3 LR BI
    if not os.path.exists("./data/ToS3/Bicubic4xLR"):
        data_dir = "./data/ToS3"
        file_id = "1FNuC0jajEjH9ycqDkH4cZQ3_eUqjxzzf"
        md5 = "3b165ffc8819d695500cf565bf3a9ca2"

        print(">>> Start to download [ToS3 LR] dataset (BI degradation)")

        download_file(data_dir, file_id, "Bicubic4xLR")
        check_md5(os.path.join(data_dir, "Bicubic4xLR.zip"), md5)
        extract_zip(os.path.join(data_dir, "Bicubic4xLR.zip"), data_dir)

else:
    print(
        f'Unknown Degradation Type: {sys.argv[1]} (Currently supported: "BD" or "BI")'
    )
