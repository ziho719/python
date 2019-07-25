# str=input("请输入:\n")
# print ("您输入了",str)

fo = open("foo.txt", "w")
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)

fo.write('helloworld!')

