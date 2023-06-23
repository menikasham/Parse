from Crypto.Cipher import AES
import sys
if name == "main":
    f = input("{?} Enter flag: ")
    xk = f[0:8].encode()
    k = bytes([xk[i % len(xk)] for i in range(16)])
    c = AES.new(k, AES.MODE_ECB)
    d = c.decrypt(c)
    td = b''
    for i in range(len(d)):
        td += bytes([d[i] ^ xk[i % len(xk)]])
    fd = open("flag_checker.pyc", "wb")
    fd.write(td)
    fd.close()
    try:    
        from flag_checker import CheckFlag
    except:
        print("{-} Incorrect!")
        sys.exit(0)
    if CheckFlag(f):
        print("{+} Correct!")