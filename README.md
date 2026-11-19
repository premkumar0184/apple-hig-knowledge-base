# 🍏 Apple HIG Knowledge Base & `apple-hig-design` Agent Skill

A comprehensive, structured offline knowledge base of **Apple's Human Interface Guidelines (HIG)** paired with an **agent-ready skill (`SKILL.md`)** and a **GraphRAG knowledge graph**.

Designed to empower developers, designers, and AI coding assistants (Antigravity, Claude Code, Cursor, Windsurf, Copilot) to build platform-native iOS, iPadOS, macOS, visionOS, and watchOS interfaces that conform to Apple's design principles.

---

## 🌟 What's Included

- **`SKILL.md`**: Master design skill file with decision trees, typography scales, contrast minimums, and platform-specific rules.
- **179 Markdown Articles**: Full offline documentation scraped directly from Apple's native Markdown endpoints.
  - Complete coverage across **Foundations**, **Patterns**, **Components**, **Inputs**, **Technologies**, and **Platform Overviews**.
  - Normalized YAML frontmatter with titles, roles, and original Apple documentation URLs.
- **Interactive Knowledge Graph (`graphify-out/`)**:
  - `graph.html`: Interactive, searchable 894-node visual graph of concepts and design relationships.
  - `graph.json`: GraphRAG-ready node/edge database with 79 community clusters.
  - `GRAPH_REPORT.md`: Comprehensive audit trail and design system relationship analysis.
- **Scraper Engine (`scraper/`)**: Python crawler to keep the knowledge base updated as Apple updates HIG.

---

## 🚀 Quick Start: How to Install & Use This Skill

### Option 1: In Antigravity / Gemini Code Assist

To make this skill globally available to all Antigravity agent sessions:

```bash
# 1. Clone the repository
git clone https://github.com/premkumar0184/apple-hig-knowledge-base.git ~/.config/AntigravityManager/profiles/default/home/.gemini/config/skills/apple-hig-design

# Or symlink the SKILL.md into your global skills folder:
mkdir -p ~/.config/AntigravityManager/profiles/default/home/.gemini/config/skills/apple-hig-design
ln -s "$(pwd)/SKILL.md" ~/.config/AntigravityManager/profiles/default/home/.gemini/config/skills/apple-hig-design/SKILL.md
```

### Option 2: In Claude Code, Cursor, Windsurf, or Other Agents

Clone anywhere and reference `SKILL.md`:

```bash
git clone https://github.com/premkumar0184/apple-hig-knowledge-base.git ~/apple-hig-knowledge-base
```

Add to your project's `.cursorrules`, `CLAUDE.md`, or system prompt:

```markdown
When designing UI or writing frontend code for Apple platforms or Apple-styled web apps,
refer to the guidelines in ~/apple-hig-knowledge-base/SKILL.md.
```

---

## 🔍 How to Query the Knowledge Base

### 1. Semantic Graph Traversals (via `graphify`)

If you have `graphify` installed (`pip install graphifyy`):

```bash
cd ~/apple-hig-knowledge-base

# Ask complex design questions across the entire knowledge base
graphify query "What are the rules for color contrast and dark mode in Apple HIG?"
graphify query "How should navigation and spatial layout be structured for visionOS?"
graphify query "When should I use a sheet vs popover on iPadOS?"

# Trace conceptual paths between two ideas
graphify path "Dark Mode" "Accessibility"
graphify path "Tab Bars" "Sidebars"
```

### 2. Fast Keyword Search (`grep`)

```bash
# Search specific contrast or touch target specifications
grep -rn -i "contrast ratio" ~/apple-hig-knowledge-base/
grep -rn -i "44 pt" ~/apple-hig-knowledge-base/
grep -rn -i "ornaments" ~/apple-hig-knowledge-base/
```

### 3. Open the Interactive Visual Graph

Open `graphify-out/graph.html` directly in any web browser to explore the clusters, god nodes, and interconnectivity of Apple's design system without running any local server.

---

## 📐 Key Specifications at a Glance

### Touch & Pointer Targets
| Platform | Minimum Target | Notes |
|---|---|---|
| **iOS / iPadOS** | **44 × 44 pt** | Even if the visual glyph is 24 × 24 pt |
| **visionOS** | **60 × 60 pt** | Eye-gaze interactive element with ≥ 16 pt spacing |
| **watchOS** | **48 × 48 pt** | Full-width buttons preferred |
| **macOS** | **16–28 pt height** | Optimized for precision cursor pointer |

### Contrast Minimums
- **Small / Body Text (up to 17pt):** Minimum **4.5:1** contrast ratio.
- **Large Text (18pt+ or 14pt+ bold):** Minimum **3:1** contrast ratio.
- **Dark Mode:** Always provide dynamic/semantic color tokens. Never hardcode hex values.

---

## 🛠️ Re-running or Updating the Scraper

To update the local knowledge base with the latest additions from Apple:

```bash
cd ~/apple-hig-knowledge-base/scraper
python3 -m pip install requests
python3 scraper.py
```

To regenerate the knowledge graph:

```bash
graphify ~/apple-hig-knowledge-base
```

---

## ⚖️ Attribution & Disclaimer

- The guidelines and design concepts herein are created and copyrighted by **Apple Inc.**
- This repository is an educational and reference knowledge base intended to assist developers and AI agents in adhering to Apple's Human Interface Guidelines.
- Does not scrape or access any restricted Apple terms pages.
