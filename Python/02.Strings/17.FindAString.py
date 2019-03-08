def count_substring(string, sub_string):
    #return string.count(sub_string) # .count only count non-overlapping occurence
    return sum(1 for i in range(len(string)) if sub_string == string[i:i+len(sub_string)])
    # interestingly, this doesn't throw error of "out of index"

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)