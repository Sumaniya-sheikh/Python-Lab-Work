# str1= input("Enter the first string: ")
# str2=""
# str3=""
# for i in range(len(str1)):
#     str2=str2+str1[i]+"@#"
# print("encrypted : ",str2) 

# for i in range(len(str2)):
#    if str2[i]!="@" and str2[i]!="#":
#        str3=str3+str2[i]
# print("decrypted : ",str3) 

str1 = input("Enter the first string: ")


str2 = "@#".join(str1) + "@#"
print("encrypted : ", str2)


str3 = str2.replace("@#", "")
print("decrypted : ", str3)