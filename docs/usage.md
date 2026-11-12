# 使用说明

## 命令格式

```bash
python3 src/textstat.py [文件路径] [--json]
```

## 参数说明

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| `文件路径` | 否 | 待统计的文本文件；不传时从标准输入读取 |
| `--json` | 否 | 以 JSON 格式输出统计结果，便于程序二次处理 |

## 统计口径

| 指标 | 口径 |
| --- | --- |
| 行数 | 按换行符 `\n` 计数；非空文本至少计为 1 行 |
| 字符总数 | 包含所有字符，含空格、制表符与换行 |
| 非空白字符数 | 去除空格、制表符、换行等空白字符后的字符数 |
| 中文字符数 | 匹配中日韩统一表意文字区段（U+4E00–U+9FFF） |
| 英文单词数 | 匹配连续的 ASCII 字母序列，支持 `it's`、`state-of-the-art` 等连写形式 |

## 常见用法

统计本地文件：

```bash
python3 src/textstat.py examples/sample.txt
```

统计一段管道文本：

```bash
cat README.md | python3 src/textstat.py
```

输出 JSON：

```bash
python3 src/textstat.py examples/sample.txt --json
```

## 已知限制

- 暂不区分日文、韩文等其他 CJK 文字，统一按中文字符区段统计。
- 编码默认按 UTF-8 读取，非 UTF-8 文件请先转码。
