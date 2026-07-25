# 移动应用安全分析平台

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![平台](https://img.shields.io/badge/平台-macOS%20%7C%20Linux%20%7C%20Windows-green.svg)](#快速开始)
[![许可证](https://img.shields.io/:license-GPL--3.0--only-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Docker](https://img.shields.io/docker/pulls/opensecurity/mobile-security-framework-mobsf?style=social)](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf/)

> 一个面向 Android / iOS 移动应用的**静态分析 + 动态分析**一体化平台,提供完整的中文界面与中文报告输出。

---

## 项目简介

本项目对**开源移动安全分析工具**进行整合与改造,聚焦以下目标:

- **移动应用安全分析**:支持 Android(APK / 源码)、iOS(IPA / 源码)、Windows Mobile(APPX)等主流移动应用格式
- **多场景适用**:应用安全评估、渗透测试支撑、恶意样本分析、隐私合规检查
- **DevSecOps 友好**:内置 REST API 与命令行工具,可与 CI/CD 流水线无缝衔接
- **简体中文优先**:从界面、规则库、报告到错误消息,**全链路中文输出**,降低中文用户的使用与协作成本

### 与上游相比的差异

- **全中文界面** —— Django i18n 框架改造,支持中英文切换,默认简体中文
- **全中文报告** —— PDF 报告模板、安全规则说明、错误消息均完成本地化
- **可编辑 Word 报告** —— 在 PDF 之外提供 `.docx` 格式报告,便于审计、批注、二次加工
- **开箱即用的 CJK 字体** —— Docker 镜像内置 Noto CJK 字体,中文字符在报告中正确显示

---

## 快速开始

### 方式一:Docker(推荐)

```bash
# 拉取镜像
docker pull ghcr.io/ysmoe/mobsf-chinese-ysmoe:latest

# 启动服务,默认监听 8000 端口
docker run -it --rm -p 8000:8000 ghcr.io/ysmoe/mobsf-chinese-ysmoe:latest

# 默认账号:mobsf / mobsf
# 启动后访问 http://127.0.0.1:8000
```

启动后访问 [http://127.0.0.1:8000](http://127.0.0.1:8000),使用默认账号登录即可。

> **镜像说明**
>
> - 镜像基于上游 [opensecurity/mobile-security-framework-mobsf](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf/) 构建,叠加中文字体(Noto CJK)与 `python-docx` 依赖,并应用本仓库的中文本地化补丁。
> - 镜像仓库为 **私有**(private),首次拉取前需要先登录 GHCR:
>
>   ```bash
>   # 登录 GitHub Container Registry(需要一个具备 read:packages 权限的 PAT)
>   echo $GITHUB_PAT | docker login ghcr.io -u ysmoe --password-stdin
>   ```
>
>   登录成功后即可正常 `docker pull`。

### 方式二:本地源码

```bash
# 克隆仓库
git clone <repository-url> mobile-app-security-analyzer
cd mobile-app-security-analyzer

# 运行安装脚本(macOS / Linux)
./setup.sh

# 启动开发服务器
./run.sh

# Windows 用户请使用 setup.bat / run.bat
```

环境要求:**Python 3.12+**,需安装 `wkhtmltopdf` 用于 PDF 报告生成,以及 Noto CJK / PingFang SC 等中文字体。

---

## 功能特性

### 静态分析

- **Android**:APK 反编译、清单分析、代码扫描、权限审计、证书与签名校验
- **iOS**:IPA 解包、Plist 分析、Swift / Objective-C 规则扫描
- **Windows Mobile**:APPX 静态分析
- **源码扫描**:支持直接上传 ZIP 源码包进行分析

### 动态分析

- **Android 动态分析**:运行时行为监控、网络流量捕获、API 调用拦截
- **iOS 动态分析**:针对 IPA 的运行时插桩测试
- **Frida 集成**:支持基于 Frida 的 Hook 与插桩脚本

### 报告输出

- **PDF 报告** —— 中文化的安全评估报告,含严重程度着色、风险评分卡
- **Word(.docx)报告** —— 同一份数据生成可编辑 Word 文档,便于在审计流程中批注、流转
  - 表格保留严重程度颜色(危险 / 警告 / 提示 / 良好)
  - 标题层级、列表、水平线、图片完整保留
  - 文档元数据(标题、作者、主题)从扫描上下文自动填充

### REST API 与 CLI

通过 REST API 与命令行工具,可在 CI/CD 流水线中触发扫描、获取结果:

- `POST /api/v1/upload` —— 上传应用
- `POST /api/v1/scan` —— 触发扫描
- `POST /api/v1/download_pdf` —— 下载 PDF 报告
- `POST /api/v1/download_docx` —— 下载 Word 报告

详细接口定义参见 Web 界面内的 "API" 页面。

---

## 文档与资源

- **使用文档**:启动后访问 Web 界面右上角"文档"链接
- **迁移说明**:`MIGRATION.md` 记录了与上游的差异以及本地化变更清单
- **更新日志**:`CHANGELOG.md`

---

## 参与贡献

欢迎通过 Issue 反馈问题、提交功能建议或发起 Pull Request。

提交前请:

1. 阅读 `AGENTS.md` 了解项目规范与安全要求
2. 运行 `tox -e lint` 确保代码通过 lint 检查
3. 对涉及安全的修改,补充相应的测试用例

> **安全提示**:本项目处理的全部输入(APK / ZIP / IPA / 清单)均来自已认证但**潜在恶意**的用户。任何路径处理、命令执行、模板渲染都必须按攻击者可控输入对待,不可信任。

---

## 许可证

本项目以 **GPL-3.0-only** 许可证发布。完整条款参见仓库根目录的 `LICENSE` 文件。

---

## 致谢

本项目参考了开源社区的 [Mobile Security Framework (MobSF)](https://github.com/MobSF/Mobile-Security-Framework-MobSF) 项目,在此向原作者与社区贡献者致以诚挚的感谢。
