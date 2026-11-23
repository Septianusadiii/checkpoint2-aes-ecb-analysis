"""Checkpoint 2 - Buktikan atau Bantah: kebocoran pola AES-ECB.

Pengembangan dari Praktikum 4A (demo konsep), 4B (AES-ECB), dan
4C (perbandingan ECB vs CBC). Jalankan langsung dari VS Code.
Memerlukan paket: pycryptodome
"""

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes
except ImportError:
    raise SystemExit(
        "PyCryptodome belum terpasang. Di terminal VS Code, jalankan: "
        "py -m pip install pycryptodome"
    )


# PRAKTIKUM 4A: demo konsep ECB (BUKAN enkripsi AES asli)
def toy_block_encrypt(block):
    return block[::-1] + "|X"


def ecb_encrypt_demo(message, block_size=4):
    blocks = [message[i:i + block_size] for i in range(0, len(message), block_size)]
    ciphertext_blocks = [toy_block_encrypt(block) for block in blocks]
    return blocks, ciphertext_blocks


# PENGEMBANGAN: agar blok AES 16-byte bisa dibandingkan satu per satu
def split_blocks(data, block_size=16):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]


def tampilkan_blok(judul, blocks):
    print(f"\n{judul}")
    for i, block in enumerate(blocks, 1):
        if isinstance(block, bytes):
            print(f"Blok {i}: {block.hex()}")
        else:
            print(f"Blok {i}: {block}")


def main():
    # Pola yang dipakai sama seperti Praktikum 4A, 4B, dan 4C.
    message = "AAAAAAAABBBBBBBBAAAAAAAABBBBBBBB"
    plaintext = message.encode("ascii")
    key = b"1234567890abcdef"  # Hanya kunci contoh dari modul praktikum

    print("=== CHECKPOINT 2: MEMBUKTIKAN KEBOCORAN POLA ECB ===")

    # LANGKAH 1 - Praktikum 4A: perlihatkan blok yang berulang.
    toy_plain, toy_cipher = ecb_encrypt_demo(message)
    tampilkan_blok("[1] Demo konsep - blok plaintext (4 karakter)", toy_plain)
    tampilkan_blok("Demo konsep - blok ciphertext (bukan AES)", toy_cipher)
    print("Blok identik menghasilkan output identik:", toy_cipher[0] == toy_cipher[1])

    # LANGKAH 2 - Praktikum 4B: AES-ECB asli.
    # AES memiliki ukuran blok 16 byte, bukan 4 karakter seperti demo konsep.
    plain_blocks = split_blocks(plaintext)
    tampilkan_blok("[2] Plaintext AES (16 byte per blok)", plain_blocks)
    print("Blok plaintext 1 == 2:", plain_blocks[0] == plain_blocks[1])

    ecb_cipher = AES.new(key, AES.MODE_ECB)
    ecb_ct = ecb_cipher.encrypt(pad(plaintext, AES.block_size))
    ecb_blocks = split_blocks(ecb_ct)
    tampilkan_blok("[3] Hasil AES-ECB (hex)", ecb_blocks)
    print("Blok ciphertext ECB 1 == 2:", ecb_blocks[0] == ecb_blocks[1])

    # LANGKAH 3 - Praktikum 4C: mode CBC menggunakan IV acak.
    iv = get_random_bytes(AES.block_size)
    cbc_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    cbc_ct = cbc_cipher.encrypt(pad(plaintext, AES.block_size))
    cbc_blocks = split_blocks(cbc_ct)
    tampilkan_blok("[4] Hasil AES-CBC (hex)", cbc_blocks)
    print("IV CBC (hex):", iv.hex())
    print("Blok ciphertext CBC 1 == 2:", cbc_blocks[0] == cbc_blocks[1])

    # PENGEMBANGAN: buktikan data masih bisa dipulihkan dengan kedua mode.
    ecb_decrypted = unpad(AES.new(key, AES.MODE_ECB).decrypt(ecb_ct), AES.block_size)
    cbc_decrypted = unpad(AES.new(key, AES.MODE_CBC, iv=iv).decrypt(cbc_ct), AES.block_size)

    print("\n[5] Kesimpulan hasil eksperimen")
    print("Enkripsi ECB berhasil didekripsi:", ecb_decrypted == plaintext)
    print("Enkripsi CBC berhasil didekripsi:", cbc_decrypted == plaintext)
    print("Pola berulang bocor pada ECB:", ecb_blocks[0] == ecb_blocks[1])
    print("Pola berulang tampak pada CBC:", cbc_blocks[0] == cbc_blocks[1])
    print("\nKESIMPULAN: AES-ECB mengenkripsi data, tetapi tetap membocorkan pola blok identik.")
    print("CBC menyamarkan pola ini, tetapi tidak menyediakan autentikasi/integritas data.")
    print("Untuk aplikasi nyata, gunakan enkripsi terautentikasi seperti AES-GCM.")


if __name__ == "__main__":
    main()
