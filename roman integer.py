class Solution(object):
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()
print(ob1.romanToInt("I"))
print(ob1.romanToInt("II"))
print(ob1.romanToInt("III"))
print(ob1.romanToInt("IV"))
print(ob1.romanToInt("V"))
print(ob1.romanToInt("VI"))
print(ob1.romanToInt("VII"))
print(ob1.romanToInt("VIII"))
print(ob1.romanToInt("IX"))
print(ob1.romanToInt("X"))
print(ob1.romanToInt("L"))
print(ob1.romanToInt("C"))
print(ob1.romanToInt("D"))
print(ob1.romanToInt("M"))




