#!/usr/bin/python3
import pickle,pprint
# 使用pickle模块将数据对象保存到文件
# data = {
#     'a': [1,2.0,3,4+6j],
#     'b': ('string', u'Unicode string'),
#     'c': None
# }

# selfref_list = [1,2,3]
# selfref_list.append(selfref_list)

# output = open('data.pkl','wb')

# pickle.dump(data,output)
# pickle.dump(selfref_list,output,-1)

# output.close()


with open('data.pkl','rb') as pkl_file:
    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)
pkl_file.closed()

