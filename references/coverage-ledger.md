# 覆盖记录与检查工具

短篇不用此工具。多文件合卷、长篇续译或补译时，用稳定单元记录每处原文去了哪里，避免合卷时漏段、重复或把注释混入正文。单元可以是源段落、章条或带定位的可独立识别片段，不要求与中文段落一一对应。

## 最小JSON结构

保存为项目工作目录中的`coverage.json`，使用UTF-8：

```json
{
  "sources": [
    {
      "id": "latin-main",
      "origin": "supplied",
      "path_or_url": "原始文件路径或稳定链接",
      "expected_unit_ids": ["p001", "p002", "p003"],
      "units": [
        {"id": "p001", "locator": "第1页，题名", "kind": "metadata", "action": "exclude", "reason": "文件题名已记入版本清单"},
        {"id": "p002", "locator": "第1章第1段", "kind": "body", "action": "translate", "output_ids": ["zh-001"]},
        {"id": "p003", "locator": "第1章第2段", "kind": "body", "action": "pending", "reason": "尚待翻译"}
      ]
    }
  ],
  "outputs": [{"id": "zh-001", "text": "该单元的中文译文。"}]
}
```

上述示例有一个未完成单元，审计会报告`INCOMPLETE`。源清单的`expected_unit_ids`必须从提取／分段清单独立生成，不要从已经翻译的列表反推，否则无法识别漏项。

`action`仅为以下四种：

- `translate`：`output_ids`指向至少一个非空译文；拆分或合并用数组及共享ID表达。
- `duplicate`：`duplicate_of`为`来源ID/单元ID`，直接指向已登记为`translate`的单元，并有`reason`。不链接另一个重复单元，以免循环或链式丢失。
- `exclude`：写明`reason`，如导航、范围外编者材料、元数据。排除必须符合用户范围，不能用来掩盖缺译。
- `pending`：写明`reason`，保留未完成项，不当作已完成翻译。

补入刊本的单元作为新source，`origin`设为`supplement`，记录稳定来源和实际页／栏／扫描定位。`kind`可区分`body`、`source-note`、`editorial`、`metadata`；语义分类由译者判断，工具不推断。

## 运行与解释

用当前可用Python运行：

```text
python scripts/audit_coverage.py 项目目录/coverage.json --report 项目目录/coverage-audit.json
```

脚本路径相对于本技能目录。仅依赖Python标准库。返回码0表示覆盖记录完整，1表示有未完成单元，2表示结构或对应关系错误；报告列出缺项、重复ID、空译文、无效链接和无来源译文。

它不读PDF或Word正文，不判断中文与原文是否等义，不核验来源真伪，也不证明范围清单本身完整。译者仍须检查实际原文件、补缺、文本地位和成品内容；版面检查另用相应文件技能完成。
