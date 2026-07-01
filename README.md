# Machine-Accelerated Investigation — CBS Hackathon: Wonen & Energie

**8 mei 2026 · CBS-hoofdkantoor · Den Haag**

Een samenwerking van [Stichting Momus](https://www.momus.nl/), [CBS](https://www.cbs.nl/), [Open State Foundation](https://openstate.eu/) en het ministerie van Binnenlandse Zaken.

Datajournalisten en programmeurs werken samen aan onderzoeksvragen over de **woningmarkt** en **energietransitie** — ondersteund door CBS open data en AI-codering agents. Doel: van idee naar werkende datapipeline in minuten in plaats van dagen.

## Wat dit repo bevat

Vijf AI-agent skills die samenwerken in een keten — van het ophalen van CBS-data tot een publicatieklare grafiek of kaart:

| Skill | Wat het doet |
|---|---|
| `wonen-energie-hackathon` | Domeinkennis wonen & energie: curated tabelregister, join-recepten, analyse-ideeën |
| `energietransitie-skill` | Macro- en sectorenergiedata los van woningen: energiebalansen, hernieuwbare energie, bedrijven, subsidies, energiearmoede |
| `cbs-statline-skill` | CBS OData API-client, regio- en periodecodes ophalen, paginering |
| `data-cleaning-dutch` | Nederlandse datakwalen oplossen (puntkomma-CSV, komma-decimalen, ontbrekende waarden) |
| `data-analysis-journalism` | Verhaallijnen vinden — uitschieters, trends, rankings, correlaties |
| `data-viz-journalism` | Publicatieklare grafieken (Altair, matplotlib, Plotly) |
| `dutch-choropleth-maps` | Choropleth-kaarten per gemeente, wijk of buurt |

## Cheat sheet

Snel overzicht van onderzoeksvraag formuleren, van vraag naar prompt, beschikbare datasets, join-recepten, codeconventies en API-verbinding:

→ [`docs/cheatsheet-wonen-energie.md`](docs/cheatsheet-wonen-energie.md)

## Dagprogramma

| Tijd | Onderdeel |
|------|-----------|
| 9:00–9:45 | Inloop, registratie en koffie |
| 9:45–10:15 | Plenaire opening — CBS over thema's wonen en energie |
| 10:15–10:30 | Introductie cheat sheet en skills |
| 10:30–12:00 | Groepsvorming en onderzoeksvraag uitwerken (met CBS-experts) |
| 12:00–13:00 | Lunch en netwerken |
| 13:00–14:15 | Werksessie 1 — onderzoeksplan en data ophalen |
| 14:15–16:15 | Werksessie 2 — analyse, visualisatie en pitch voorbereiden |
| 16:15–17:00 | Pitches (3 min per team) + feedback CBS-experts |
| 17:00–18:00 | Borrel en netwerken |

## Vereisten

| Tool | Waarvoor | Installeren |
|---|---|---|
| **VS Code** | Code-editor | [code.visualstudio.com/download](https://code.visualstudio.com/download) |
| **Git** | Repository en skills clonen | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **Kilo Code** | AI coding agent (VS Code extensie) | [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=kilocode.kilo-code) |
| **uv** | Python package manager — installeert Python én alle dependencies in één stap | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |

## Setup

### 1. Kilo Code instellen

1. Open VS Code en zorg dat Kilo Code is geïnstalleerd
2. Sluit het ingebouwde Chat-tabblad als dat open staat
3. Klik op het **Kilo Code-icoon** in de sidebar
4. Klik op het **tandwiel-icoon** binnen Kilo Code
5. Klik op **Providers**
6. Klik naast **OpenRouter** op **+ Connect**
7. Plak de API-sleutel die aan het begin van de hackathon wordt gedeeld
8. Selecteer onderaan het scherm het model dat door de organisatie wordt aangegeven

### 2. Repository installeren

```bash
git clone --recurse-submodules https://github.com/linksmith/Machine-Accelerated-Investigation-CBS-Workshop.git
cd Machine-Accelerated-Investigation-CBS-Workshop
```

**Mac / Linux** (met `make`):
```bash
make setup
make jupyter
```

**Windows** (of zonder `make`):
```bash
uv sync --group dev --group viz
uv run jupyter lab
```

Installeert alle Python-dependencies (~30 seconden) en opent daarna JupyterLab in de browser.

Voor choropleth-kaarten:

```bash
# Mac / Linux
make setup-geo

# Windows
uv sync --all-groups
```

### Skills bijwerken

De submodule-skills leven elk in een eigen repository. Laatste versie ophalen:

```bash
# Mac / Linux
make update

# Windows
git submodule update --remote --merge
```

Bij het pullen van wijzigingen aan het workshop-repo inclusief submodules:

```bash
git pull --recurse-submodules
```

Als je zonder `--recurse-submodules` hebt gekloond en de skill-mappen leeg zijn:

```bash
git submodule update --init --recursive
```

## Skills gebruiken

Open Kilo Code en laad een skill voordat je begint. Klik op **Add Skill** en wijs naar de skill-map, of installeer via de GitHub release-URL. In Claude Code gebruik je `/skill`.

**Aanbevolen volgorde:**
1. `wonen-energie-hackathon` — laad als eerste, voor domeinkennis en tabelregister
2. `energietransitie-skill` — voor energievragen los van woningen (macro/sector)
3. `cbs-statline-skill` — voor de CBS API-client
4. `data-analysis-journalism` / `data-viz-journalism` / `dutch-choropleth-maps` — naar behoefte

## Presentatie

De workshop-slides staan in de map `presentation/`:

- [`presentation/presentatie.pdf`](presentation/presentatie.pdf) — PDF-versie
- [`presentation/presentatie.pptx`](presentation/presentatie.pptx) — PowerPoint-versie

## Over data/expedities

[data/expedities](https://dataexpedities.nl/) zijn intensieve hackathons waar datajournalisten CBS-statistieken gebruiken om onderzoeksverhalen te ontwikkelen. Dit repo is het voorbereidingsmateriaal: het geeft deelnemers de tools en skills om op de dag zelf direct van start te kunnen.

## Licentie

MIT
