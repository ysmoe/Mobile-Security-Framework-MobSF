# 迁移说明(MIGRATION)

本文档记录本项目与上游参考实现之间的差异、新增特性、以及本地化与改造涉及的代码清单。供维护者与贡献者参考,普通使用者无需阅读。

---

## 1. 中文本地化基础

### 1.1 Django i18n 基础设施

- `mobsf/MobSF/settings.py` 中启用 `LocaleMiddleware`,默认语言设为 `zh-hans`(简体中文)
- 配置 `LANGUAGES` 支持简体中文与英文切换
- 配置 `LOCALE_PATHS` 指向翻译文件目录
- 注册 i18n 上下文处理器与自定义语言上下文处理器
- 新增 `/i18n/setlang/` 路由用于语言切换

### 1.2 Web 界面中文化

所有 HTML 模板已翻译为中文,涵盖:

- **导航栏**:最近扫描、静态分析、动态分析、API、捐赠、文档、关于
- **首页**:上传并分析、拖拽上传、下载并扫描安装包
- **扫描记录**:扫描列表、操作按钮(静态报告、动态报告、安全评分卡、删除扫描等)
- **扫描队列**:任务列表、状态监控
- **认证页面**:登录、注册、修改密码、用户管理
- **静态分析**:Android / iOS / Windows 分析结果页、安全评分卡、应用对比
- **动态分析**:Android / iOS 动态分析器、动态报告、API 监控、日志查看
- **其他页面**:关于、捐赠、错误页、ZIP 说明等

### 1.3 PDF 报告中文化

- Android / iOS / Windows 三种 PDF 报告模板全部翻译
- 加入 CJK 字体回退链(PingFang SC、Microsoft YaHei、Noto Sans CJK SC 等)
- 确保中文在 wkhtmltopdf 渲染时正确显示

### 1.4 安全规则中文化

所有 YAML 规则中的 `message` 字段已翻译:

| 规则文件 | 数量 |
| --- | --- |
| `android_rules.yaml` | 52 条 |
| `android_apis.yaml` | 54 条 |
| `android_permissions.yaml` | 全部 |
| `android_niap.yaml` | 全部 |
| `swift_rules.yaml` | 39 条 |
| `objective_c_rules.yaml` | 25 条 |
| `ios_apis.yaml` | 13 条 |
| `behaviour_rules.yaml` | 211 条 |

### 1.5 Python 错误消息中文化

用户可见的错误消息已在以下模块中翻译:

- `mobsf/MobSF/views/home.py`
- `mobsf/StaticAnalyzer/views/common/pdf.py`
- `mobsf/StaticAnalyzer/views/common/shared_func.py`
- `mobsf/MobSF/views/appsec.py`
- `mobsf/MobSF/utils.py`

---

## 2. 语言切换

默认语言为简体中文。切换方式:

```
/i18n/setlang/?lang=en-us    # 切到英文
/i18n/setlang/?lang=zh-hans  # 切回中文
```

---

## 3. 字体支持

PDF 报告生成依赖 wkhtmltopdf 加载中文字体。CSS 中已配置字体回退链:

- **macOS**:PingFang SC(系统自带)
- **Linux**:Noto Sans CJK SC / WenQuanYi Micro Hei(需安装)
- **Windows**:SimHei / Microsoft YaHei(系统自带)

Linux 安装中文字体:

```bash
# Ubuntu / Debian
sudo apt-get install fonts-noto-cjk

# 或
sudo apt-get install fonts-wqy-microhei
```

---

## 4. Word (.docx) 报告导出

除 PDF 报告外,本项目还支持直接生成可编辑的 Word (.docx) 报告。

### 4.1 入口

- **Web 端**:任一扫描详情页(如 `/static_analyzer/<md5>/`)左侧导航栏,"PDF 报告"按钮下方新增"Word 报告"按钮
- **扫描列表**:`/recent_scans/` 页面每条记录旁边新增绿色 Word 按钮
- **REST API**:`POST /api/v1/download_docx`,参数 `hash=<md5>`

