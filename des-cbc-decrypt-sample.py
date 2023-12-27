import base64
from Crypto.Cipher import DES
import sys

args = sys.argv
# 暗号化されたBase64文字列
encrypted_text = args[1]

# Base64デコード
encrypted_data = base64.b64decode(encrypted_text)

# 鍵
key_hex = args[2]
key = bytes.fromhex(key_hex)

# 初期ベクトル (IV)
iv_hex = args[3]
iv = bytes.fromhex(iv_hex)

# DES-CBCの暗号化オブジェクトを作成
cipher = DES.new(key, DES.MODE_CBC, iv)

# 復号化
decrypted_data = cipher.decrypt(encrypted_data)

print("復号化されたバイナリデータ:", decrypted_data)
# バイナリデータを文字列に変換
decrypted_text = decrypted_data.decode('utf-8')
print("復号化された文字列:", decrypted_text)