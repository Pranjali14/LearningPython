def Descending_Order(num):
  n = sorted(list(str(num)), reverse=True);
  return int(''.join(n));
