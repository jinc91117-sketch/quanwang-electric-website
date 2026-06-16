$ErrorActionPreference = "Stop"

function Assert-True {
  param(
    [bool]$Condition,
    [string]$Message
  )

  if (-not $Condition) {
    throw $Message
  }
}

function Read-Page {
  param([string]$Path)
  Assert-True (Test-Path -LiteralPath $Path) "Missing page: $Path"
  return Get-Content -LiteralPath $Path -Raw -Encoding UTF8
}

$root = Split-Path -Parent $PSScriptRoot
$requiredFiles = @(
  "index.html",
  "products.html",
  "contact.html",
  "README.md",
  ".gitignore",
  "quanwang-electric-single.html",
  "assets/styles.css",
  "assets/site.js",
  "assets/hero-home.png",
  "assets/brochure/quanwang-brochure.pdf",
  "assets/brochure/page-01.png",
  "assets/brochure/page-02.png",
  "assets/brochure/page-03.png",
  "assets/products/stainless-distribution-cabinet.png",
  "assets/products/jp-cabinet.png",
  "assets/products/meter-box.png",
  "assets/products/outdoor-box.png"
)

foreach ($file in $requiredFiles) {
  Assert-True (Test-Path -LiteralPath (Join-Path $root $file)) "Missing required file: $file"
}

$pages = @{
  "index.html" = Read-Page (Join-Path $root "index.html")
  "products.html" = Read-Page (Join-Path $root "products.html")
  "contact.html" = Read-Page (Join-Path $root "contact.html")
  "single.html" = Read-Page (Join-Path $root "quanwang-electric-single.html")
}

foreach ($entry in $pages.GetEnumerator()) {
  $html = $entry.Value
  Assert-True ($html -match 'WENZHOU QUANWANG ELECTRICAL') "$($entry.Key) missing English brand"
}

foreach ($pageName in @("index.html", "products.html", "contact.html")) {
  Assert-True ($pages[$pageName] -match 'assets/styles\.css') "$pageName missing stylesheet link"
  Assert-True ($pages[$pageName] -match 'index\.html') "$pageName missing home nav"
  Assert-True ($pages[$pageName] -match 'products\.html') "$pageName missing products nav"
  Assert-True ($pages[$pageName] -match 'contact\.html') "$pageName missing contact nav"
}

$allHtml = ($pages.Values -join "`n")
Assert-True ($allHtml -match '0577-58252365') "Missing phone number"
Assert-True ($allHtml -match '15167876572@163\.com') "Missing email"
Assert-True ($allHtml -match 'Huai Chuan Zhong Road 42') "Missing address"
Assert-True ($pages["products.html"] -match 'quanwang-brochure\.pdf') "Products page missing brochure PDF link"
Assert-True ($pages["products.html"] -match 'stainless-distribution-cabinet') "Products page missing primary product category"
Assert-True ($pages["products.html"] -match 'jp-cabinet') "Products page missing JP cabinet category"
Assert-True ($pages["index.html"] -match 'qr-entry') "Home page missing QR strategy copy"
Assert-True ($pages["index.html"] -match 'hero-home\.png') "Home page missing custom hero background"
Assert-True ($pages["single.html"] -match 'data:image/png;base64') "Single HTML missing embedded images"
Assert-True ($pages["single.html"] -match 'tel:0577-58252365') "Single HTML missing phone link"
Assert-True ($pages["single.html"] -match 'mailto:15167876572@163\.com') "Single HTML missing email link"
Assert-True ($pages["single.html"] -notmatch 'href="assets/') "Single HTML still depends on asset links"

Write-Host "Site checks passed."
