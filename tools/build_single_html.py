from __future__ import annotations

import base64
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quanwang-electric-single.html"
CN_OUT = ROOT / "温州全旺电气有限公司官网-单文件展示版.html"


def data_uri(path: str, mime: str) -> str:
    raw = (ROOT / path).read_bytes()
    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"


def css() -> str:
    source = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    return source.replace("position: sticky;", "position: relative;")


def card(title: str, text: str, image_path: str) -> str:
    return f"""
            <article class="product-card">
              <img src="{data_uri(image_path, 'image/png')}" alt="{html.escape(title)}" />
              <div class="product-card-body"><h3>{title}</h3><p>{text}</p></div>
            </article>"""


def brochure_page(label: str, image_path: str) -> str:
    return f"""
            <article class="brochure-page">
              <img src="{data_uri(image_path, 'image/png')}" alt="{html.escape(label)}" />
              <span>{label}</span>
            </article>"""


def main() -> None:
    hero = data_uri("assets/hero-home.png", "image/png")
    intro = data_uri("assets/brochure/page-02.png", "image/png")
    brochure_pdf = data_uri("assets/brochure/quanwang-brochure.pdf", "application/pdf")
    page = f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>温州全旺电气有限公司 - 单文件展示版</title>
    <style>
{css()}
      .site-nav a[href^="#"] {{ cursor: pointer; }}
      @media (max-width: 720px) {{
        .site-header {{
          align-items: flex-start;
          flex-direction: column;
          gap: 10px;
          padding-top: 12px;
          padding-bottom: 12px;
        }}

        .site-nav {{
          position: static;
          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
          gap: 8px;
          width: 100%;
          padding: 0;
          border: 0;
          background: transparent;
          box-shadow: none;
        }}

        .site-nav a {{
          padding: 8px 10px;
          border: 1px solid rgba(23, 49, 76, 0.12);
          border-radius: 999px;
          background: rgba(255, 255, 255, 0.72);
        }}
      }}
    </style>
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="#home" aria-label="温州全旺电气有限公司首页">
        <span class="brand-mark">QW</span>
        <span>温州全旺电气有限公司<small>WENZHOU QUANWANG ELECTRICAL</small></span>
      </a>
      <nav class="site-nav" aria-label="主导航">
        <a href="#home">首页</a>
        <a href="#products">产品与画册</a>
        <a href="#contact">联系我们</a>
      </nav>
    </header>

    <main id="home">
      <section class="hero" style="--hero-image: url('{hero}')">
        <div class="hero-content">
          <p class="eyebrow">Stainless steel distribution box / cabinet</p>
          <h1>温州全旺电气有限公司</h1>
          <p class="hero-lead">专业从事电器生产销售、技术服务与产品研发，面向配电箱、控制箱、动力柜、JP柜及各类非标箱柜提供可靠配套。</p>
          <div class="hero-actions">
            <a class="button button-primary" href="tel:0577-58252365">电话咨询</a>
            <a class="button button-secondary" href="#products">查看产品画册</a>
          </div>
        </div>
      </section>

      <div class="metric-strip" aria-label="公司核心能力">
        <div class="metric"><strong>2024</strong><span>成立于浙江温州乐清</span></div>
        <div class="metric"><strong>不锈钢</strong><span>配电箱/配电柜专业制造</span></div>
        <div class="metric"><strong>定制</strong><span>支持各类机箱柜和非标箱</span></div>
        <div class="metric"><strong class="qr-entry">扫码进入官网</strong><span>后续用正式网址生成二维码</span></div>
      </div>

      <section class="section">
        <div class="section-inner split-layout">
          <div>
            <p class="section-kicker">Enterprise Introduction</p>
            <h2>扎根电气成套配套，服务工业与民用配电场景</h2>
            <p class="lead">公司长期聚焦不锈钢配电箱、控制箱、基业箱、动力配电箱、XL-21动力柜、GGD低压柜、户外防雨箱、户内配电箱、电表箱、弱电箱、多媒体信息箱及非标箱柜。</p>
            <div class="feature-list">
              <div class="feature-item"><span class="feature-index">01</span><div><h3>配电箱柜制造</h3><p>覆盖户内、户外、明装、暗装及动力配电类箱柜。</p></div></div>
              <div class="feature-item"><span class="feature-index">02</span><div><h3>工程配套能力</h3><p>面向电气成套、楼宇配电、工业控制和设备配套需求。</p></div></div>
              <div class="feature-item"><span class="feature-index">03</span><div><h3>非标定制服务</h3><p>围绕尺寸、结构、安装方式和应用场景提供定制化箱柜。</p></div></div>
            </div>
          </div>
          <figure class="media-frame"><img src="{intro}" alt="温州全旺电气企业简介画册页" /></figure>
        </div>
      </section>

      <section class="section dark-band">
        <div class="section-inner">
          <p class="section-kicker">Product Categories</p>
          <h2>核心产品分类</h2>
          <div class="category-grid">
            <span>不锈钢配电箱/配电柜</span><span>不锈钢JP柜</span><span>不锈钢电表箱</span><span>不锈钢端子箱</span>
            <span>不锈钢户外箱</span><span>不锈钢暗装箱</span><span>电缆分接箱</span><span>XL-21 动力柜</span>
          </div>
        </div>
      </section>

      <section class="section" id="products">
        <div class="section-inner">
          <p class="section-kicker">Product Matrix</p>
          <h2>产品与画册</h2>
          <div class="product-grid">
{card('不锈钢配电箱/配电柜', '动力柜、基业箱、综合配电箱、户内外箱体。', 'assets/products/stainless-distribution-cabinet.png')}
{card('不锈钢JP柜', '常规JP柜、立式JP柜及户外综合配电配套。', 'assets/products/jp-cabinet.png')}
{card('不锈钢电表箱', '适配计量、电力分配和工程安装需求。', 'assets/products/meter-box.png')}
{card('户外箱 / 暗装箱 / 电缆分接箱', '覆盖挂墙式、落地式、端子箱和分接箱应用。', 'assets/products/outdoor-box.png')}
          </div>
          <div class="action-row">
            <a class="button button-primary" href="{brochure_pdf}" download="全旺电气资质.pdf">下载 PDF 画册</a>
            <a class="button button-light" href="#contact">联系咨询</a>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="section-inner">
          <p class="section-kicker">Brochure Preview</p>
          <h2>企业画册预览</h2>
          <div class="brochure-grid">
{brochure_page('01 封面', 'assets/brochure/page-01.png')}
{brochure_page('02 企业简介', 'assets/brochure/page-02.png')}
{brochure_page('03 产品展示', 'assets/brochure/page-03.png')}
{brochure_page('04 JP柜与电表箱', 'assets/brochure/page-04.png')}
{brochure_page('05 户外箱与暗装箱', 'assets/brochure/page-05.png')}
          </div>
        </div>
      </section>

      <section class="section" id="contact">
        <div class="section-inner contact-panel">
          <div class="contact-block">
            <p class="section-kicker">Company Information</p>
            <h2>温州全旺电气有限公司</h2>
            <div class="contact-row"><span>电话</span><a href="tel:0577-58252365">0577-58252365</a></div>
            <div class="contact-row"><span>邮箱</span><a href="mailto:15167876572@163.com">15167876572@163.com</a></div>
            <div class="contact-row"><span>地址</span><strong>浙江省温州市乐清市翁垟街道王宅村槐川中路 42 号</strong><p>Huai Chuan Zhong Road 42, Wengyang Street, Yueqing, Wenzhou, Zhejiang</p></div>
          </div>
          <aside class="service-block">
            <p class="section-kicker">Service Scope</p>
            <h2>咨询范围</h2>
            <ul class="service-list">
              <li>配电箱、JP柜、电表箱、户外箱或非标柜</li>
              <li>户内、户外、挂墙式、落地式、明装或暗装</li>
              <li>箱体尺寸、板材、门锁、防雨和开孔需求</li>
              <li>工业配电、楼宇配电、电气成套或设备配套</li>
            </ul>
          </aside>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <span>© 2026 温州全旺电气有限公司</span>
      <span>WENZHOU QUANWANG ELECTRICAL CO., LTD</span>
    </footer>
  </body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    CN_OUT.write_text(page, encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
