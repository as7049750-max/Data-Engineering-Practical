import os
import struct
import pickle

os.makedirs("data", exist_ok=True)

# ---------- Binary file: write ----------
bin_path = "data/records.bin"
with open(bin_path, "wb") as f:
    for item in [(1, 25, 88.5), (2, 30, 92.0)]:
        f.write(struct.pack("iif", item[0], item[1], item[2]))

print(f"Binary data written to {bin_path}")

# ---------- Binary file: read ----------
record_size = struct.calcsize("iif")
with open(bin_path, "rb") as f:
    while chunk := f.read(record_size):
        print("Read from binary:", struct.unpack("iif", chunk))

# ---------- Pickle: write ----------
pkl_path = "data/app.pkl"
with open(pkl_path, "wb") as f:
    pickle.dump({"status": "active", "ids": [101, 102]}, f)

# ---------- Pickle: read ----------
with open(pkl_path, "rb") as f:
    print("Read from pickle:", pickle.load(f))