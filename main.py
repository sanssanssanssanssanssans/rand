def gen(bytelen):
    with open("/dev/random","rb") as f:
        return f.read(bytelen)

bytesize = int(input())
rand = gen(bytesize)
print(int.from_bytes(rand,byteorder="big"))
