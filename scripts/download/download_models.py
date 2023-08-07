import gdown
import zipfile
import os
import sys
import hashlib


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def download_small_file(fpath, fid, md5sum):
    url = f"https://drive.google.com/uc?export=download&id={fid}"
    gdown.download(url, fpath, quiet=False)
    if md5sum != md5(fpath):
        print(f"!!! Fail to match MD5 sum for: {fpath}")
        print("!!! Please try downloading it again")
        sys.exit(1)


if sys.argv[1] == "BD" and sys.argv[2] == "TecoGAN":
    fpath = "./pretrained_models/TecoGAN_BD_iter500000.pth"
    if not os.path.exists(fpath):
        fid = "13FPxKE6q7tuRrfhTE7GB040jBeURBj58"
        md5sum = "13d826c9f066538aea9340e8d3387289"
        print("Start to download model [TecoGAN BD]")
        download_small_file(fpath, fid, md5sum)

elif sys.argv[1] == "BD" and sys.argv[2] == "FRVSR":
    fpath = "./pretrained_models/FRVSR_BD_iter400000.pth"
    if not os.path.exists(fpath):
        fid = "11kPVS04a3B3k0SD-mKEpY_Q8WL7KrTIA"
        md5sum = "77d33c58b5cbf1fc68a1887be80ed18f"
        print("Start to download model [FRVSR BD]")
        download_small_file(fpath, fid, md5sum)

elif sys.argv[1] == "BI" and sys.argv[2] == "TecoGAN":
    fpath = "./pretrained_models/TecoGAN_BI_iter500000.pth"
    if not os.path.exists(fpath):
        fid = "1ie1F7wJcO4mhNWK8nPX7F0LgOoPzCwEu"
        md5sum = "4955b65b80f88456e94443d9d042d1e6"
        print("Start to download model [TecoGAN BI]")
        download_small_file(fpath, fid, md5sum)

elif sys.argv[1] == "BI" and sys.argv[2] == "FRVSR":
    fpath = "./pretrained_models/FRVSR_BI_iter400000.pth"
    if not os.path.exists(fpath):
        fid = "1wejMAFwIBde_7sz-H7zwlOCbCvjt3G9L"
        md5sum = "ad6337d934ec7ca72441082acd80c4ae"
        print("Start to download model [FRVSR BI]")
        download_small_file(fpath, fid, md5sum)

else:
    print(f"Unknown combination: {sys.argv[1]}, {sys.argv[2]}")
