---
name: apple-hig-design
description: Master Apple Human Interface Guidelines (HIG) for iOS, iPadOS, macOS, visionOS, watchOS, and Apple-aligned web apps. Use when designing user interfaces, SwiftUI/web components, navigation architectures, Dark Mode, typography, accessibility, or querying the Apple HIG knowledge base.
---

# Apple HIG Design

Master Apple's Human Interface Guidelines (HIG) across iOS, iPadOS, macOS, visionOS, and watchOS to build intuitive, accessible, and platform-native digital experiences.

---

## 1. When to Consult This Skill & Knowledge Base

Consult this skill whenever you are:
- **Designing or building apps for Apple platforms** (SwiftUI, UIKit, AppKit) or **Apple-inspired web experiences**.
- **Architecting navigation flows** (choosing between Tab Bars, Sidebars, Navigation Stacks, Modals, Sheets, or Ornaments).
- **Styling typography & layout** (adopting SF Pro, Dynamic Type scales, layout grids, and touch/pointer target sizes).
- **Implementing color & appearances** (Dark Mode palettes, vibrancy, semantic system colors, Apple Glass materials).
- **Ensuring accessibility (a11y)** (WCAG contrast ratios, VoiceOver labels, Dynamic Type scaling, Reduce Motion).
- **Choosing user input controls** (Buttons, Menus, Popovers, Context Menus, Toolbars, Pickers, Haptics).
- **Designing platform features** (Live Activities, Widgets, SF Symbols, App Clips, SharePlay, Shortcuts).

---

## 2. Knowledge Base Location & How to Query It

The entire structured Apple HIG documentation (~179 articles, 288k words, 894 concepts, 79 community clusters) is persistently cached and indexed at:
`/home/prem/apple-hig-knowledge-base/`

### Query Strategy

1. **Semantic Search with Graphify (Recommended for conceptual, relational, or multi-platform questions):**
   ```bash
   # From /home/prem/apple-hig-knowledge-base or globally:
   graphify query "What are the rules for color contrast and dark mode in Apple HIG?"
   graphify query "How should navigation be structured in visionOS?"
   graphify query "When should I use a sheet vs popover on iPadOS?"
   ```

2. **Concept Relationship & Path Tracing:**
   ```bash
   graphify path "Dark Mode" "Accessibility"
   graphify path "Tab Bars" "Sidebars"
   ```

3. **Targeted Keyword Grep (Fast lookup for specific properties, values, or components):**
   ```bash
   grep -rn -i "contrast ratio" /home/prem/apple-hig-knowledge-base/
   grep -rn -i "dynamic type" /home/prem/apple-hig-knowledge-base/typography/
   grep -rn -i "ornaments" /home/prem/apple-hig-knowledge-base/
   ```

4. **Direct Article Reading:**
   Use `view_file` on the target topic file:
   - `/home/prem/apple-hig-knowledge-base/foundations/accessibility.md`
   - `/home/prem/apple-hig-knowledge-base/color/index.md`
   - `/home/prem/apple-hig-knowledge-base/dark-mode/index.md`
   - `/home/prem/apple-hig-knowledge-base/typography/index.md`
   - `/home/prem/apple-hig-knowledge-base/tab-bars/index.md`
   - Full URL-to-path index available in: `/home/prem/apple-hig-knowledge-base/metadata.json`

> [!CAUTION]
> **Safety Rule**: Never attempt to fetch or read `https://www.apple.com/legal/internet-services/terms/site.html`.

---

## 3. Core Apple Design Principles

Every Apple platform interface rests on three foundational pillars:

### 1. Clarity
- **Text must be legible at every size.** Never compromise readability for decoration.
- **Icons are precise and lucid.** Use SF Symbols whenever possible to maintain consistent visual weight with system fonts.
- **Emphasize functionality.** Non-critical embellishments are minimized; color is used purposefully to highlight action or state.

### 2. Deference
- **Fluid motion and crisp UI defer to the content.** The interface stays out of the user's way.
- **Full bleed & spaciousness.** Content occupies the natural screen bounds while subtle translucency and materials hint at surrounding context.
- **Direct manipulation.** Gestures feel physical and responsive with zero perceived latency.

### 3. Depth
- **Visual hierarchy through layering.** Windows, sheets, panels, and ornaments create clear spatial order.
- **Vibrancy and materials.** Background blur (`Material`) conveys elevation and proximity to the user.
- **Consistent physical cues.** Haptics and realistic physics reinforce interaction boundaries.

---

## 4. Universal Design System Specifications

### Typography Scale (Default SF Pro Sizes & Weights)
| Platform | Large Title | Title 1 | Headline / Body | Subheadline / Callout | Caption |
|---|---|---|---|---|---|
| **iOS / iPadOS** | 34pt (Regular) | 28pt (Regular) | 17pt (Semibold / Regular) | 15pt / 16pt | 12pt / 11pt |
| **macOS** | — | — | 13pt (Regular / Medium) | 11pt (Regular) | 10pt (Regular) |
| **tvOS** | — | 76pt (Medium) | 38pt (Medium / Regular) | 29pt (Regular) | 25pt (Regular) |
| **visionOS** | 34pt (Regular) | 28pt (Regular) | 17pt (Regular) | 15pt (Regular) | 12pt (Regular) |
| **watchOS** | — | — | 16pt (Regular) | 15pt (Regular) | 12pt / 10pt |

