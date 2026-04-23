# Cheat Sheet — CBS Hackathon Wonen & Energie
**8 mei 2026 · CBS-hoofdkantoor · Den Haag**

---

## 1. Onderzoeksvraag formuleren

Een goede onderzoeksvraag is de basis van alles. Zonder scherpe vraag levert de AI een vaag antwoord.

### Van breed naar scherp

```
Breed:    "Iets doen met gasverbruik"
         ↓
Minder breed: "Welke buurten verbruiken veel gas?"
         ↓
Scherp:   "Welke 15 gemeenten tonen de sterkste daling in gemiddeld
           aardgasverbruik per woning tussen 2022 en 2024, en
           hoe verhoudt dit zich tot het landelijk gemiddelde?"
```

> **Tip energielabels:** Energielabels (A t/m G) zijn beschikbaar via [Transitiedata.nl](https://transitiedata.nl), niet via CBS StatLine. Vermeld dit in je prompt als databron.

### Checklist goede onderzoeksvraag

- [ ] **Specifiek** — één duidelijk fenomeen, niet "iets over energie"
- [ ] **Meetbaar** — beantwoordbaar met getallen uit CBS-data
- [ ] **Geografisch** — op welk schaalniveau? (buurt / wijk / gemeente / provincie)
- [ ] **Tijdgebonden** — welk jaar of welke periode?
- [ ] **Journalistiek relevant** — raakt aan ongelijkheid, beleid, trend of verrassing

### Voorbeeldvragen

**Wonen:**
- Welke gemeenten hebben de snelste stijging van koopprijzen in wijken met veel sociale huurwoningen?
- In welke wijken is het aandeel kleine woningen (< 50 m²) het hoogst, en wie wonen er?

**Energie:**
- Welke buurten tonen de sterkste daling in aardgasverbruik per woning (2019–2023)?
- Welke gemeenten lopen het meest achter bij zonnepanelen, gecorrigeerd voor woningtype?

---

## 2. Van onderzoeksvraag naar prompt

Gebruik de **5-onderdelen structuur** voor een effectieve briefing aan de AI-agent.

### Template

```
## Context
[2–4 zinnen over waarom dit journalistiek relevant is. Welk beleid staat er
 op het spel? Welke ongelijkheid speelt er?]

## Databron
Gebruik CBS-tabel `[TABEL-ID]` ([naam tabel]) via de CBS OData API.
Laad de wonen-energie-hackathon skill voor de juiste kolomnamen en join-sleutels.

## Onderzoeksvraag
**[Schrijf hier je scherpe vraag, vetgedrukt]**

## Gewenst eindresultaat
1. [Concreet output 1 — bijv. tabel top-15 gemeenten met kolom X en Y]
2. [Concreet output 2 — bijv. horizontaal staafdiagram met referentielijn]
3. [Concreet output 3 — bijv. CSV-export als backup_DATUM.csv]
4. [Korte samenvatting van 3–5 zinnen met de hoofdbevinding]

## Verificatiecriteria
- Het totaal aantal gemeenten in de output is [verwacht aantal, bijv. 342]
- De peildatum is [jaar] of het meest recente beschikbare jaar
- [Bekende uitschieters] staan op een logische plek in de ranking
- De grafiek heeft een titel, aslabels en bronvermelding (CBS StatLine, [TABEL-ID])
```

### Tips voor effectieve prompts

- **Geef tabel-IDs expliciet mee** — schrijf `86159NED`, niet "de energieverbruikstabel"
- **Definieer de output precies** — "top-15" is beter dan "een lijst"
- **Schrijf verificatiecriteria vóórdat je de prompt uitvoert** — dit dwingt je om na te denken over wat je verwacht
- **Één onderzoeksvraag per prompt** — splits bij twijfel op in twee prompts
- **Vraag om een Python-script**, niet een notebook, als je het resultaat wilt hergebruiken

---

## 3. Beschikbare datasets — Wonen

| Tabel-ID | Naam | Regio-niveau | Wat zit erin |
|----------|------|-------------|--------------|
| **86165NED** | Kerncijfers wijken en buurten 2025 | GM / WK / BU | Bevolking, woningvoorraad, inkomen, energieverbruik, voorzieningen — alles in één tabel (meest recent) |
| **85984NED** | Kerncijfers wijken en buurten 2024 | GM / WK / BU | Idem, editie 2024 |
| **86098NED** | Levensloop van woningen; gebruiksfunctie, regio | GM | Voorraad, nieuwbouw, sloop, toevoegingen per gebruiksfunctie, 2015–2026 |
| **85035NED** | Woningvoorraad; woningtype, 1 januari | GM | Woningtype (vrijstaand, appartement, etc.) per gemeente |
| **82900NED** | Woningvoorraad; eigendom, type verhuurder, bewoning | GM | Koop/huur, corporatie vs. overige verhuurder, 2012–2025 |
| **82550NED** | Woningvoorraad; woningtype, bouwjaarklasse, oppervlak | GM | Woningtype × bouwjaarklasse × gemiddeld m², 2012–2026 |
| **83625NED** | Koopprijzen; gemiddelde verkoopprijzen | GM / provincie | Gemiddelde verkoopprijs per jaar en regio |
| **85792NED** | Koopprijzen; prijsindex 2020=100 | GM / provincie | Prijsontwikkeling t.o.v. basisjaar 2020 |

**Tip:** Begin met `86165NED` — dit is de meest recente en meest complete tabel en bevat al energieverbruik per buurt.

---

## 4. Beschikbare datasets — Energie & Energietransitie

| Tabel-ID | Naam | Regio-niveau | Wat zit erin |
|----------|------|-------------|--------------|
| **86159NED** | Energieverbruik woningen; wijken/buurten, 2024 | GM / WK / BU | Gas + elektra per woning per woningtype (meest recent) |
| **85999NED** | Energieverbruik woningen; wijken/buurten, 2023 | GM / WK / BU | Idem, 2023 |
| **85697NED** | Energieverbruik woningen; wijken/buurten, 2022 | GM / WK / BU | Idem, 2022 |
| **81528NED** | Energieverbruik woningen; woningtype en regio's (2010–) | GM / provincie | Tijdreeks vanaf 2010 — voor trendanalyse |
| **84948NED** | Woningen; hoofdverwarmingsinstallaties, regio 2017–2022 | GM | Aandeel gas/elektra/stadsverwarming per gemeente — voor transitietrendanalyse |
| **85677NED** | Woningen; hoofdverwarmingsinstallaties, wijk/buurt, 2022 | WK / BU | Idem op wijkniveau — voor kaarten |
| **85005NED** | Zonnestroom; vermogen woningen, regio | GM | Totaal geïnstalleerd vermogen (kWp) en aantal installaties 2019–2025 |
| **86044NED** | Zonnestroom; zonnepanelen woningen, wijk/buurt, 2022 | WK / BU | Zonnestroom op wijkniveau — voor kaarten |

> ⚠️ **Energielabels (A t/m G) zijn niet beschikbaar via CBS StatLine.** Gebruik [Transitiedata.nl](https://transitiedata.nl) voor energielabels per buurt/gemeente.

**Cross-domein:**

| Tabel-ID | Naam | Gebruik |
|----------|------|---------|
| **85140NED** | Energieverbruik; woningtype, oppervlakte, bouwjaar, bewoning | Energieverbruik × woningkenmerken in één tabel, 2019–2024 |

---

## 5. Tabellen combineren

### Regiocode-hiërarchie

```
Nederland (NL01)
 └── Provincie (PV##)         bijv. PV27 = Noord-Holland
      └── Gemeente (GM####)   bijv. GM0363 = Amsterdam
           └── Wijk (WK######)     bijv. WK036300
                └── Buurt (BU########) bijv. BU03630000
```

Wijk- en buurtcodes bevatten de gemeentecode als prefix. Hierdoor kun je altijd aggregeren naar een hoger niveau.

### ⚠️ Trailing spaces

CBS-regiocodes bevatten trailing spaces. Altijd strippen:

```python
df['RegioS'] = df['RegioS'].str.strip()
```

### Join-recepten

**Eigendom × Koopprijzen (per gemeente)**
```python
import cbsodata, pandas as pd

eigendom = pd.DataFrame(cbsodata.get_data('82900NED',
               filters="startswith(RegioS,'GM')"))
prijzen  = pd.DataFrame(cbsodata.get_data('83625NED',
               filters="startswith(RegioS,'GM')"))

for df in [eigendom, prijzen]:
    df['RegioS'] = df['RegioS'].str.strip()
    df['Jaar'] = df['Perioden'].str[:4]

merged = eigendom.merge(prijzen, on=['RegioS', 'Jaar'])
```

**Energieverbruik × Kerncijfers (per buurt — inclusief inkomen)**
```python
verbruik    = pd.DataFrame(cbsodata.get_data('86159NED',
                  filters="startswith(RegioS,'BU')"))
kerncijfers = pd.DataFrame(cbsodata.get_data('86165NED'))  # 2025, meest recent

for df in [verbruik, kerncijfers]:
    df['RegioS'] = df['RegioS'].str.strip()

merged = verbruik.merge(kerncijfers, on='RegioS')
```

**Trendanalyse energieverbruik over meerdere jaren**
```python
jaren = {
    '2022': cbsodata.get_data('85697NED', filters="startswith(RegioS,'GM')"),
    '2023': cbsodata.get_data('85999NED', filters="startswith(RegioS,'GM')"),
    '2024': cbsodata.get_data('86159NED', filters="startswith(RegioS,'GM')"),
}
frames = []
for jaar, data in jaren.items():
    df = pd.DataFrame(data)
    df['Jaar'] = jaar
    frames.append(df)
trend = pd.concat(frames)
```

---

## 6. CBS-codeconventies

### Periodecodes

| Code | Betekenis |
|------|-----------|
| `2023JJ00` | Jaar 2023 (volledig jaar) |
| `2023KW01` | Kwartaal 1, 2023 (jan–mrt) |
| `2023KW04` | Kwartaal 4, 2023 (okt–dec) |
| `2023MM01` | Januari 2023 |
| `2023MM12` | December 2023 |

```python
# Jaar extraheren uit periodecode
df['Jaar'] = df['Perioden'].str[:4].astype(int)

# Alleen jaardata ophalen
df = pd.DataFrame(cbsodata.get_data('81528NED',
    filters="endswith(Perioden,'JJ00')"))
```

### Regiocodes

| Prefix | Niveau | Voorbeeld | Naam |
|--------|--------|-----------|------|
| `NL01` | Nederland | `NL01  ` | Nederland totaal |
| `PV##` | Provincie | `PV27` | Noord-Holland |
| `GM####` | Gemeente | `GM0363` | Amsterdam |
| `WK######` | Wijk | `WK036300` | — |
| `BU########` | Buurt | `BU03630000` | — |
| `LD##` | Landsdeel | `LD01` | Noord-Nederland |
| `CR####` | COROP-gebied | `CR16` | Groot-Amsterdam |

```python
# Alleen gemeenten
df_gem  = df[df['RegioS'].str.strip().str.startswith('GM')]

# Alleen buurten
df_buur = df[df['RegioS'].str.strip().str.startswith('BU')]

# Gemeente-code uit buurt-code halen
df['GemeenteCode'] = 'GM' + df['RegioS'].str.strip().str[2:6]
```

### Datastatus

| Waarde | Symbool | Betekenis |
|--------|---------|-----------|
| `Definitief` | — | Definitief, geen revisie verwacht |
| `Voorlopig` | `*` | Onder voorbehoud, revisie mogelijk |
| `Nader voorlopig` | `**` | Tweede voorlopige versie |

```python
# Statusverdeling controleren
print(df['Status'].value_counts())
```

### Ontbrekende waarden

CBS gebruikt `.` (punt) voor missende waarden in numerieke kolommen. Pandas leest dit als `NaN` als je `na_values=['.']` opgeeft:

```python
df = pd.read_csv('bestand.csv', sep=';', decimal=',', na_values=['.'])
```

---

## 7. API-verbinding

### Basispatroon

```python
import cbsodata
import pandas as pd

# Metadata van een tabel
meta = cbsodata.get_meta('86165NED')

# Kolommen bekijken
print(pd.DataFrame(meta['DataProperties'])[['Key', 'Title', 'Type']])

# Codelijst bekijken (bijv. regio-labels)
print(pd.DataFrame(meta['RegioSCodes']))

# Alle data ophalen
df = pd.DataFrame(cbsodata.get_data('86165NED'))

# Met OData-filter (sneller, minder data)
df = pd.DataFrame(cbsodata.get_data('86165NED',
    filters="startswith(RegioS, 'GM')"))
```

### Directe OData v4 URL
```
https://opendata.cbs.nl/ODataApi/odata/{TABEL_ID}/TypedDataSet
```

Voorbeeld:
```
https://opendata.cbs.nl/ODataApi/odata/86159NED/TypedDataSet?$filter=startswith(RegioS,'GM')&$top=500
```

### Paginering

CBS retourneert maximaal 100.000 cellen per request. Bij grote tabellen is er een `@odata.nextLink` in de response. De `cbsodata` library handelt dit automatisch af.

```python
# Handmatige paginering als cbsodata niet werkt
import requests

url = "https://opendata.cbs.nl/ODataApi/odata/85984NED/TypedDataSet"
results = []
while url:
    r = requests.get(url).json()
    results.extend(r['value'])
    url = r.get('@odata.nextLink')

df = pd.DataFrame(results)
```

### Alternatief: Transitiedata.nl

Voor buurt-niveau energiedata die CBS (nog) niet publiceert:
- Energielabeldistributie per buurt
- Gasdaling 2019–2025 per buurt
- Warmteplannen en warmtebronnen per buurt

```python
# Transitiedata gebruikt GeoJSON/API — zie documentatie op transitiedata.nl
```

---

## 8. Skill activeren in Kilo Code

1. Open VS Code → klik het **Kilo Code**-icoon in de sidebar
2. Klik op **Add Skill**
3. Wijs naar de map `.kilo/skills/wonen-energie-hackathon/`
4. De skill is nu geladen — typ je prompt en de agent gebruikt de tabelkennis automatisch

**Laad daarnaast ook `cbs-statline-skill`** voor de volledige CBS API-client (`cbs_client.py`).

**Stroomschema:**

```
Onderzoeksvraag
      ↓
[wonen-energie-hackathon skill]  ← domeinkennis, tabelregister, join-recepten
      ↓
[cbs-statline-skill]             ← CBS OData API-client, paginering
      ↓
[data-cleaning-dutch]            ← fix komma-decimalen, puntcodering, Dutch quirks
      ↓
[data-analysis-journalism]       ← outliers, trends, rankings
      ↓
[data-viz-journalism]            ← publicatieklare grafiek (Altair / matplotlib)
[dutch-choropleth-maps]          ← choropleth kaart per gemeente/wijk/buurt
```

---

*Bron: CBS StatLine open data — opendata.cbs.nl · Transitiedata — transitiedata.nl*
*Hackathon georganiseerd door Stichting Momus, CBS en Open State Foundation*
