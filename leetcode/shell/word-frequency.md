#Problem Description:
#### Write a bash script to calculate the frequency of each word in a text file words.txt.
#### 
#### For simplicity sake, you may assume:
#### 
#### words.txt contains only lowercase characters and space ' ' characters.
#### Each word must consist of lowercase characters only.
#### Words are separated by one or more whitespace characters.
#### For example, assume that words.txt has the following content:
#### 
#### the day is sunny the the
#### the sunny is is
#### Your script should output the following, sorted by descending frequency:
#### the 4
#### is 3
#### sunny 2
#### day 1
#### Note:
#### Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
#### 
#### [show hint]
#### 
#### Hint:
#### Could you write it in one-line using Unix pipes?
###

#My Idea: 
#### sort命令拾遗：
#### 选项：
#### -k POS1[,POS2]
####              key, 从关键字POS1开始,*到*POS2结束.
####              字段数和字符偏移量都从1开始计数(与基于零的+POS格式作比较)
####       -k  keydef
####              The keydef argument is a restricted sort key field definition.  The format
####              of this definition is:
###
####              field_start[type][,field_end[type]]
###
####       When  there  are multiple key fields, later keys shall be compared only after all
####       earlier keys compare equal.
###
#### -n:　numeric，按照数字方式进行排序。以排序13、8两个数为例：按照数字正序排序，8在前，13在后;
####       否则（按照子母正序排序），'13'在前，'8'在后（字符'1'<字符'8'）
#### -r: reverse, 反序
#### -n -r两个选项在一起，可写作-nr
###
#### Read from the file words.txt and output the word frequency list to stdout.
#My Solution:
awk '{for(i=1;i<=NF;i++) freq[$i]+=1;} END{for(a in freq) printf "%s %d\n",a,freq[a];}' words.txt | sort -k 2 -nr
