def getBit(num, i):
  return num & (1 << i) != 0

print getBit(4, 2)

def setBit(num, i):
  return num | (1 << i)

print setBit(4, 0)

def clearBit(num, i):
  mask = ~(1 << i)
  return num & mask

print clearBit(5, 0)

def clearBitsMSBthroughI(num, i):
  mask = (1 << i) - 1
  return mask & num

def clearBitsIthrough0(num, i):
  mask = ~((1 << (i + 1)) - 1)
  return num & mask

def updateBit(num, i, v):
  mask = ~(1 << i)
  return (num & mask) | (v << i)

print updateBit(4, 3, 1)

