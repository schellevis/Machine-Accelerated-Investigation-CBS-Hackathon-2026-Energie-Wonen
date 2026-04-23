# Agents

## Wonen & Energie Hackathon

Voor analyses over de **woningmarkt** en **energietransitie** laad je de `wonen-energie-hackathon` skill uit `.kilo/skills/wonen-energie-hackathon/`. Deze skill bevat:

- Een curated **tabelregister** van ~15 vetted CBS-tabellen voor wonen en energie, met join-sleutels
- **Join-recepten** voor veelgebruikte combinaties (energielabels × woningkenmerken, verbruik × kerncijfers, etc.)
- **Analyse-recepten** voor journalistieke verhaallijnen (energielabel-achterstand, gasverbruiksdaling, zonnepanelen-adoptie, etc.)
- CBS **codeconventies** specifiek voor wonen- en energiethema's

Laad deze skill wanneer je:
- Werkt met woning- of energiedata van CBS StatLine
- Een onderzoeksvraag over wonen of energietransitie wilt uitwerken
- Tabellen wilt joinen op gemeentecode, wijkcode of buurtcode
- Verhaallijnen wilt vinden in de beschikbare datasets

## CBS StatLine Data

Voor de onderliggende CBS API-client gebruik je de `cbs-statline-skill` uit `.kilo/skills/cbs-statline-skill/`. Deze skill biedt:

- Een **CBS OData v4 client** (`cbs_client.py`) voor metadata-inspectie, data downloaden, paginering en code-naar-label resolutie
- Kennis van alle CBS-conventies (Perioden-codes, RegioS-codes, datastatus)
- Een algemeen **tabelregister** van ~35 vetted CBS-tabellen (breder dan wonen/energie)

Sleutel CBS-conventies:
- **Periodecodes**: `2023JJ00` = jaar, `2023KW01` = kwartaal, `2023MM06` = maand
- **Regiocodes**: `GM####` = gemeente, `WK######` = wijk, `BU########` = buurt. Altijd `.strip()` toepassen.
- **Datastatus**: `Definitief` (definitief), `Voorlopig` (`*`), `Nader voorlopig` (`**`)
- Controleer altijd op **verouderde tabellen** vóór gebruik

## Na het ophalen van CBS-data

Gebruik de passende downstream skill:

| Taak | Skill |
|------|-------|
| CSV/Excel opschonen of Nederlandse datakwalen oplossen | `data-cleaning-dutch` |
| Verhaallijnen vinden, uitschieters, trends, rankings | `data-analysis-journalism` |
| Grafieken en publicatieklare figuren maken | `data-viz-journalism` |
| Choropleth-kaarten per gemeente, wijk of buurt | `dutch-choropleth-maps` |
