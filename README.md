pycrtool 是一个功能丰富且使用简单的 Python 第三方模块。

## 类 run_command
这是一个可以运行终端控制台命令并实时获取输出的 Python 类。

### run_command()
通过 `xxx = run_command( 终端命令 )` 可以给变量 `xxx` 给予一个类，并运行终端命令。

### get_part()
通过 `xxx.get_part()` 可以获取到新输出的终端输出，既相比上一次获取多出的终端输出。

### get_con()
通过 `xxx.get_con()` 可以获取到终端命令目前的运行状况，若运行完成返回 `True` ，未完成则返回 `False` 。

### get_all()
通过 `xxx.get_all()` 可以获取到目前终端的所有输出。

### 示例代码:
```python
import pycrtool
cmd = pycrtool.run_command("dir C:\\") # 运行 dir C:\ 命令
while not cmd.get_con(): # 检查是否运行完毕
    print(cmd.get_part(),end="") # 输出相比上一次的新的输出
print(print(f"输出共 {len(cmd.get_all())} 字。") # 获得所有输出并统计字数
```

## 类 modern_replace
这是一个能实现更加高效智能的在一些方面替代 `replace()` 的类。

### dict_replace()
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

### cross_replace()
通过 `cross_replace(text,a,b)` 可以实现对字符串的交叉替换。它将 `text` 中所有出现的 `a` 替换为 `b`，同时将所有出现的 `b` 替换为 `a`。
```python
import pycrtool
text = "苹果和小米"
text = pycrtool.modern_replace(text,"苹果","小米")
print(text) # 小米和苹果
```