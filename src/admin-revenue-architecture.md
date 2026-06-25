# SpaceLinq: Admin-Side Revenue Architecture & Phased Rollout

*How SpaceLinq (the platform) captures value, what to set up for each stream, and the sequence to switch them on without choking growth.*

---

## The governing principle: monetise liquidity, not the calendar

A two-sided marketplace lives or dies on liquidity — enough providers that seekers find what they want, and enough seekers that providers stay listed. Every revenue stream below is sequenced against **liquidity milestones**, not just "month 6." The 6-month free window is your *promise*; the milestones are your *trigger*.

Three rules guide the whole rollout:

1. **Free where it buys supply or demand.** Seeker search/discovery and basic listings stay free permanently. These are acquisition costs, not revenue opportunities.
2. **Charge where you've proven value.** A fee only switches on after the platform has demonstrably done the work (made the match, moved the money, reduced the risk).
3. **Some revenue should subsidise growth.** Featured-listing and ad income in early phases funds referral rewards and founding-member discounts — revenue that recycles into acquisition rather than margin.

---

## Refinements to the earlier revenue model

Two things to correct from the first revenue report before building on it:

**The percentage commission breaks at the top end.** A 15% take on a $200k/year warehouse contract is $30k — both parties will transact around you (disintermediation, which is already flagged as your biggest platform risk). Percentage works for small and mid deals; large/long deals need a **capped fee or a flat success fee + small ongoing platform fee** so the take never becomes large enough to be worth dodging.

**Seekers pay on the transaction, not for discovery.** You've been clear seekers aren't charged to find space. So frame the seeker-side fee as a *booking/transaction fee* applied only at the point of a confirmed rental — never a search paywall. This keeps the top of the funnel completely free and maximises sign-ups.

The corrected take-rate ceiling by deal size:

| Monthly rental value | Model | Effective take |
|---|---|---|
| Under $500 | % commission | ~20–23% |
| $500–$2,000 | % commission | ~15–18% |
| $2,000–$5,000 | % commission | ~12–15% |
| $5,000–$15,000 | % commission, capped | ~8–10% |
| $15,000+ | Flat success fee + monthly platform fee | Capped $ amount |

---

## The admin revenue stack — five layers you control

Think of SpaceLinq's income as five stacked layers. Each sits on top of the one below and only switches on once the layer beneath is stable.

### Layer 1 — Transaction take rate (the engine)

The core. A split commission off every confirmed booking: a small provider share (3–5%) and a seeker booking fee (tiered, as above), collected automatically when you sit in the money flow.

**How you set it up:** You must hold funds in escrow to capture this cleanly — seeker pays SpaceLinq, SpaceLinq releases to provider minus commission. In NZ that means a payment provider supporting marketplace/split payments and held balances (Stripe Connect is the common path; Windcave is the local option to price against). Your admin panel needs: a commission-rate table editable per tier, a promotional-override flag (set to 0% during the free window), a founding-member flag (locks a permanent discount), and an escrow/payout ledger.

**Admin levers:** tier thresholds, provider vs seeker split, promo overrides, founding-member rates, payout timing (holding funds longer improves your working capital and float).

### Layer 2 — Provider visibility & subscriptions

Once providers compete for seeker attention, visibility becomes sellable: featured listings, top-of-search placement, and provider subscription tiers (more listings, analytics, priority support). This is the first revenue you can charge *during* the free transaction window, because it's a provider choosing to pay for an edge — not a tax on the core service.

**How you set it up:** A listing-tier field on each provider account (Free / Professional / Enterprise), a featured-slot inventory system (how many featured slots per region/category, sold by day or month), and a billing system for recurring subscriptions separate from transaction escrow.

**Admin levers:** number of featured slots (scarcity = price), subscription tier pricing, which analytics sit behind the paid tier.

### Layer 3 — Embedded services margin (insurance, security, value-add)

You don't underwrite — you earn a margin reselling. Insurance, monitored security, and value-added services (kitting, labelling, compliance handling) each carry a 15–25% platform margin. Include a baseline free protection tier ($10–15k cover, funded from your commission) as a trust signal, then upsell.

**How you set it up:** Partner agreements first (an underwriter such as NZI/Vero for goods-in-storage cover; a monitoring provider for security), then an add-on selector at checkout that itemises each service and applies your margin. Your booking-detail page already has the add-on toggle pattern built — this extends it.

**Admin levers:** partner margin %, which services are bundled free vs paid, attach-rate targets.

### Layer 4 — Retail media network (data & advertising)

