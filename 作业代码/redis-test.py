import redis

pool = redis.ConnectionPool('localhost')  # 连接池
r = redis.Redis('localhost')  # 连接
r.set('name', 'cao')  # 设置值
print(r.get('name'))  # 取出值
