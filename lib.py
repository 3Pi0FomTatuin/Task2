import re

unit = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

teen = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

ten = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

mill = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]

and_word = "and"


class Converter:
    def __init__(self):
        self.mill_count = 0

    def unit_f(self, units, mill_index):
        return "{} {}".format(unit[units], self.mill_f(mill_index))

    def ten_f(self, tens, units, mill_index=0):
        if tens != 1:
            return "{}{}{} {}".format(
                ten[tens],
                "-" if tens and units else "",
                unit[units],
                self.mill_f(mill_index),
            )
        return "{} {}".format(teen[units], mill[mill_index])

    def hund_f(self, hundreds, tens, units, mill_index):
        if hundreds:
            return "{} hundred{}{}{}, ".format(
                unit[hundreds],  # use unit not unitfn as simpler
                " %s " % and_word if tens or units else "",
                self.ten_f(tens, units),
                self.mill_f(mill_index),
            )
        if tens or units:
            return "{} {}, ".format(self.ten_f(tens, units), self.mill_f(mill_index))
        return ""

    @staticmethod
    def mill_f(ind):
        if ind > len(mill) - 1:
            print("number out of range")
            raise Exception('NumOutOfRangeError')
        return mill[ind]

    def unit_sub(self, match_obj):
        return self.unit_f(int(match_obj.group(1)), self.mill_count) + ', '

    def ten_sub(self, match_obj):
        return self.ten_f(int(match_obj.group(1)), int(match_obj.group(2)), self.mill_count) + ', '

    def hund_sub(self, match_obj):
        ret = self.hund_f(
            int(match_obj.group(1)), int(match_obj.group(2)), int(match_obj.group(3)), self.mill_count
        )
        self.mill_count += 1
        return ret

    def number_to_words(self, num):
        self.mill_count = 0

        num = num.lstrip().lstrip('0')
        if num == '':
            return 'zero'

        match_obj = re.search(r'(\d)(\d)(\d)(?=\D*\Z)', num)
        while match_obj:
            num = re.sub(r'(\d)(\d)(\d)(?=\D*\Z)', self.hund_sub, num, 1)
            match_obj = re.search(r'(\d)(\d)(\d)(?=\D*\Z)', num)
        num = re.sub(r'(\d)(\d)(?=\D*\Z)', self.ten_sub, num, 1)
        num = re.sub(r'(\d)(?=\D*\Z)', self.unit_sub, num, 1)

        if num[-2:] == ', ':
            num = num[:-2]

        num = re.sub(r', (\S+)\s+\Z', f' {and_word} \\1', num)
        num = re.sub(r'\s+', ' ', num)
        return num.strip()
