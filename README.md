# Apple Design System Knowledge Base & Agent Skill

An offline-first, structured knowledge base and GraphRAG knowledge graph paired with an AI coding skill (`SKILL.md`).

This repository enables autonomous coding assistants (Antigravity, Claude Code, Cursor, Windsurf) and developers to query, inspect, and apply interface design guidelines across Apple platforms.

---

## Repository Structure

```
.
├── SKILL.md              # Machine-readable skill definition for AI agents
├── README.md             # Project documentation and quickstart
├── LICENSE               # MIT License
├── .gitignore            # Environment ignore patterns
├── guidelines/           # Structured Markdown documentation
│   ├── index.md          # Topic taxonomy and index
│   └── ...               # Categorized topic guidelines
├── graphify-out/         # Pre-built GraphRAG knowledge graph
│   ├── graph.html        # Interactive in-browser relationship graph
│   ├── graph.json        # Node and edge database
│   └── GRAPH_REPORT.md   # Structural audit and cluster report
└── scraper/              # Python crawler pipeline
    ├── scraper.py        # Crawler orchestrator
    ├── fetcher.py        # Rate-limited HTTP client
    ├── parser.py         # Link and metadata parser
    └── writer.py         # Directory serializer
```

---

## Installation & Setup

### For Antigravity IDE

Install globally for all workspace profiles:

```bash
git clone https://github.com/premkumar0184/apple-hig-knowledge-base.git \
  ~/.config/AntigravityManager/profiles/default/home/.gemini/config/skills/apple-hig-design
```

### For Cursor, Claude Code, or Windsurf

Clone into a local path:

```bash
git clone https://github.com/premkumar0184/apple-hig-knowledge-base.git ~/apple-hig-knowledge-base
```

Reference `SKILL.md` within your project rules (`.cursorrules` or `CLAUDE.md`):

```markdown
When designing UI or writing frontend code for Apple platforms,
refer to the decision trees and specifications in:
~/apple-hig-knowledge-base/SKILL.md
```

---

## Querying the Knowledge Graph

### Graph Traversals via Graphify

With `graphifyy` installed (`pip install graphifyy`):

```bash
cd ~/apple-hig-knowledge-base

# Run semantic queries across the knowledge graph
graphify query "What are the rules for color contrast and dark mode?"
graphify query "How should navigation be structured in visionOS?"

# Trace shortest relationship paths between concepts
graphify path "Dark Mode" "Accessibility"
graphify path "Tab Bars" "Sidebars"
```

### Text Search

```bash
grep -rn -i "contrast ratio" guidelines/
grep -rn -i "dynamic type" guidelines/
```

### Visual Explorer

Open `graphify-out/graph.html` directly in any standard browser to explore the interactive visual graph offline.

---

## Scraper Maintenance

To update local content from source endpoints:

```bash
cd scraper
python3 -m pip install requests
python3 scraper.py
```

To regenerate the knowledge graph:

```bash
graphify .
```

---

## License

Tooling and skill files are available under the MIT License. Guidelines documentation and related trademarks are the property of Apple Inc.
