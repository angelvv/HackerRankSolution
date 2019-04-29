# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
#m = re.findall(r'\w(?!aeiou_0-9)+([aeiou]{2,})\w(?!aeiou_0-9)+',s, flags = re.I)
#m = re.findall(r'(?<=[a-z&&[^aeiou]])+([aeiou]{2,})(?=[a-z&&[^aeiou]])+',s, flags = re.I) # seems to not support intersection
m = re.findall(r'[%s]([%s]{2,})(?=[%s])' % (c,v,c),s,flags=re.I) # use lookahead to avoid consuming the consonant so that the next vowel in "baabaab" can be detected
# re.I #stands for ignore case;
print('\n'.join(m) if m else -1)