### Touch & Pointer Targets
- **iOS / iPadOS:** Minimum **44 × 44 pt** touch target (even if visual icon is 24 × 24 pt).
- **visionOS:** Minimum **60 × 60 pt** eye-gaze target with at least **16 pt** separation between clickable elements.
- **watchOS:** Minimum **48 × 48 pt** tap target; keep full-width buttons where possible.
- **macOS:** Standard controls typically **16–28 pt** height, optimized for cursor precision.

### Color & Contrast Standards
- **Standard Text / Icons (up to 17pt):** Minimum **4.5:1** contrast ratio against background.
- **Large Text (18pt+ or 14pt+ bold):** Minimum **3:1** contrast ratio.
- **Dark Mode parity:** Always supply dynamic variants or semantic tokens (`systemBackground`, `secondarySystemBackground`, `label`, `secondaryLabel`). Never hardcode hex values.
- **Color Independence:** Never use color as the sole indicator of status or error; pair with icons, shapes, or text labels.

---

## 5. Platform-Specific Decision Trees

```
                              [Which Platform?]
                                      │
       ┌──────────────┬───────────────┼───────────────┬──────────────┐
       ▼              ▼               ▼               ▼              ▼
     [iOS]         [iPadOS]        [macOS]        [visionOS]     [watchOS]
```

### A. iOS Decision Flow
1. **Primary Navigation Hierarchy:**
   - **3 to 5 destinations?** → **Tab Bar** at bottom (persistent, icons + labels).
   - **Fewer than 3?** → Single view with header controls or flat page control.
   - **More than 5?** → Consolidate into 4 tabs + 1 "More" tab, or rethink information architecture.
2. **Drill-down vs. Task Flow:**
   - **Hierarchical content (parent → child)?** → **Navigation Stack** with standard top Navigation Bar (`push`/`pop`).
   - **Self-contained distinct task (create, edit, settings)?** → **Modal Sheet** (detents: medium or large).
   - **Critical alert or confirmation?** → **Alert** (max 2 buttons) or **Action Sheet** (contextual destructive choices).
3. **Actions & Menus:**
   - **Secondary actions on a view?** → Pull-down menu attached to toolbar button.
   - **Object-level actions?** → Context Menu (tap-and-hold / haptic touch).

---

### B. iPadOS Decision Flow
1. **Windowing & Screen Size:**
   - **Compact width (Split View / Slide Over)?** → Gracefully adapt down to iOS Tab Bar and single-column navigation.
   - **Regular width?** → Use **NavigationSplitView** with **Sidebar** (primary list) + **Detail** pane.
2. **Navigation & Menus:**
   - Replace bottom Tab Bar with an expandable **Sidebar**.
   - Use **Popovers** anchored to source elements instead of full-screen Action Sheets.
   - Support hardware keyboard shortcuts and trackpad pointer hover effects.

---

### C. macOS Decision Flow
1. **App Shell Architecture:**
   - **Unified Toolbar** containing Window Title, Search field, segmented controls, and primary action buttons.
   - **Source List Sidebar** on the left for library / folder navigation.
   - **Three-column layout:** Sidebar → Content List → Detail/Inspector.
2. **Commands & Discoverability:**
   - Every primary action must exist in the **Menu Bar** (File, Edit, View, Window).
   - Provide standard keyboard shortcuts (`Cmd+S`, `Cmd+N`, `Cmd+F`, `Cmd+W`).
   - Right-click Context Menus for shortcuts, never for unique unfindable actions.
3. **Window Management:**
   - Design for variable window resizing, multiple tabs, and Stage Manager.

---

### D. visionOS Decision Flow
1. **Spatial Container Selection:**
   - **Standard information & 2D content?** → **Window** in Shared Space.
   - **Self-contained 3D object / model?** → **Volume** (bounded 3D box with shared depth).
   - **Fully engaging cinematic / game experience?** → **Full Immersive Space**.
2. **Interface Chrome:**
   - **Window Controls:** Keep bottom Window Bar for resize and repositioning clear.
   - **Primary Navigation:** Floating **Ornaments** anchored to the bottom or edge of the window.
   - **Tabs:** Attached vertically to the leading side of the window.
3. **Visual Aesthetics:**
   - Always use **System Glass Material** for windows. Never paint solid opaque backgrounds.
   - Interactive elements must activate hover/highlight state upon eye fixation before pinch selection.

---

### E. watchOS Decision Flow
1. **Session Length:**
   - Optimize for **2 to 5 second glances**. Every key metric must be visible immediately.
2. **Hierarchy:**
   - **Hierarchical:** Action-oriented apps with one main list drilling down.
   - **Page-based:** Flat swipeable cards (weather, fitness).
3. **Aesthetics & Ergonomics:**
   - Backgrounds are strictly `#000000` pure black (blends with OLED bezel).
   - Full-width rounded buttons with bold iconography.
   - Digital Crown scrolling with haptic detent feedback.
   - Complication support across circular, corner, rectangular, and inline formats.

---

## 6. Implementation Checklist for Agents

When generating UI code (SwiftUI, React, CSS, HTML) following this skill:
- [ ] **Dynamic Color:** Are colors referencing system tokens or CSS `@media (prefers-color-scheme: dark)`?
- [ ] **Contrast:** Does body text meet 4.5:1 against its immediate background in both light and dark modes?
- [ ] **SF Symbols:** Are icons semantic, consistent in weight (`.medium` default), and aligned with typography?
- [ ] **Target Sizing:** Are interactive elements padded to meet platform minimums (44pt iOS / 60pt visionOS)?
- [ ] **Navigation Semantics:** Does the top-level container match platform norms (Tab Bar vs. Sidebar vs. Ornament)?
- [ ] **Feedback & Motion:** Are transitions smooth, non-disorienting, and respectful of `prefers-reduced-motion`?
