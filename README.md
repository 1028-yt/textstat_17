# textstat_17

> 轻量级文本统计命令行小工具：一键统计行数、字符数、非空白字符数、中文字符数与英文单词数。

`textstat` 是一个使用 Python 编写的命令行工具，仅依赖标准库，无需安装第三方包。适用于课程作业、文本预处理、写作字数自查等简单场景。

## 功能特性

- 统计**行数**、**字符总数**（含空白）、**非空白字符数**
- 分别统计**中文字符数**与**英文单词数**
- 支持读取本地文本文件，或从标准输入（管道）读取
- 支持表格与 JSON 两种输出格式
- 纯 Python 标准库实现，跨平台运行，无需联网，兼容 Python 3.7+


## 环境要求

- Python 3.7 及以上版本
- 无需安装任何第三方依赖

## 快速开始

克隆仓库后进入项目目录：

```bash
git clone https://github.com/1028-yt/textstat_17.git
cd textstat_17
```

统计示例文件：

```bash
python3 src/textstat.py examples/sample.txt
```

管道方式统计：

```bash
echo "Hello 开源世界" | python3 src/textstat.py
```

以 JSON 格式输出：

```bash
python3 src/textstat.py examples/sample.txt --json
```

## 输出示例

```
+----------------------+-------+
| 行数                 |     3 |
| 字符总数（含空白）   |    98 |
| 非空白字符数         |    89 |
| 中文字符数           |    53 |
| 英文单词数           |     5 |
+----------------------+-------+
```

## 项目结构

```
textstat_17/
├── src/
│   └── textstat.py        # 主程序：参数解析与统计逻辑
├── docs/
│   ├── usage.md           # 详细使用说明
│   └── branching.md       # 分支管理与协作流程说明
├── examples/
│   └── sample.txt         # 示例文本
├── CONTRIBUTING.md        # 参与贡献指南
├── LICENSE                # 开源许可证（MIT）
└── README.md              # 项目说明文档
```

## 使用说明

更多命令参数与统计口径说明见 [`docs/usage.md`](docs/usage.md)。

## 参与贡献

欢迎通过 Issue 反馈问题或提出改进建议，也欢迎提交 Pull Request。贡献流程见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 开源许可证

本项目基于 [MIT License](LICENSE) 开源，任何人可自由使用、修改与分发。
