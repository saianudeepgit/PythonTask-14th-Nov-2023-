class int_rom_convert:
     num_rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
     def num2roman(self, num):
         roman = ""
         while num > 0:
             for i, r in self.num_rom:
                 while num >= i:
                     roman += r
                     num -= i
                     return roman
num = int(input("Enter a number:"))
print("Roman number is:", int_rom_convert().num2roman(num))