This is the "Retail Media Network for Logistics" idea, and it's the highest-margin layer. Sponsored search results, category banners, and — later — data insight products (anonymised demand/pricing trends sold back to providers and the wider industry). It only works at scale, because advertisers pay for audience.

**How you set it up:** An ad-serving slot system (sponsored results in search, banner inventory on category pages), a CPC/CPM billing model, and an advertiser self-serve console. Build this last among the "core" layers — it needs traffic to be worth anything.

**Admin levers:** CPC/CPM floor prices, ad inventory density (too many ads degrades the marketplace), keyword auction settings.

### Layer 5 — Next-generation platform fees (long horizon)

Energy trading commission, digital asset custody, circular-economy processing fees, EV charging. Each is its own mini-marketplace with its own take rate (e.g. 2–5% on energy transactions). These are real but should be treated as **future option value**, switched on facility-by-facility once a provider has the physical capability — not core to the rollout.

**Admin levers:** per-stream commission %, which facilities are enabled, partner integrations.

---

## The phased rollout

Each phase is gated by a liquidity milestone, with an approximate timing. Move when the milestone is hit, not just when the clock says so.

### Phase 0 — Acquisition (Months 0–6): everything free, but instrumented

**Milestone to exit:** ~50+ active providers in a region (start Auckland), seekers browsing, and a meaningful number of completed bookings.

Revenue switched on: **none from transactions.** Listings free, transactions free, search free. But you run the *full booking flow including escrow* from day one — you're just setting commission to 0%. This is critical: it trains both sides to transact *inside* the platform, so when fees turn on, the habit already exists and disintermediation is far harder.

What you're actually doing here is buying liquidity and collecting the proof you'll need later: every match made, dollar moved, day saved. Launch the **Founding Member Program** now — early providers lock a permanent reduced commission, which both accelerates sign-up and gives them a reason to stay when fees arrive.

You *can* quietly test Layer 2 (a paid featured listing) late in this phase with a handful of keen providers — optional, low-stakes, and it tells you willingness-to-pay before you commit.

### Phase 1 — Activation (Months 6–12): turn on the engine, gently

**Milestone to enter:** liquidity proven in your first region. **Milestone to exit:** transaction fees accepted with <15% churn, and a second region (Wellington/Christchurch) reaching liquidity.

Switch on **Layer 1** for new users first, grandfathering existing free users for an extra 3–6 months at a discount. Give 60–90 days' notice with a value report ("SpaceLinq connected you to X bookings worth $Y"). Roll out **Layer 2** properly — featured listings and provider subscriptions become a standing product. Introduce **Layer 3** insurance as an opt-in add-on with the free baseline tier live.

Watch churn obsessively in this phase. >15% immediate churn on the fee announcement means the rate is too high — adjust tiers rather than abandon the model.

### Phase 2 — Expansion (Months 12–24): layer the margins

**Milestone to enter:** transaction revenue stable and growing across two+ regions.

Scale **Layer 3** (security packages, value-added services attach at checkout). Stand up **Layer 4** — sponsored search and banners — now that traffic justifies advertiser spend. Begin the Australia groundwork using the proven NZ commission structure. This is where the blended revenue picture (commission + subscriptions + ads + add-ons) starts to compound.

### Phase 3 — Platform (Months 24+): optionality and moat

**Milestone to enter:** SpaceLinq is the default warehouse marketplace in NZ with Australia live.

Switch on **Layer 5** streams facility-by-facility as providers gain capability (energy, digital custody, circular economy). Launch data insight products off the Layer 4 base. These don't carry the rollout — they widen the moat and create the "innovation hub" story for investors and acquirers.

---

## What this builds toward

| Phase | Live revenue layers | Primary goal |
|---|---|---|
| 0 (0–6mo) | None (escrow live, 0% fee) | Liquidity + transaction habit |
| 1 (6–12mo) | 1, 2, basic 3 | Activate the engine, prove fee tolerance |
| 2 (12–24mo) | 1, 2, full 3, 4 | Compound margins, expand regions |
| 3 (24mo+) | All five | Moat, optionality, scale to AU |

The discipline that makes this work: **never introduce a layer that suppresses the layer beneath it.** Search stays free forever because it feeds everything. Transaction fees wait for liquidity. Ads wait for traffic. Each layer earns the right to exist by the success of the one below — which is exactly how you get rapid two-sided sign-up *and* a revenue base that grows with you instead of fighting you.

---

*Next practical step: confirm your payment/escrow provider (Stripe Connect vs Windcave for NZ), since Layer 1's entire setup hangs off being able to hold and split funds. Everything else can be built around that decision.*
