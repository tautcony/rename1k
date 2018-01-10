# rename1k 千字文编码改名

使用千字文的想法来自[这里](https://github.com/xiaq/base1k)。

理论上修改`SYMBOLS`为任意2的指数次个互不相同字符均能正常运作。

需要使用`Python 3`，现时有两个选项：

- `--encode`: 将给定的文件或文件夹及其下的文件均以`base1k`进行编码
- `--decode`: 将给定的文件或文件夹及其下的文件均以`base1k`进行解码

如若直接拖文件/文件夹上去，则默认为decode。
