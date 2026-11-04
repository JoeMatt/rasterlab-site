# Handoff: RasterLab website

Generated 2026-11-03 from the RasterLab app source at `RasterLab/RasterLab/RasterLab` (branch `develop`, commit 815ace7). Nothing here is deployed; this is a local static site in its own git repository.

## Files

| Path | Purpose |
|---|---|
| `index.html` | Landing page |
| `support/index.html` | Support URL for App Store Connect: FAQ, troubleshooting, permissions, contact |
| `privacy/index.html` | Privacy Policy URL for App Store Connect |
| `styles.css` | Single stylesheet, light/dark via `prefers-color-scheme`, responsive at 900px and 600px |
| `assets/app-icon-512.png`, `assets/apple-touch-icon.png` | Resized from the app's `AppIcon1024x1024.png` |
| `scripts/check.py`, `Makefile` | `make serve` (port 8080) and `make check` (links, anchors, assets, title/lang/h1/alt) |

## Facts the pages rely on (verified in source)

- Display name `RasterLab`, bundle id `com.mattimedia.RasterLab`, copyright string "Copyright © 2025 Matti Media LLC" (`Tuist/ProjectDescriptionHelpers/TargetSettings.swift`).
- Privacy manifests in `RasterLab/PrivacyInfo.xcprivacy` and `RasterLabShared/PrivacyInfo.xcprivacy`: tracking false, no tracking domains, no collected data types; required-reason APIs UserDefaults (CA92.1, 1C8F.1) and FileTimestamp (C617.1).
- Entitlements (`RasterLab/RasterLab.entitlements`): App Group `group.com.mattimedia.rasterlab`, Siri, photos-library, GPU continued processing. No iCloud, no push (dropped in commit 815ace7).
- Usage strings: Camera, Microphone, Photo Library add/read, Location when-in-use ("adds location data to your photos"), Siri.
- No `URLSession`, `NWConnection`, analytics, crash-reporting or StoreKit references in app/extension/watch Swift sources. `CLLocationManager` in `RasterLab/Core/LocationManager.swift`; `WCSession` in the watch and phone connectivity managers.
- Declared packages: Zip and Alloy (README). Catalog: 1,024 shaders, previews for 1,020 (README). iOS 26.0+, watchOS 10.6+ (README).

## Needs owner confirmation before publishing (all marked in-page with "Draft · needs owner confirmation" or a dashed `todo` chip)

1. **Support contact route.** No email, form or issue tracker exists in source. App Store Connect requires one on the Support URL page. (`support/index.html` × 2)
2. **Privacy contact** and **effective date**. (`privacy/index.html`)
3. **App Store link / availability.** Not verified; no badge or link is shown on the landing page.
4. **Children / general-audience statement** and **regional rights language** (GDPR, CCPA) in the privacy policy.
5. **Location tagging behaviour.** The usage string says location is added to photos; I found `LocationManager` but did not trace the EXIF/QuickTime metadata write. Confirm the wording "attached to captures".
6. **Zip package purpose.** Listed as "archive handling for bundled shader resources"; confirm the actual use. `External/game-music-emu` is vendored in the repo but not referenced from app sources I searched; it is not listed on the site. Confirm whether it ships in the binary.
7. **Hosting domain.** Pages use relative links and work at a domain root or sub-path. OG image path is relative and should become absolute once the domain is known.

To make `make check` fail while any draft marker remains: `make check STRICT=1`.

## Not done / out of scope

- No deploy, DNS, GitHub remote, App Store Connect or signing changes.
- No screenshots of the app; the landing page uses the app icon only. Real device screenshots would improve the hero.
- The app repository was not modified.
