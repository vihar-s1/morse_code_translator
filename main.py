import encoder, decoder

message = input('Enter String: ')
encoded = encoder.encode(message)
decoded = decoder.decode(encoded)
print( f"encoded: {encoded} \ndecoded: {decoded}" )