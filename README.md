# Echo website

Public static product, support, privacy and usage pages for Echo / Echotm.

Custom domain: https://echo.tendazl.com
Public support: tendazlkj@gmail.com
Operator: 聊城腾达智联科创有限公司

English, Japanese, German and French pages. A Chinese privacy archive is retained at /zh-Hans/privacy/. App screenshots are real public fictional examples, with authored tasks explicitly marked; German and French pages label their English screenshots. No testimonials, automated-AI-demo claims, analytics, cookies, forms or external font dependencies are added.

GitHub Pages publishes main at the root. CNAME is the custom hostname. DNS must contain only an additional echo CNAME to abertgao.github.io; preserve existing apex, www, MX, SPF and cfo records. Enable HTTPS in Pages after certificate provisioning. No Tencent server deployment or paid resource is needed.

Preview: python3 -m http.server 8765 --bind 127.0.0.1
Validate: python3 tools/check_site.py
