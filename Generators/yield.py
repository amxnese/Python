def Generator():
    yield "someday"
    yield "i'm gonna appreciate myself"
    yield "for not giving up"
myGen = Generator()
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
for index in myGen:
    print(index)


def gen():
    yield "getting wormed up"
    yield "getting into it"
    yield "almost there"
    yield "loading some oponents"
    yield "finished"
    yield "its ready to be launched"

mygen = gen()
print(next(mygen))
print("the beggining")
print(next(mygen))
print("getting to the point")
print(next(mygen))
print("last touches")
print(next(mygen))
for lines in mygen:
    print(lines)

def yields():
    yield "first"
    yield "second"
    yield "third"
nxt = yields()
print(next(nxt))
print(next(nxt))
print(next(nxt))