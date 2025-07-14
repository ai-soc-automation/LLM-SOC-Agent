"""Download and extract CIC‑IDS 2018 flows as CSV.
Run: python scripts/download_cicids.py --dest datasets/cicids2018
"""
import argparse, hashlib, pathlib, tarfile, urllib.request

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00502/CICIDS2018.tar.gz"
SHA256 = "a0b77f3d87f5d5e0c5e8c94b5c4bcd875a6e61c71bdd3d8d24e3adadf0e1f5a3"

def download(url, path):
    if path.exists():
        print("✓ File already exists")
        return
    print("Downloading…")
    urllib.request.urlretrieve(url, path)

def verify(path, sha256):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    assert h.hexdigest() == sha256, "Checksum mismatch!"

parser = argparse.ArgumentParser()
parser.add_argument("--dest", default="datasets/cicids2018")
args = parser.parse_args()

path = pathlib.Path("datasets")
path.mkdir(exist_ok=True)
archive = path / "CICIDS2018.tar.gz"

download(URL, archive)
verify(archive, SHA256)
print("Extracting…")
with tarfile.open(archive, "r:gz") as tar:
    tar.extractall(args.dest)
print("✓ Dataset ready →", args.dest)