# 温州全旺电气有限公司官网

这是温州全旺电气有限公司的静态展示网站，包含多页官网和一个可单独发送的 HTML 展示版。

## 本地预览

直接打开 `index.html`，或在当前目录启动本地服务器：

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

然后访问：

```text
http://127.0.0.1:4173/index.html
```

## 文件说明

- `index.html`：官网首页
- `products.html`：产品与画册页
- `contact.html`：联系方式页
- `assets/`：图片、画册 PDF、样式和脚本
- `quanwang-electric-single.html`：可单独发给别人查看的展示版
- `温州全旺电气有限公司官网-单文件展示版.html`：同内容中文文件名副本

## 验证

```powershell
powershell -ExecutionPolicy Bypass -File .\tests\site-check.ps1
```
