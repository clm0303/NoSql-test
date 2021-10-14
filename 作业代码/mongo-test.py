import pymongo

client = pymongo.MongoClient('localhost')  # 建立连接
# print(client) #connect=True则连接成功
db = client['Nosql-test']  # 选择/新建数据库
# db = pymongo.MongoClient('localhost').get_database('Nosql-test')  #效果同上
# print(db)
col = db['students']  # 选择数据集
stu1 = {'id': '001', 'name': 'cao', 'age': '20'}
col.insert_one(stu1)  # 插入一条数据

result = col.find_one()  # 查询数据
print(result)
