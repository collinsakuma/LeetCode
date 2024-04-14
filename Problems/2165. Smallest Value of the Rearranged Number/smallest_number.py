class Solution:
    def smallestNumber(self, num: int) -> int:
        # edge case 
        if num == 0:
            return 0
            
        str_num = str(num)
        if num > 0:
            str_num = sorted(str_num)
            if '0' in str_num:
                for idx, i in enumerate(str_num):
                    if i != '0':
                        str_num[0], str_num[idx] = i, '0'
                        break
        else:
            str_num = str_num[1:]
            str_num = sorted(str_num, reverse=True)
            str_num.insert(0,'-')
            
        
        return int(''.join(str_num))