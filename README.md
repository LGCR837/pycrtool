# pycrtool

# 介绍
pycrtool 是一个功能丰富且使用简单的 Python 第三方模块。

# 类 run_command
这是一个可以运行终端控制台命令并实时获取输出的 Python 类。

### 1. **run_command()**
通过 `xxx = run_command( 终端命令 )` 可以给变量 `xxx` 给予一个类，并运行终端命令。

### 1. **get_part()**
通过 `xxx.get_part()` 可以获取到新输出的终端输出，既相比上一次获取多出的终端输出。

### 1. **get_con()**
通过 `xxx.get_con()` 可以获取到终端命令目前的运行状况，若运行完成返回 `True` ，未完成则返回 `False` 。

### 1. **get_all()**
通过 `xxx.get_all()` 可以获取到目前终端的所有输出。

### 示例代码:
```python
import pycrtool
cmd = pycrtool.run_command("dir C:\\") # 运行 dir C:\ 命令
while not cmd.get_con(): # 检查是否运行完毕
    print(cmd.get_part(),end="") # 输出相比上一次的新的输出
print(print(f"输出共 {len(cmd.get_all())} 字。") # 获得所有输出并统计字数
```

# 类 modern_replace
这是一个能实现更加高效智能的在一些方面替代 `replace()` 的类。

### 1. **dict_replace()**
通过 `dict_replace(text,replacements,regex=False)` 可以实现使用替换字典 `replacements` 对 `text` 进行替换，`regex` 为 `True` 时将允许使用 `re` 模块的正则表达式，`regex` 默认为 `False` 。
```python
import pycrtool
replacements = {
    "苹果": "香蕉",
    "小米": "大米",
    "这是替换前": "这是替换后"
}
text = "这是替换前的: 苹果与小米是截然不同的东西"
text = pycrtool.modern_replace.dict_replace(text,replacements)
print(text) # 这是替换后的: 香蕉与大米是截然不同的东西
```

### 2. **cross_replace()**
通过 `cross_replace(text,a,b)` 可以实现对字符串的交叉替换。它将 `text` 中所有出现的 `a` 替换为 `b`，同时将所有出现的 `b` 替换为 `a`。
```python
import pycrtool
text = "苹果和小米"
text = pycrtool.modern_replace(text,"苹果","小米")
print(text) # 小米和苹果
```

### 3. **count_replace()**
通过 `count_replace(text,a,b,count=-1)` 可以实现对文本的反复替换， `count` 是替换的次数，默认为 `-1` ，即始终替换。
```python
count_replace("1111111111111111","11","1") # 1
count_replace("1111111111111111","11","1",count=2) # 1111
```

# 类 modern_str
这个类使你可以更加高效的管理字符串。

### 1. **add_text()**
通过 `add_text(text,text_len,add_str=" ")` 可以实现在字符串后追加字符串使其达到指定长度，其中 `text` 是原始文本， `text_len` 是预计的长度， `add_str` 是在末尾追加的字符串，默认为 `" "` (空格)。

# 类 simple_sqlite3
`simple_sqlite3` 是一个简化版的 SQLite 数据库管理类，旨在为开发者提供一种简单的方式来操作 SQLite3 数据库。它封装了常见的数据库操作，如创建表、插入数据、查询数据、更新数据和删除数据,可以帮助开发者轻松地进行数据库管理，避免直接操作SQL语句。

### 1. **初始化:**
- `xxx = simple_sqlite3(db_file)`
- 初始化 simple_sqlite3 对象并连接到指定数据库。
   ```python
   db = simple_sqlite3('my_database.db')
   ```

### 2. **创建表:**
- `create_table(table_name, columns)`
- 创建一个表，其中 `columns` 是一个字典，键为列名，值为列的数据类型。
   ```python
   columns = {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'}
   db.create_table('users', columns)
   ```

### 3. **插入数据:**
- `insert(table_name, data)`
- 向指定表中插入数据， `data` 是一个字典，键为列名，值为数据。
   ```python
   data = {'name': 'John Doe', 'age': 30}
   db.insert('users', data)
   ```

### 4. **查询数据:**
- `select(table_name, columns='*', condition=None)`
- 查询指定表的数据， `columns` 为要查询的列， `condition` 为筛选条件（可选）。
   ```python
   result = db.select('users', columns='id, name', condition="age > 25")
   print(result)
   ```

### 5. **更新数据:**
- `update(table_name, data, condition)`
- 更新指定表的数据，`data`是一个字典，`condition`是更新条件。
   ```python
   data = {'name': 'Jane Doe'}
   db.update('users', data, condition="id = 1")
   ```

### 6. **删除数据:**
- `delete(table_name, condition)`
- 删除指定表的数据，`condition`是删除条件。
   ```python
   db.delete('users', condition="id = 1")
   ```

### 7. **关闭数据库连接:**
- `close()` - 关闭数据库连接。
   ```python
   db.close()
   ```


### 示例代码

```python
db = simple_sqlite3('example.db')
db.create_table('students', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})
db.insert('students', {'name': 'Alice', 'age': 22})
students = db.select('students')
print(students)
db.close()
```

# 类 sort
`sort` 类可以让你方便的进行各种排序操作，`arr` 需要是能够排序的类型，如列表。

### 1. **冒泡排序:**
- **`bubble_sort(arr)`**
  - 使用冒泡排序算法对数组进行排序。

### 2. **选择排序:**
- **`selection_sort(arr)`**
  - 使用选择排序算法对数组进行排序。

### 3. **插入排序:**
- **`insertion_sort(arr)`**
  - 使用插入排序算法对数组进行排序。

### 4. **快速排序:**
- **`quick_sort(arr)`**
  - 使用快速排序算法对数组进行排序。

### 5. **归并排序:**
- **`merge_sort(arr)`**
  - 使用归并排序算法对数组进行排序。

### 6. **堆排序:**
- **`heap_sort(arr)`**
  - 使用堆排序算法对数组进行排序。

### 7. **计数排序:**
- **`counting_sort(arr)`**
  - 使用计数排序算法对数组进行排序。

### 8. **桶排序:**
- **`bucket_sort(arr)`**
  - 使用桶排序算法对数组进行排序。

### 9. **猴子排序:**
- **`monkey_sort(arr)`**
  - 猴子会不断随机尝试所有方式直到成功。

# 类 suan
`suan` 是一个数学模块组，提供一些 `math` 库中不含有或使用不方便的函数。

### 1. **质数判断:**
- **`is_prime(n)`**
  - 判断`n`是否是质数，返回`True`或`False`。

### 2. **阶乘运算:**
- **`factorial(n)`**
  - 返回`n`的阶乘。

### 3. **勾股定理计算:**
- **`pythagoras(a=None, b=None, c=None)`**
  - 通过指定 `a`,`b`,`c` 中的任意两个返回另一条边，其中 `a`,`b` 为直角边，`c` 为斜边。

# 类 crawl
`crawl` 是一个网络爬虫工具合集，用于方便的进行一些合法的网络信息爬取。

### 1. **Bing 搜索获取**
- **`bing_search(query,url_start="https://www.bing.com/search?q=",url_end="")`**
  - 通过 Bing 搜索 `query` 并返回列表形式的搜索结果。
  - 返回值示例: `[["标题","链接","文本"],["标题","链接","文本"]]`
  - `url_start`,`url_end` 为可选性的参数，用于自定义搜索链接。