"""
Builds public/index.html from src/page.html.

The source file holds only <title>, <style> and the page markup. This script
wraps it into a complete document, adding the doctype, <head>, meta tags and
the CSS reset, so the markup stays easy to edit on its own.

    python build.py [path-to-source.html]
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE = os.path.join(HERE, "src", "page.html")
PUBLIC = os.path.join(HERE, "public")

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kardelen Aldemir — Mobile &amp; Web Developer, İzmir</title>
<meta name="description" content="Kardelen Aldemir is a mobile and web developer in İzmir, Türkiye. Computer Engineering B.Sc. Kotlin, React Native, Expo, Spring Boot, FastAPI. Currently building YomYom, a walking app.">
<meta name="author" content="Kardelen Aldemir">
<link rel="canonical" href="https://kardelenaldemir.com/">
<meta name="theme-color" content="#62A73A" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0B0B" media="(prefers-color-scheme: dark)">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<meta property="og:type" content="website">
<meta property="og:url" content="https://kardelenaldemir.com/">
<meta property="og:title" content="Kardelen Aldemir — Mobile &amp; Web Developer">
<meta property="og:description" content="Mobile and web developer in İzmir. I build the whole thing, from the sensor to the screen.">
<meta property="og:image" content="https://kardelenaldemir.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="tr_TR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Kardelen Aldemir — Mobile &amp; Web Developer">
<meta name="twitter:description" content="Mobile and web developer in İzmir. I build the whole thing, from the sensor to the screen.">
<meta name="twitter:image" content="https://kardelenaldemir.com/og-image.png">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Kardelen Aldemir",
  "url": "https://kardelenaldemir.com/",
  "email": "kardelena0057@gmail.com",
  "telephone": "+90-543-887-7445",
  "jobTitle": "Mobile & Web Developer",
  "address": { "@type": "PostalAddress", "addressLocality": "İzmir", "addressCountry": "TR" },
  "alumniOf": { "@type": "CollegeOrUniversity", "name": "Yaşar University" },
  "sameAs": ["https://github.com/kardelenaldemir"],
  "knowsLanguage": ["tr", "en"],
  "knowsAbout": ["Kotlin", "React Native", "Expo", "Jetpack Compose", "Spring Boot", "FastAPI", "PostgreSQL", "Bluetooth Low Energy"]
}
</script>

"""

# Minimal reset, kept here so src/page.html carries no boilerplate.
RESET = (
    "  *, *::before, *::after { box-sizing: border-box; }\n"
    "  img { max-width: 100%; height: auto; }\n"
    "  .rows { margin: 0; }"
)


def build(source_path, target_path):
    """Wrap the source page in a full HTML document and write it out."""
    with open(source_path, encoding="utf-8") as handle:
        src = handle.read()

    match = re.search(r"<style>.*?</style>", src, re.S)
    if not match:
        raise SystemExit(f"no <style> block found in {source_path}")

    style = match.group(0).replace("  * { box-sizing: border-box; }", RESET)
    body = src[src.index("</style>") + len("</style>"):].strip()
    page = f"{HEAD}{style}\n</head>\n<body>\n\n{body}\n\n</body>\n</html>\n"

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as handle:
        handle.write(page)

    return len(page.encode("utf-8"))


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SOURCE
    target = os.path.join(PUBLIC, "index.html")
    size = build(source, target)
    print(f"built {target} ({size / 1024:.1f} KB) from {source}")


if __name__ == "__main__":
    main()
