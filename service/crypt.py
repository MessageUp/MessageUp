from Crypto.Cipher import ARC2
import struct
import binascii

def encrypt(plain, key):
    if isinstance(key, str):
        key = key.encode()
    if isinstance(plain, str):
        plain = plain.encode()
    iv = ARC2.block_size * b'\x00'
    cipher = ARC2.new(key, ARC2.MODE_ECB, iv)
    pad = (8 - divmod(len(plain), 8)[1]) * b'\x00'
    plain = plain + pad + struct.pack('!Q', len(pad))
    crypt = iv + cipher.encrypt(plain)
    return binascii.hexlify(crypt).decode()


def decrypt(crypt, key):
    if isinstance(key, str):
        key = key.encode()
    if isinstance(crypt, str):
        try:
            crypt = binascii.unhexlify(crypt.encode())
        except ValueError:
            raise ValueError("Incorrect encoded data: " + crypt)
    iv = crypt[:ARC2.block_size]
    crypt = crypt[ARC2.block_size:]
    cipher = ARC2.new(key, ARC2.MODE_ECB, iv)
    plain = cipher.decrypt(crypt)
    pad_len = struct.unpack('!Q', plain[-8:])[0] + 8
    plain = plain[:-pad_len]
    return plain.decode()
