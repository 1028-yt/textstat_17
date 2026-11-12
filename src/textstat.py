#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""textstat: 一个轻量级文本统计命令行小工具。

统计文本文件（或标准输入）的行数、字符数、非空白字符数、
中文字符数与英文单词数，结果以表格或 JSON 形式输出。

仅使用 Python 标准库，无第三方依赖。
"""

import argparse
import json
import re
import sys
from collections import OrderedDict

# 匹配连续的 ASCII 字母序列，作为英文单词
WORD_PATTERN = re.compile(r"[A-Za-z]+(?:['-][A-Za-z]+)*")
# 匹配中日韩统一表意文字区段
CJK_PATTERN = re.compile(r"[\u4e00-\u9fff]")


def count_words(text: str) -> int:
    """统计英文单词数量。"""
    return len(WORD_PATTERN.findall(text))


def count_cjk(text: str) -> int:
    """统计中文字符数量。"""
    return len(CJK_PATTERN.findall(text))


def analyze(text: str) -> "OrderedDict[str, int]":
    """计算各项文本统计指标。"""
    stats = OrderedDict()
    stats["lines"] = len(text.splitlines())
    stats["chars"] = len(text)
    stats["non_whitespace_chars"] = len(re.sub(r"\s", "", text))
    stats["cjk_chars"] = count_cjk(text)
    stats["english_words"] = count_words(text)
    return stats


def render_table(stats: "OrderedDict[str, int]") -> str:
    """以简易文本表格形式输出统计结果。"""
    label_map = {
        "lines": "行数",
        "chars": "字符总数（含空白）",
        "non_whitespace_chars": "非空白字符数",
        "cjk_chars": "中文字符数",
        "english_words": "英文单词数",
    }
    rows = [(label_map[key], value) for key, value in stats.items()]
    width_label = max(len(label) for label, _ in rows)
    width_value = max(len(str(value)) for _, value in rows)
    border = "+" + "-" * (width_label + 2) + "+" + "-" * (width_value + 2) + "+"
    lines = [border]
    for label, value in rows:
        lines.append(f"| {label:<{width_label}} | {value:>{width_value}} |")
        lines.append(border)
    return "\n".join(lines)


def read_source(args: argparse.Namespace) -> str:
    """从文件或标准输入读取文本。"""
    if args.file:
        with open(args.file, "r", encoding="utf-8") as fp:
            return fp.read()
    return sys.stdin.read()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="textstat：轻量级文本统计命令行工具（行数 / 字符 / 中文 / 英文单词）。"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="待统计的文本文件路径；不传则从标准输入读取。",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式输出统计结果。",
    )
    args = parser.parse_args()

    text = read_source(args)
    stats = analyze(text)

    if args.json:
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        print(render_table(stats))


if __name__ == "__main__":
    main()
