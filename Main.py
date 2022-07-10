import MorseCoder

message = input('Enter String: ')
encoded = MorseCoder.encode(message)
decoded = MorseCoder.decode(encoded)
print(f"encoded: {encoded} \ndecoded: {decoded}")
