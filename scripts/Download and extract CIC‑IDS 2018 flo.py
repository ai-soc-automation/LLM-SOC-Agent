"""Download and extract CIC‑IDS 2018 flows as CSV.
Run: python scripts/download_cicids.py --dest datasets/cicids2018
"""
import argparse, hashlib, pathlib, tarfile, urllib.request, sys

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00502/CICIDS2018.tar.gz"
SHA256 = "a0b77f3d87f5d5e0c5e8c94b5c4bcd875a6e61c71bdd3d8d24e3adadf0e1f5a3"

def download(url, path):
    if path.exists():
        print("✓ File already exists:", path)
        return
    print("Downloading…")
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print("Download failed:", e)
        sys.exit(1)

def verify(path, sha256):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    if h.hexdigest() != sha256:
        print("Checksum mismatch!")
        sys.exit(1)
    print("✓ Checksum verified")

parser = argparse.ArgumentParser()
parser.add_argument("--dest", default="datasets/cicids2018")
args = parser.parse_args()

archive_dir = pathlib.Path("datasets")
archive_dir.mkdir(exist_ok=True)
archive = archive_dir / "CICIDS2018.tar.gz"

download(URL, archive)
verify(archive, SHA256)

dest_path = pathlib.Path(args.dest)
dest_path.mkdir(parents=True, exist_ok=True)
print("Extracting…")
try:
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(dest_path)
except Exception as e:
    print("Extraction failed:", e)
    sys.exit(1)

print("✓ Dataset ready →", dest_path)