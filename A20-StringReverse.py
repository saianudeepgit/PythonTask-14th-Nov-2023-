class reverse:
    def reverse_words(self, s):
        sp = s.split()
        sp.reverse()
        res = " ".join(sp)
        return res
str = input("Enter a string to reverse:")
print(reverse().reverse_words(str))
