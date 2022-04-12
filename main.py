import Encoder
import Decoder

message = input('Enter String: ')
encoded = Encoder.encode(message)
decoded = Decoder.decode(encoded)
print(f"encoded: {encoded} \ndecoded: {decoded}")