### 4.2 浏览器手动下载

```
http://127.0.0.1:8000/download_docx/<md5>/
```

### 4.3 curl 命令

```bash
API_KEY="<your-api-key>"
MD5="db8506bfe28c1339a6cad91618fbc9ed"

curl -X POST http://127.0.0.1:8000/api/v1/download_docx \
  -d "hash=$MD5" \
  -H "Authorization: $API_KEY" \
  -o report.docx
```

### 4.4 实现原理

- 在 PDF 模板渲染的 HTML 字符串上,**同一个 `template.render(context)` 数据**走两条分支:
  - 原路:HTML → wkhtmltopdf → PDF
  - 新路:HTML → BeautifulSoup → python-docx → DOCX
- 不重写模板、不重写数据组装逻辑、不引入 LibreOffice
- 文档元数据(标题、作者、主题、描述)从扫描 context 提取,写入 docx core properties

### 4.5 DOCX 内容映射

- 中文字体:Noto Sans CJK SC(Docker 镜像已装 `fonts-noto-cjk`)
- 标题层级:h1-h6 → Heading 1-4
- 段落、列表(ul/ol)、水平线(hr)直接保留
- 表格:保留表头,Bootstrap 严重程度颜色映射到单元格背景色
  - `danger` → 浅红 `#F8D7DA`
  - `warning` → 浅黄 `#FFF3CD`
  - `info` → 浅蓝 `#D1ECF1`
  - `success` → 浅绿 `#D4EDDA`
- 图片:`file://` / `data:image/png;base64` / 相对路径自动内嵌

### 4.6 依赖

- `python-docx>=1.1.0`(已写入 `Dockerfile.zh`)
- `lxml>=4.9.0`(python-docx 间接依赖)

### 4.7 Python API

```python
from mobsf.StaticAnalyzer.views.common.docx import html_to_docx
doc = html_to_docx(html_string, context=context_dict)
doc.save("report.docx")
```

---

## 5. 文件变更清单

### 5.1 新增文件

- `mobsf/MobSF/views/i18n.py` —— 语言切换视图与上下文处理器
- `mobsf/locale/` —— Django locale 目录
- `mobsf/StaticAnalyzer/views/common/docx.py` —— DOCX 报告生成器
- `Dockerfile.zh` —— 内置 CJK 字体的 Docker 镜像

### 5.2 修改文件

#### 配置与路由

- `mobsf/MobSF/settings.py` —— i18n 配置
- `mobsf/MobSF/urls.py` —— 语言切换路由

#### 模板

- `mobsf/templates/base/nav.html`
- `mobsf/templates/base/base_layout.html`
- `mobsf/templates/general/home.html`
- `mobsf/templates/general/recent.html`
- `mobsf/templates/general/tasks.html`
- `mobsf/templates/general/about.html`
- `mobsf/templates/general/dynamic.html`
- `mobsf/templates/general/error.html`
- `mobsf/templates/general/zip.html`
- `mobsf/templates/general/donate.html`
- `mobsf/templates/auth/*.html`(登录、注册、修改密码、用户管理)
- `mobsf/templates/pdf/android_report.html`
- `mobsf/templates/pdf/ios_report.html`
- `mobsf/templates/pdf/windows_report.html`
- `mobsf/templates/static_analysis/*.html`
- `mobsf/templates/dynamic_analysis/**/*.html`
- `mobsf/templates/404.html` / `403.html` / `500.html`

#### 规则

- `mobsf/StaticAnalyzer/views/android/rules/*.yaml`
- `mobsf/StaticAnalyzer/views/ios/rules/*.yaml`
- `mobsf/MalwareAnalyzer/views/android/rules/behaviour_rules.yaml`

#### Python 视图

- `mobsf/MobSF/views/home.py`
- `mobsf/StaticAnalyzer/views/common/pdf.py`
- `mobsf/StaticAnalyzer/views/common/shared_func.py`
- `mobsf/StaticAnalyzer/views/android/__init__.py`(新增 DOCX 路由)
