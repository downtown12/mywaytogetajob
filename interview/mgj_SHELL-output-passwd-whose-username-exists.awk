#!/bin/awk -f
# MOGUJIE 2016 Written examination
# Information Security Job Position
# Question:
# Given two files user.info and passwd.info.
# user.info is user's id and user name mapping. like:
# id username
# 01 xiaomo
# 02 xiaogu
# 03 xiaojie
# 04 root
# 05 admin
# 06 lilei
# 07 hanmeimei
# 
# passwd.info is the username and passwd mapping. like:
# user password
# lilei ll_123
# xiaojie 123_xj
# damo dmdmdm
# xiaomo xmxmxm
# dagu dgdgdg
# 
# Please use shell to output the passwords whose username occurs in file: user.info.
# the example above should output:
# 123_xj
# xmxmxm
# ll_123
# 

#code begins, 
#to run, type: awk -f mgj_SHELL-output-passwd-whose-username-exists.awk user.info passwd.info
        BEGIN{
                usersize = 0;
                passwdsize =0
                }
        ARGIND==1 {user[$2] = $2; usersize++}
        ARGIND==2 {passwd[$1] = $2; passwdsize++}

        END{
          for(i in user){
                  for(j in passwd){
                          if(j == i){
                                  print passwd[j];
                                  break;
                          }
                  }
          }
       }

