class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chr_list = []
        chr_list.append([s[0], 0, 0])
        for i in range(len(s)):
            if chr_list[len(chr_list) - 1][0] == s[i]:
                chr_list[len(chr_list) - 1][1] += 1
            else:
                chr_list.append([s[i], 1, i])
        #print chr_list

        longest_str = ""
        for i in range(len(chr_list)):
            begin_i = i
            end_i = i
            inner_i = 0
            for j in range(len(chr_list) - i):
                if begin_i - 1 < 0:
                    break
                if end_i + 1 >= len(chr_list):
                    break
                if chr_list[begin_i - 1][0] != chr_list[end_i + 1][0]:
                    break
                if chr_list[begin_i - 1][1] != chr_list[end_i + 1][1]:
                    begin_i -= 1
                    end_i += 1
                    inner_i = chr_list[begin_i][1] if chr_list[begin_i][1] < chr_list[end_i][1] else chr_list[end_i][1]
                    break
                begin_i -= 1
                end_i += 1

            if inner_i > 0:
                sub_str = s[chr_list[begin_i][2] + chr_list[begin_i][1] - inner_i:chr_list[end_i][2] + inner_i]
            else:
                sub_str = s[chr_list[begin_i][2]:chr_list[end_i][2] + chr_list[end_i][1]]

            if len(longest_str) < len(sub_str):
                longest_str = sub_str
                #print sub_str

        return longest_str
