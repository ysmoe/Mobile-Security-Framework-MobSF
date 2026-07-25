# Mobile Application Security Analyzer

> A unified platform for **static analysis** and **dynamic analysis** of Android / iOS mobile applications, with full Simplified Chinese interface and reporting.

---

## Overview

This project integrates and refines **open-source mobile security tooling** to deliver:

- **Mobile app security analysis** for Android (APK / source), iOS (IPA / source), and Windows Mobile (APPX)
- **Use cases**: application security assessment, penetration testing support, malware analysis, privacy compliance
- **DevSecOps-friendly**: REST APIs and CLI tools for CI/CD integration
- **Simplified Chinese first**: end-to-end localized UI, rule descriptions, reports, and error messages

### Differences from upstream

- **Fully localized UI** via Django i18n, with Chinese / English switcher; default language is Simplified Chinese
- **Fully localized reports** — PDF templates, security rule messages, and user-facing errors are translated
- **Editable Word reports** in addition to PDF — convenient for auditing, annotation, and downstream workflows
- **Pre-installed CJK fonts** in the Docker image for correct Chinese rendering in reports

---

## Quick Start

### Option 1: Docker (recommended)

```bash
docker pull ghcr.io/ysmoe/mobsf-chinese-ysmoe:latest
docker run -it --rm -p 8000:8000 ghcr.io/ysmoe/mobsf-chinese-ysmoe:latest
# Default credentials: mobsf / mobsf
# Then visit http://127.0.0.1:8000
```

> **Image notes**
>
> - The image is built on top of the upstream [opensecurity/mobile-security-framework-mobsf](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf/) image, with CJK fonts (Noto CJK), `python-docx`, and the Chinese localization files from this repository layered on top.
> - The image is **private**. Log in to GHCR before pulling:
>
>   ```bash
>   echo $GITHUB_PAT | docker login ghcr.io -u ysmoe --password-stdin
>   ```

### Option 2: Local source

```bash
git clone <repository-url> mobile-app-security-analyzer
cd mobile-app-security-analyzer
./setup.sh        # macOS / Linux
./run.sh
# Windows: use setup.bat / run.bat
```

Requirements: **Python 3.12+**, `wkhtmltopdf` for PDF generation, Noto CJK / PingFang SC or equivalent Chinese fonts.

---

## Features

### Static Analysis

- **Android**: APK decompilation, manifest analysis, code scanning, permission audit, certificate & signature validation
- **iOS**: IPA unpacking, Plist analysis, Swift / Objective-C rule scanning
- **Windows Mobile**: APPX static analysis
- **Source code scanning**: ZIP source upload supported

### Dynamic Analysis

- **Android dynamic analysis**: runtime behavior monitoring, network traffic capture, API call interception
- **iOS dynamic analysis**: runtime instrumentation for IPA targets
- **Frida integration**: hook and instrumentation scripts

### Reports

- **PDF reports** — localized security assessment with severity coloring and risk scorecards
- **Word (.docx) reports** — same data, editable format for audit workflows
  - Severity colors preserved in tables (danger / warning / info / success)
  - Headings, lists, dividers, and images preserved
  - Document metadata (title, author, subject) auto-populated from scan context

### REST API and CLI

Programmatic access for CI/CD pipelines:

- `POST /api/v1/upload` — upload app
- `POST /api/v1/scan` — trigger scan
- `POST /api/v1/download_pdf` — download PDF report
- `POST /api/v1/download_docx` — download Word report

For full API reference, see the "API" page in the web UI.

---

## Documentation

- In-app documentation is linked from the web UI
- See `CHANGELOG.md` for release notes
- See `MIGRATION.md` for the full list of localization and integration changes from upstream

---

## Contributing

Issues and pull requests are welcome.

Before submitting:

1. Read `AGENTS.md` for project conventions and security requirements
2. Run `tox -e lint` to ensure lint passes
3. Add tests for any security-sensitive changes

> **Security note**: This project processes attacker-supplied input (APK, ZIP, IPA, manifests) from authenticated but **potentially malicious** users. All path handling, command execution, and template rendering must treat input as untrusted.

---

## License

Released under **GPL-3.0-only**. See the `LICENSE` file for the full text.

---

## Acknowledgements

This project is built with reference to the open-source [Mobile Security Framework (MobSF)](https://github.com/MobSF/Mobile-Security-Framework-MobSF) project. Sincere thanks to its original authors and community contributors.
