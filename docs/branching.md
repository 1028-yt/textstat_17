# 分支管理与协作流程

本项目使用 Git 进行版本管理，遵循「主干稳定、分支开发、合并评审」的分支管理方式，用于在课程作业中体现分支创建、合并与冲突解决的完整过程。

## 分支规划

| 分支 | 作用 | 保护规则 |
| --- | --- | --- |
| `main` | 主干分支，保存可正常运行的稳定版本 | 不直接向 main 提交，改动经分支合并进入 |
| `feature/cjk-count` | 功能分支：开发中文字符统计功能 | 开发完成后合并回 main |
| `fix/word-count` | 修复分支：修正英文单词计数逻辑 | 修复验证后合并回 main |

## 典型操作流程

### 1. 创建功能分支

```bash
git checkout main
git pull origin main
git checkout -b feature/cjk-count
```

在分支上完成开发并提交：

```bash
git add src/textstat.py
git commit -m "add: 增加中文字符统计"
git push origin feature/cjk-count
```

### 2. 合并功能分支

在 GitHub 上发起 Pull Request，将 `feature/cjk-count` 合并回 `main`；本地也可执行：

```bash
git checkout main
git merge feature/cjk-count
```

### 3. 制造与解决冲突

当两个分支修改了同一处代码时，合并可能产生冲突。典型步骤：

1. 分别在两个分支上修改 `src/textstat.py` 中同一函数的同一行。
2. 执行 `git merge fix/word-count`，Git 提示冲突文件。
3. 打开冲突文件，阅读冲突标记：

```text
<<<<<<< HEAD
stats["english_words"] = count_words(text)
=======
stats["english_words"] = len(text.split())
>>>>>>> fix/word-count
```

4. 手动保留正确版本（或融合两种写法），删除冲突标记。
5. 重新提交：

```bash
git add src/textstat.py
git commit -m "merge: 合并单词计数修复并解决冲突"
```

### 4. 分支清理

合并完成后，删除已合并的远程与本地分支：

```bash
git branch -d feature/cjk-count
git push origin --delete feature/cjk-count
```

## 提交信息约定

- `add:` 新增功能
- `fix:` 修复问题
- `docs:` 文档改动
- `refactor:` 重构，不改变功能
