def substring_search(data_str):
    long_slice = ''
    start_index = 0
    max_length_slice = 0
    for i in range(len(data_str)):
        if data_str[i] not in long_slice:
            long_slice += data_str[i]
            if len(long_slice) > max_length_slice:
                max_length_slice = len(long_slice)
        else:
            duble_index = data_str.rfind(data_str[i], start_index, i)
            start_index = duble_index + 1
            long_slice = data_str[start_index:i + 1]
    return max_length_slice


if __name__ == '__main__':
    # data_str = 'ejkfuamrksxrqgsfnuubbkntgmgguqtmrpperyyafgnhsmymrajvowrlyjrvtizgowfkujcewwpypnjpipcdpfdoxuckrhvrzbsbxvxqoqwaqvsvvpptuqeunzqcmhiftlruxqxseqisxoszkrjrbmfdmlaaxaqjlzisedvfeprbnqyzxhvmdcjwfrqlcczywbdwoayatkbfowxclispgkelpuosgknuztrrlwidgppxtcfcjwgmkgkhdpqymbtiljnsnijiieoycvdgrsqeyytvrvpcvvxmupcuhiufzpgwmkcobgeoapuvycqbitlremumauhuhnlvnzaadmpugybktdfvkxwhldzpkqxndgvxgmlkczndnwbtvuzaadvpnylenbdelwthzgpoczwjfwxaqeoryrbbuzmlvwjwtivfbyeafdvstrcwlawjwrcfmsnzbbdgvgaktfvvfirynbzbquzekxjmcbaokldjjdmwaniznkmmmhluitefypvoasixvwxbgfxksnmxigrdpdgxdwacrijbkrzgxehiagirywvxosxykntgnxxgstanmeiydqcyyhgjktbycicmwtwzdwisxccvgjzgokvebmlngmonkdqeeozegtqzfqptqligfrpcxqhmveiwhjjnoicevcugwzvfityeheiirbwdrgdywwdgpxlvbbwszuqwuvniahtqytsbvtuqqybsxfxcmlzufpcbtkyptjjjpwfyfmyezvwnognhdzzdugdqymlrsxhqhywihmcilnbciizwnsnjakvcvfwzdbfboazbuaybaoeqgeutftdofrxypnxklysschvsqnpefkvpykoujzfmfetnwblunnluotrrjzrfhosoqbimdcmdhftqvimragczketsbumrfqwnpiiijplulyidmyxwoapgkvhrvxwnorloprhcoyfwczionqukbnzlxejjfeajpezdalmncupunfasxddgfstpziedqrllakbnbwbqtsiohxjw'
    data_str = input()
    print(substring_search(data_str))
