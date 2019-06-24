# Illustration
Translate Mysql search result to an object which like ORM search result. 

database :

| id   | name  |
| ---- | ----- |
| 1    | yjijn |
| 2    | Jack  |
| 3    | Tom   |

useing class SqlObjLIst(),we can get the sql result as ORM serch result.

for example:

```pyhon
sql_result = SqlObjList(cursor).result# cursor is SQL search reslut
for result in sql_result:
	print(result.name)
	#print result:
	#yjijn
	#Jack
	#Tom
```



run "sql_obj_result.py" will get printing like this:

```json
<class 'list'>
1 Yjijn
2 Jack
3 Tom
```

