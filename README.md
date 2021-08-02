# Simple Fluid

## 问题背景

前提：猫咪走丢了

已知：

<div class="img-anchor"></div>

![Fluid](docs/liquid.jpg)

<style>
.img-anchor + img {
  max-width: 200px;
}
</style>

结论：？

## 问题描述

你需要进行代码填空，完成一个简单的二维不可压缩流体模拟程序。你需要完成的代码功能大致包括：

1. 读取 JSON 输入，调用提供好的接口，初始化模拟环境（设置格点密度，边界条件，模拟参数等）
2. 实现以上初始化接口的具体逻辑。
3. 完成每个时间片内的模拟逻辑，更新格点上的流体速度和压强，溶质的浓度。
4. 模拟一定步数后，将每个格点的流体速度，溶质的浓度输出到一个 HDF5 文件中。

模板代码位于 `fluid.example.py`，请先将其重命名为 `fluid.py`，随后将其中标有 `# TODO` 的部分替换为相应的代码。算法和输入输出格式说明位于 `docs/detail.pdf`， `TODO` 注释中带有的**编号**和 `docs/detail.pdf` 中的**章节号**对应，请仔细阅读。

## 样例与评测

本题进行黑盒评测。共有 10 组输入，对于每组输入，我们会对你的输出的所有通道共进行 1000 次采样，如果采样得到的值是 $r$，助教所写的模拟得到对应的值是 $r\_std$，那么这个点给分比例 `(0, 1]` 如下：

```python
THRESHOLD = 0.01
def scoring(r, r_std):
  ratio = abs(r - r_std) / max(abs(r_std), 1e-5)

  if ratio < THRESHOLD:
    return 1
  return 0.1 ** (-(1 + THRESHOLD) * ratio + THRESDHOLD)
```

也就是如果相对误差在 Threshold = 1% 以内给 100% 的分数，相对误差在 100% 的时候给 10% 的分数。所有采样的平均分是黑盒的得分比例，乘以黑盒满分即为黑盒得分。

本题分数构成为：

- 黑盒: 按上述方法计算。
- 白盒: 代码风格与 Git 使用 20 分（包括恰当注释、合理命名、提交日志等）。

本题不设置运行时间、空间限制。

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。
