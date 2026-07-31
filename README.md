# kardelenaldemir.com

My personal portfolio site. One page, no framework, no dependencies.

**Live:** [kardelenaldemir.com](https://kardelenaldemir.com)

## About

A single self-contained HTML page. It makes no external requests at all — no CDN
scripts, no web fonts, no remote images. The illustration is inlined as a data
URI and the type is set in system fonts, so the page renders immediately and
works offline once loaded.

Content is bilingual. The language is picked from the visitor's device
(`navigator.language`), can be switched from the header, and the choice is
remembered in `localStorage`.

Light and dark themes are both designed, following the visitor's system setting.

## Structure

```text
src/page.html      Source — edit here
build.py           src/page.html → public/index.html
netlify.toml       Publish directory, security headers, cache rules

public/            The deployed folder
  index.html         Generated — do not edit by hand
  404.html
  og-image.png       Social share card
  favicon.*
  robots.txt
  sitemap.xml
```

`src/page.html` holds only the `<title>`, `<style>` and the markup. `build.py`
wraps it into a complete document, adding the doctype, `<head>`, meta tags,
Open Graph data and the CSS reset. Keeping the boilerplate out of the source
makes the markup easier to work on.

## Running it

```bash
python build.py
cd public && python -m http.server 8000
```

Then open <http://localhost:8000>.

## Editing

1. Edit `src/page.html`.
2. Run `python build.py`.
3. Commit both the source and the generated `public/index.html`.

Translations live in the `I18N` object at the end of `src/page.html`. Every
translatable string is marked with `data-i18n="key"` in the markup, and each key
must exist in both the `en` and `tr` dictionaries.

## Licence

Code is MIT. The written content, CV details and the YomYom illustration are
mine and not covered by that licence.
