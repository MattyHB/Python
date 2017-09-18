def countLetter(msg: str, letter2find: str) -> int:
  count = 0
  for ch in msg:
    if ch == letter2find:
      count += 1
  return count
