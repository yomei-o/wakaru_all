# wakaru_all ── The "Wakaru" Series Collection

**🌐 [日本語](README.md) ｜ English**

The **canonical originals** of "Wakaru" ("It Clicks") — a reading series for physics-loving high-schoolers and undergraduates. Every series is managed here from now on. Each episode is a self-contained HTML page (serif type + MathJax + live canvas figures + print/PDF ready; the only external dependency is the MathJax CDN).

## 🌐 Published site (read in your browser)

**➡ https://yomei-o.github.io/wakaru_all/**

> On GitHub's file pages (github.com/…) the HTML shows up as **source**. To **actually read it and play with the live figures**, open the published site (GitHub Pages) above. The links in the tables below also point to the published (rendered) site.

## Series (English editions)

| Series | About | Read (published site) |
|---|---|---|
| **Cosmology That Clicks** | Read the universe through the speed of light, the fine-structure constant, and gauge symmetry | [open](https://yomei-o.github.io/wakaru_all/wakaru-uchuron-en/index.html) |
| **Relativity That Clicks** | Divide everything by c. β · γ · spacetime interval · E=mc² · simultaneity · gravity = curvature · variable-c ≡ curvature (7 episodes, complete) | [open](https://yomei-o.github.io/wakaru_all/wakaru-soutai-en/index.html) |
| **Quantum That Clicks** | The story of ℏ. S/ℏ separates classical from quantum: grain & wave, wave function, sum over paths, Schrödinger, uncertainty, measurement (6 episodes + bonus, complete) | [open](https://yomei-o.github.io/wakaru_all/wakaru-ryoushi-en/index.html) |
| **Fields That Click** | Why forces travel at the speed of light. Reading fields as "dimensionless ratios" (8 episodes, complete) | [open](https://yomei-o.github.io/wakaru_all/wakaru-ba-en/index.html) |
| **Black Holes That Click** | The diagonal of the cube (c · ℏ · G), read through information and bits: horizon · entropy = bit count · Hawking temperature · fastest computer · holography · information paradox (6 episodes + bonus, complete) | [open](https://yomei-o.github.io/wakaru_all/wakaru-blackhole-en/index.html) |
| **Force That Clicks** | Peel back what "force" really is — down to fields, geometry, and symmetry | [open](https://yomei-o.github.io/wakaru_all/wakaru-chikara-en/index.html) |
| **Mass That Clicks** | What mass actually is | [open](https://yomei-o.github.io/wakaru_all/wakaru-shitsuryo-en/index.html) |
| **The Universe Is a Computer** | Read the cosmos through the lens of computation | [open](https://yomei-o.github.io/wakaru_all/wakaru-uchu-keisanki-en/uchu-keisanki-index.html) |
| **Learning That Clicks** | Evolution, learning, and consciousness read through one and the same gradient | [open](https://yomei-o.github.io/wakaru_all/wakaru-gakushuron-en/index.html) |
| **A History of UNIX That Clicks** | The history of UNIX | [open](https://yomei-o.github.io/wakaru_all/wakaru-unix-en/index.html) |

**★ Map of the whole collection: [The Physics Cube](https://yomei-o.github.io/wakaru_all/butsuri-rittai-en.html)** ── take in every series at a glance along the three axes c · ℏ · G.

(English folders: `wakaru-uchuron-en/` · `wakaru-soutai-en/` · `wakaru-ryoushi-en/` · `wakaru-ba-en/` · `wakaru-blackhole-en/` · `wakaru-chikara-en/` · `wakaru-shitsuryo-en/` · `wakaru-uchu-keisanki-en/` · `wakaru-gakushuron-en/` · `wakaru-unix-en/`)

## 日本語版 (Japanese originals)

The Japanese originals live in sibling folders and are listed in the [Japanese README](README.md). Quick links: [Fields](https://yomei-o.github.io/wakaru_all/wakaru-ba/index.html) · [Relativity](https://yomei-o.github.io/wakaru_all/wakaru-soutai/index.html) · [Quantum](https://yomei-o.github.io/wakaru_all/wakaru-ryoushi/index.html) · [Cosmology](https://yomei-o.github.io/wakaru_all/wakaru/index.html) · [Force](https://yomei-o.github.io/wakaru_all/wakaru-chikara/index.html) · [Mass](https://yomei-o.github.io/wakaru_all/wakaru_shitsuryo/index.html) · [Universe-as-Computer](https://yomei-o.github.io/wakaru_all/wakaru-uchu-keisanki/uchu-keisanki-index.html) · [Learning](https://yomei-o.github.io/wakaru_all/wakaru_learn/index.html) · [UNIX](https://yomei-o.github.io/wakaru_all/wakaru-unix/index.html).

## How to read
Start from the contents page of the **published site** above and go to each episode. Every individual HTML file just works when opened in a browser (the only external dependency is the MathJax CDN). To print, use each page's "Print → Save as PDF."

## Notes on structure
- Each series sits as a **sibling folder directly under this repository**. Contents pages reference their sister series with relative links (e.g. the contents of `wakaru-ba-en/` → `../wakaru-chikara-en/index.html`), so keep each series in its sibling folder directly under the root.
- The physics tetralogy (Fields · Relativity · Quantum · Cosmology) connects on a single sheet through the fundamental constants c · ℏ · G (→ [The Physics Cube](butsuri-rittai-en.html)). "Quantities with units are stage scenery; what matters is the dimensionless ratio" is the through-line of the whole collection.
- English editions are one-to-one translations of the Japanese originals; the code, figures, and math are preserved, only the visible text is translated. Expressions such as "the speed of light slows" are equivalent rephrasings (projections) for understanding — the locally measured speed of light and the dimensionless constant α are invariant.
