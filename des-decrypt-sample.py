import base64
from Crypto.Cipher import DES
import sys

args = sys.argv
# 暗号化された文字列
encrypted_text = args[1]

# Base64デコード
encrypted_data = base64.b64decode(encrypted_text)

# 鍵
key = args[2]
key_bytes = bytes.fromhex(key)

# DES-ECBの暗号化オブジェクトを作成
cipher = DES.new(key_bytes, DES.MODE_ECB)

# 復号化
decrypted_data = cipher.decrypt(encrypted_data)

print("復号化されたバイナリデータ:", decrypted_data)
# バイナリデータを文字列に変換
decrypted_text = decrypted_data.decode('utf-8')
print("復号化された文字列:", decrypted_text)





