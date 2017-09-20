#Listing One
def countLetter(msg: str, letter2find: str) -> int:
  count = 0
  msg = msg.upper()
  letter2find = letter2find.upper()
  for ch in msg:
    if ch == letter2find:
      count += 1
  return count

#Listing Two
def test_countLetter():
    assert countLetter('abcda', 'a') == 2
    assert countLetter('abcd' , 'e') == 0
    assert countLetter('ABCa' , 'A') == 2

#Listing Three
def split(s: str, delim: str) -> (str, str):
    """Splits a string `s` into two parts, using `delim` as the separator character.

    Preconditions: None
    Postconditions:
      * If `delim` is present in `s`, returns 
         (portion of `s` before `delim`, portion of `s` after `delim`)
      * Otherwise, returns (`s`, '')
    """
    x = s.find(delim)
    if x == -1:
      return ('no delimiter here', '')
    else:
        first = s[:x]
        second = s[x + 1:]
    return (first , second)
    

def test_split():
    assert split('100-200', '-') == ('100' , '200')
    assert split('os/360', '/') == ('os' , '360')
    assert split('no delimiter here', '-') == ('no delimiter here','')