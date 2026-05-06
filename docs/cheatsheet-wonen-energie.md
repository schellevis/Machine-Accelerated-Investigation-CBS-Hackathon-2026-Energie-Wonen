# Cheat Sheet — CBS Hackathon Wonen & Energie
**8 mei 2026 · CBS-hoofdkantoor · Den Haag**

---

## 1. Onderzoeksvraag formuleren

Een goede onderzoeksvraag is de basis van alles. Zonder scherpe vraag levert de AI een vaag antwoord.

### Van breed naar scherp

```
Breed: "Iets doen met gasverbruik"
 ↓
Minder breed: "Welke buurten verbruiken veel gas?"
 ↓
Scherp: "Welke 15 gemeenten tonen de sterkste daling in gemiddeld aardgasverbruik per woning tussen 2022 en 2024, en hoe verhoudt dit zich tot het landelijk gemiddelde?"
```

### Checklist

- [ ] **Specifiek** — één fenomeen, niet "iets over energie"
- [ ] **Meetbaar** — beantwoordbaar met cijfers uit CBS-data
- [ ] **Geografisch** — buurt / wijk / gemeente / provincie?
- [ ] **Tijdgebonden** — welk jaar of welke periode?
- [ ] **Journalistiek relevant** — ongelijkheid, beleid, trend of verrassing?

### Voorbeeldvragen

**Wonen:** Welke gemeenten hebben de snelste stijging van koopprijzen in wijken met veel sociale huurwoningen?

**Energie:** Welke buurten tonen de sterkste daling in aardgasverbruik per woning (2019–2023)?

---

## 2. Van onderzoeksvraag naar prompt

Gebruik deze structuur voor een effectieve briefing aan de AI-agent:

```
## Context
[2–4 zinnen: waarom is dit journalistiek relevant? Welk beleid of
 welke ongelijkheid speelt er?]

## Databron
Gebruik CBS-tabel `[TABEL-ID]` via de CBS OData API.
Laad de wonen-energie-hackathon skill voor de juiste kolomnamen.

## Onderzoeksvraag
**[Jouw scherpe vraag, vetgedrukt]**

## Gewenst eindresultaat
1. Tabel top-15 gemeenten met kolom X en Y
2. Horizontaal staafdiagram met referentielijn landelijk gemiddelde
3. Korte samenvatting van 3–5 zinnen met de hoofdbevinding

## Verificatiecriteria
- Het totaal aantal gemeenten in de output is [verwacht aantal]
- De peildatum is [jaar] of het meest recente beschikbare jaar
- [Bekende uitschieters] staan op een logische plek in de ranking
```

**Tips:**
- Geef het tabel-ID expliciet mee — schrijf `86159NED`, niet "de energietabel"
- Schrijf verificatiecriteria vóórdat je de prompt uitvoert
- Één onderzoeksvraag per prompt — splits bij twijfel op

---

## 3. Beschikbare data — Wonen

Alle woningdata is beschikbaar per gemeente, de meeste ook per wijk en buurt.

| Thema | Wat kun je ermee? |
|-------|-------------------|
| **Woningvoorraad** | Hoeveel woningen zijn er per type (vrijstaand, appartement, tussenwoning)? Hoe oud zijn ze? Hoe groot gemiddeld? |
| **Eigendom** | Verhouding koop vs. huur, aandeel woningcorporaties vs. particuliere verhuurders, per gemeente 2012–2025 |
| **Koopprijzen** | Gemiddelde verkoopprijzen en prijsontwikkeling per gemeente en provincie, tijdreeks 1995–2025 |
| **Nieuwbouw & sloop** | Hoeveel woningen werden toegevoegd of gesloopt? Maandelijks bijgewerkt t/m 2026 |
| **Kerncijfers buurten** | Bevolking, inkomen, woningvoorraad én energieverbruik gecombineerd in één tabel — ideaal startpunt |

> **Tip:** Begin met de kerncijfertabel (2025) — deze combineert bevolking, woningkenmerken en energieverbruik per buurt in één overzicht.

---

## 4. Beschikbare data — Energie & Energietransitie

Energiedata gaat verder dan woningen — CBS dekt ook industrie, transport en de overheid.

| Thema | Wat kun je ermee? |
|-------|-------------------|
| **Gasverbruik per woning** | Gemiddeld aardgasverbruik (m³/jaar, temperatuurgecorrigeerd) per buurt, wijk en gemeente — voor 2022, 2023 en 2024 afzonderlijk beschikbaar, plus tijdreeks vanaf 2010 |
| **Elektriciteitsverbruik** | Gemiddeld verbruik (kWh/jaar) per woning, inclusief teruglevering van zonnepanelen |
| **Verwarmingsinstallaties** | Aandeel woningen op aardgas, warmtepomp of stadsverwarming — per gemeente (trend 2017–2022) en per wijk (2022) |
| **Zonnepanelen** | Geïnstalleerd vermogen (kWp) en aantal installaties per gemeente (2019–2025) en per wijk (2022) |
| **Energiebalans Nederland** | Totaal aanbod, omzetting en verbruik per sector (industrie, transport, huishoudens) — nationale tijdreeks |
| **Hernieuwbare energie** | Productie zonnestroom, wind, biomassa — ook uitgesplitst naar RES-regio en provincie |
| **Energielabels (A t/m G)** | ⚠️ Niet via CBS — gebruik [Transitiedata.nl](https://transitiedata.nl) voor labeldata per buurt |

> **Tip:** Gasverbruik en elektriciteitsverbruik zijn ook uitgesplitst naar woningtype (vrijstaand, appartement, etc.), zodat je appels met appels vergelijkt.

> **Tip:** Naast StatLine publiceert CBS ook **maatwerk** (in opdracht van ministeries) met journalistieke waarde: energiearmoede, subsidiemonitors, energieafhankelijkheid per land. Startpunt: [Energietransitie | CBS](https://www.cbs.nl/nl-nl/economie/industrie-en-energie/energietransitie) en het [overzicht aanvullende statistische diensten](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/publicaties/industrie-en-energie/overzicht-aanvullende-statistische-diensten-energietransitie).

---

*Bron: CBS StatLine open data — opendata.cbs.nl · Energielabels — transitiedata.nl*
*Hackathon georganiseerd door Stichting Momus, CBS en Open State Foundation*
