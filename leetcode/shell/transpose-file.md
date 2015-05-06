#Problem Description:
		#### Given a text file file.txt, transpose its content.
		#### 
		#### You may assume that each row has the same number of columns and each field is separated by the ' ' character.
		#### 
		#### For example, if file.txt has the following content:
		#### 
		#### name age
		#### alice 21
		#### ryan 30
		#### Output the following:
		#### 
		#### name alice ryan
		####age 21 30
		###

#My Idea:
#### awk中双重for循环的使用
#### 注意：NF和NR的含义不一样
#### NF： Number of Fields，一行中列的个数
#### NR： Number of Record, 已经读取的记录的个数，也就是已经处理到了第几行（从1计数）
#### 只有当所有行都执行完后NR才是当前文件的行数。当然这是对于只有一个输入文件而言的，如果有多个输入文件，NR的值会累加
###
#### Read from the file file.txt and print its transposed content to stdout.

#My Solution:
		awk '{for(j=1;j<=NF;j++) row[NR][j] = $j;} 
		
		END{
		        for(j=1;j<=NF;j++){
		            for(i=1;i<=NR;i++){
		                    if(i<NR){printf "%s ",row[i][j]}
		                    else{printf "%s\n",row[i][j]}
		            }   
		        }
		}' file.txt
