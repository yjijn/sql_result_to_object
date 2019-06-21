# sql_result_to_object
Translate Mysql search result to an object which like ORM search result. 

database like this:

| id   | name  |
| ---- | ----- |
| 1    | yjijn |
| 2    | Jack  |
| 3    | Tom   |



and run "sql_obj_result.py" will get printing like this:

```json
<class 'list'>
1 Yjijn
2 Jack
3 Tom
```

