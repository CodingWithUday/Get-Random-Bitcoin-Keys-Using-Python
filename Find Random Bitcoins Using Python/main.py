from bitcoin import * #pip install bitcoin
myprivatekey = random_key() #It Generates a Random Bitcoin Key
mypubkey = privkey_to_pubkey(myprivatekey) #Generates The Private Key To Public Key
bitcoinaddress = privkey_to_address(myprivatekey) #Generates The Private Key To The Coin Address
print("================================================================")
print("Private Key -", myprivatekey)
print("Public key -", mypubkey)
print("Coin Address -", bitcoinaddress)
print("================================================================")