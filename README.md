# RasterLab website

Static marketing and App Store compliance site for RasterLab, the retro shader camera app by Matti Media LLC.

Pages:

- `index.html` — landing page
- `support/index.html` — help, FAQ, troubleshooting, contact (App Store **Support URL**)
- `privacy/index.html` — privacy policy (App Store **Privacy Policy URL**)

No build step, no framework, no JavaScript. Plain HTML + one stylesheet. Light and dark themes follow the system setting.

## Preview locally

```sh
make serve
```

Then open <http://localhost:8080/>. Any static file server works; the pages use relative links so the site can be hosted at a domain root or a sub‑path.

## Checks

```sh
make check
```

`scripts/check.py` parses every HTML file, verifies that each local link and asset resolves, that each in‑page `#anchor` exists, and that no page still contains the `DRAFT` callouts once you strip them for release (run `make check STRICT=1` to fail on remaining drafts).

## Before publishing

Everything marked **Draft · needs owner confirmation** in the pages must be resolved. See `HANDOFF.md` for the list.
