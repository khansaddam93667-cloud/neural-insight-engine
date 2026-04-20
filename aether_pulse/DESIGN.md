# Design System Strategy: The Neural Architecture

## 1. Overview & Creative North Star
This design system is built upon the **"Neural Architecture"**—a creative North Star that treats the interface not as a flat screen, but as a multi-dimensional data environment. For a deep-research AI application, the UI must feel authoritative yet ethereal. We achieve this by moving away from "standard" modular grids and embracing an editorial layout characterized by intentional asymmetry, vast negative space, and "light-as-logic" signifiers.

The "Neural Architecture" prioritizes depth. Instead of flat components, elements emerge from the deep navy void (`#0e1322`) through glassmorphism and luminescence. It is a signature experience that replaces structural rigidity with tonal fluidity, ensuring the user feels they are "submerging" into data rather than just viewing it.

## 2. Color & Surface Logic
The palette is rooted in the depth of night, utilizing high-contrast accents to guide the eye through complex research threads.

### The "No-Line" Rule
Standard UI relies on 1px borders to separate content. **In this system, 1px solid borders are strictly prohibited for sectioning.** Boundaries must be defined through:
*   **Background Shifts:** Distinguish a sidebar from a main feed by moving from `surface` (`#0e1322`) to `surface-container-low` (`#161b2b`).
*   **Tonal Transitions:** Use soft gradients between `surface-container` tiers to imply a change in context.

### Surface Hierarchy & Nesting
We treat the UI as a series of physical layers. Hierarchy is achieved by "stacking" the surface tokens:
*   **Level 0 (Base):** `surface-dim` (`#0e1322`) – The infinite canvas.
*   **Level 1 (Sections):** `surface-container-low` (`#161b2b`) – Broad content areas.
*   **Level 2 (Cards/Modules):** `surface-container` (`#1a1f2f`) – Discrete data points.
*   **Level 3 (Interactive/Floating):** `surface-container-high` (`#25293a`) – Overlays and active research nodes.

### The "Glass & Glow" Rule
To create the "high-tech" feel, use Glassmorphism for floating elements (e.g., tooltips, floating nav). 
*   **Formula:** Apply a semi-transparent `surface-variant` (`#2f3445` at 60% opacity) with a `backdrop-filter: blur(12px)`.
*   **Luminescence:** Use the `primary` (`#c3f5ff`) and `secondary` (`#dfb7ff`) tokens as soft glows (box-shadows with 20px+ blur at 10% opacity) behind active AI "connected" elements to simulate light emission from the data itself.

## 3. Typography
The typography is a study in contrast: the industrial precision of **Space Grotesk** paired with the humanistic clarity of **Manrope**.

*   **The Editorial Voice (Space Grotesk):** Used for `display` and `headline` scales. This font’s geometric quirks provide the "futuristic" edge. Use `display-lg` (3.5rem) with tight letter-spacing for hero research titles to create an authoritative, magazine-like feel.
*   **The Functional Voice (Manrope):** Used for `title`, `body`, and `label` scales. Manrope ensures high legibility during deep reading sessions. 
*   **Hierarchy Tip:** Pair a `headline-sm` in Space Grotesk with a `body-md` in Manrope. The tension between the two weights creates a sophisticated, bespoke look that avoids the "bootstrap" aesthetic.

## 4. Elevation & Depth
Depth is a functional tool for research, not just an aesthetic choice.

*   **Tonal Layering:** Avoid drop shadows for static elements. If a card needs to stand out, place a `surface-container-highest` (`#2f3445`) card on a `surface-container-low` (`#161b2b`) background.
*   **Ambient Shadows:** For elements that truly "float" (modals, dropdowns), use extra-diffused shadows. Color the shadow using a tinted version of `on-surface` (`#dee1f7`) at 5% opacity rather than black. This mimics the way light refracts through glass in a dark environment.
*   **The Ghost Border Fallback:** Where accessibility requires a container edge, use the "Ghost Border"—the `outline-variant` (`#3b494c`) at 20% opacity. It should be felt, not seen.

## 5. Components

### Buttons
*   **Primary:** A high-gloss transition from `primary` (`#c3f5ff`) to `primary-container` (`#00e5ff`). No border. Use a subtle `primary` glow on hover.
*   **Secondary:** `surface-container-highest` background with `on-surface` text. 
*   **Tertiary:** Ghost style—no background, just `on-secondary-container` text with a thin-line icon.

### Cards & Data Nodes
*   **Construction:** Use `surface-container-low` with a `lg` (0.5rem) roundedness.
*   **Constraint:** No dividers. Separate the header from the body using a vertical spacing of 1.5rem or a subtle background shift to `surface-container-highest` for the header area.

### Input Fields
*   **Minimalist State:** A simple `outline-variant` bottom-stroke. 
*   **Active State:** The stroke transitions to `primary` with a 2px glow. The background subtly shifts to `surface-container-highest`.

### AI Connected Elements (The "Stream")
*   **Visual Style:** For "connecting" research dots, use thin-line paths (1px) using the `secondary` (`#dfb7ff`) token. Apply a CSS animation "pulse" to the stroke to indicate active AI processing.

### Futuristic Icons
*   All icons must be **thin-line (1px or 1.5px weight)**. Use the `primary` token for active icons and `outline` for inactive ones. Avoid filled icon states; use "glow" to indicate selection instead.

## 6. Do’s and Don’ts

### Do:
*   **Embrace Asymmetry:** Align text to the left but allow data visualizations to break the grid and bleed toward the edges.
*   **Use Tonal Depth:** Always check if you can separate two areas with a color shift before reaching for a line.
*   **Prioritize Breathing Room:** Use the `xl` spacing scale between major research blocks to prevent cognitive overload.

### Don’t:
*   **Don't use pure black:** The deepest color should be `surface` (`#0e1322`). Pure black kills the "glassy" depth of the navy tones.
*   **Don't use high-contrast borders:** They shatter the illusion of a continuous, fluid AI environment.
*   **Don't over-animate:** Glows and pulses should be slow and "organic"—think of a breathing organism, not a flickering strobe light.