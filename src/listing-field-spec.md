# SpaceLink — Listing Form Field Specification

A reference for the provider "List your space" form. The goal is that every field
answers a **different** question, with no overlapping options between fields.

---

## Part 1 — Categorisation fields

Each field is independent (orthogonal). A provider can pick from every field without
ever ticking the same concept twice.

| Field | Question it answers | Input type |
|-------|--------------------|------------|
| Storage type | What kind of facility/operation is this? | multi-select |
| Storage environment | What conditions does the space hold? | multi-select |
| Goods type | What products can be stored here? | multi-select |
| Storage format | How is it physically stored / racked? | multi-select |
| Services offered | What value-added services are available? | multi-select |

### 1. Storage type (facility / operation)
- General warehouse
- Distribution centre
- Fulfilment centre
- Cross-dock / transload facility
- Bonded / customs-controlled warehouse
- Container & yard storage
- Outdoor / open-air storage
- Self-storage / small units

> Removed from the old list: *Cold storage* and *Dry storage* (these are **environment**),
> *Dangerous goods* (this is **goods type**), *Freight* (this is a **service**).

### 2. Storage environment (climate maintained)
- Ambient / dry (unconditioned)
- Climate-controlled (temperature + humidity)
- Chilled / refrigerated (2–8°C)
- Frozen (-18°C to -25°C)
- Humidity-controlled

> Collapsed duplicates: "Cold storage" = Chilled/refrigerated; "Climate-controlled"
> already covers the old "Temperature-controlled".

### 3. Goods type (what can be stored)
- General / dry goods
- Food & beverage
- Perishables (fresh produce, dairy)
- Pharmaceuticals & healthcare
- Dangerous / hazardous goods
- Chemicals
- Electronics & high-value
- Automotive parts
- Textiles & apparel
- Building materials
- Consumer goods / FMCG
- Bulk commodities / raw materials
- Fragile goods
- Oversized / heavy machinery

> Removed: *Dry storage* (environment), *E-commerce (Pick/Pack)* and *Third-party Logistics*
> (these are **services**).

### 4. Storage format (physical configuration)
- Pallet racking (selective)
- Drive-in / drive-through racking
- Push-back / pallet-flow racking
- Cantilever racking
- Floor / block stacked
- Bulk floor storage
- Shelving / small-parts bins
- Mezzanine
- Mobile racking
- Automated (AS/RS)

> Removed: *Dry storage* (environment). Rest was already clean.

### 5. Services offered (NEW — value-added)
Catches the items that were wrongly sitting under goods/type.
- Pick & pack / e-commerce fulfilment
- Third-party logistics (3PL)
- Cross-docking / transloading
- Kitting & assembly
- Labelling & repackaging
- Returns / reverse logistics
- Freight forwarding / transport
- Inventory management

---

## Part 2 — Pricing model

### Problem with the current form
"Pricing Types" offers four mutually exclusive options (Flexible, Per pallet, Per SQM,
Fixed Monthly) but the form only collects a single "Monthly Rate" field that doesn't change
based on the selection, and never shows a calculated total. A "$10.50" entry against
"Per SQM" is ambiguous — is that the per-m² rate or the whole monthly price? There's no
breakdown for either side.

### Recommended structure
The pricing model selection should **drive which inputs appear** and show a **live total**.

**Pricing models** (rename "Flexible" → "Custom / quote" for clarity):

| Model | Inputs shown | Monthly total formula |
|-------|-------------|----------------------|
| Per m² | rate ($/m²/mo) | `rate × total area (m²)` |
| Per pallet | rate ($/pallet), billing cycle (week/month), pallet positions | `rate × positions` (× 4.333 if weekly) |
| Fixed monthly | flat amount ($/mo) | the amount |
| Custom / quote | (optional) indicative min–max | none — shown as "Price on enquiry" |

**Billing cycle toggle** (Weekly / Monthly): NZ warehousing often quotes per pallet
**per week**, so support both and normalise to a monthly figure for display.
Weekly → monthly factor = 52 ÷ 12 = **4.333**.

**Optional add-ons** (flat $/month each — gives flexibility, ties to the amenities):
- Climate control surcharge
- 24/7 access
- WMS / inventory management
- Dock / loading handling

**Optional minimum commitment**: minimum term (months) and/or minimum monthly spend.

### Live summary (clarity for both sides)
```
Base                $8,400.00 / mo   ($10.50/m² × 800 m²)
+ Climate control     $400.00 / mo
─────────────────────────────────
Customer pays       $8,800.00 / mo
− SpaceLink fee 8%    −$704.00 / mo
─────────────────────────────────
You receive         $8,096.00 / mo
```

A plain-language line reinforces it, e.g.:
*"Customers see this space at $8,800/mo. After SpaceLink's 8% fee you receive $8,096/mo."*

> Fee % shown here is a placeholder — wire it to your actual commission config
> (the 15–18% blended rate, or the 6-month promotional rate during launch).

A working prototype of this module is provided alongside this doc
(`spacelink_pricing_module.html`).
