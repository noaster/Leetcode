class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if len(word_list) != len(pattern):
            return False
        str_dict = dict()
        
        for index, char in enumerate(pattern):
            if char in str_dict:
                if str_dict[char] != word_list[index]:
                    return False
            else:
                found_keys = [key for key, value in str_dict.items() if value == word_list[index]]
                if len(found_keys) > 0:
                    return False
                str_dict[char] = word_list[index]
        return True
