# Substance Painter 插件开发快速指南

> 适合：第一次写 Substance 3D Painter 插件，希望先跑通一个最小可用插件（MVP）。

## 1. 开发前准备

- 安装 **Adobe Substance 3D Painter**（建议与目标用户保持同一大版本）。
- 熟悉 Python 基础（函数、模块、异常、文件读写）。
- 了解 Painter 插件目录结构（一个插件文件夹 + `__init__.py`）。

## 2. 插件目录（推荐）

```text
ie_painter_starter/
├── __init__.py
└── README.md
```

Painter 会扫描用户插件目录并加载包含 `start_plugin()` / `close_plugin()` 的 Python 模块。

## 3. 最小插件生命周期

1. `start_plugin()`：Painter 启动插件时调用。
2. 注册 UI（菜单 Action / Dock Widget）和事件。
3. `close_plugin()`：Painter 卸载插件时调用，释放资源、移除 UI。

## 4. 典型开发流程

1. 在本仓库的 `plugins/ie_painter_starter` 下修改代码。
2. 将该文件夹复制到本机 Painter 插件目录。
3. 打开 Painter，启用插件并观察日志输出。
4. 迭代开发：每次修改后重载插件测试。

## 5. 建议优先做的 3 个功能

1. **一键检查当前工程状态**（材质集数量、纹理集名）。
2. **批量导出预设**（统一导出路径、命名规则）。
3. **项目规范检查器**（贴图尺寸、命名、通道完整性）。

## 6. 常见坑

- 忘记在 `close_plugin()` 里清理 UI / 回调，导致重复注册。
- 异常未捕获导致插件中断，建议统一日志函数。
- 把业务逻辑和 UI 强耦合，后续难以维护。

## 7. 下一步建议

- 先以本仓库示例插件为模板，跑通菜单按钮 + 日志输出。
- 再逐步增加导出、校验、自动化处理功能。
