from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# '매트릭스'의 평점 출력
target_movie = db.movies.find_one({'title': '매트릭스'})
target_point = target_movie['point']
print(target_point)

# '매트릭스'의 평점과 같은 영화 출력
movies = list(db.movies.find({'point': target_point}))
for movie in movies:
    print(movie['title'])

# '매트릭스'의 평점 0으로 만들기
db.movies.update_one({'title': '매트릭스'}, {'$set': {'point': 0}})
