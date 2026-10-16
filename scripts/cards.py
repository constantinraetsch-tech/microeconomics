"""Microeconomics midterm decks for RECALL (recall-v1)."""
import json, os, shutil, zipfile

SUBJECT = "Microeconomics"
U1 = "Topic 1 – Introduction to Economics"
U2 = "Topic 2 – Market Analysis"
U3 = "Topic 3 – Market Interventions I"
U4 = "Exam Practice – Seminars & Past Midterms"
UNITS = [(U1, 1), (U2, 2), (U3, 3), (U4, 4)]

cards = []
def c(unit, section, cid, front, back, tags=(), img=None, explain=None, src=None):
    d = {"id": cid, "unit": unit, "section": section, "front": front, "back": back,
         "front_image": None, "back_image": f"images/{img}" if img else None,
         "tags": ["midterm", *tags], "source": src or {U1: "Topic 1 slides", U2: "Topic 2 slides", U3: "Topic 3 slides", U4: "Seminars / past midterms"}[unit]}
    if explain: d["explain"] = explain
    cards.append(d)

# ───────────────────────── TOPIC 1 ─────────────────────────
S = "01. The concept of Economics"
c(U1, S, "mi-t1-robbins", "How did **Lionel Robbins** (1932) define economics?",
  "The science that studies human behaviour as a relationship between **ends** and **scarce means** which have **alternative uses**.",
  explain="The key word is **scarcity**: we have unlimited wants but limited resources, so every use of a resource means giving up another use. That is why opportunity cost is at the heart of economics.")
c(U1, S, "mi-t1-smith", "How did **Adam Smith** describe economics?",
  "A study of mankind in the **ordinary business of life** – the part of action connected with the attainment and use of the **material requisites of well-being**.")
c(U1, S, "mi-t1-social-science", "Why is economics called a **social science**?",
  "It uses the **scientific method**: build **theories**, state **hypotheses**, test them with **empirical data** (hence statistics/data analytics matter).")
c(U1, S, "mi-t1-not-money", "Economics is not about money – what is it about, and which two criteria does it judge policies by?",
  "It is about **well-being**. Policies are judged by **efficiency** (best use of resources) and **equity** (fair distribution of income).")
c(U1, S, "mi-t1-correlation", "Golden rule when analysing economic data?",
  "**Correlation does not imply causality.**",
  explain="Example from Seminar 1: GDP per capita and primary school enrolment move together, but a scatterplot alone cannot prove that higher GDP *causes* higher enrolment. You need e.g. a natural experiment.")
c(U1, S, "mi-t1-disciplines", "Name connections between economics and other disciplines (slides).",
  "- **Psychology** → behavioural economics\n- **International relations**\n- **Law** → competition law\n- **Maths** → models to express theories")

S = "02. Micro vs Macro"
c(U1, S, "mi-t1-micro", "What does **microeconomics** analyse?",
  "**Specific markets**: market structures, incentive design, **consumer choice**, firms' **strategic decisions**.")
c(U1, S, "mi-t1-macro", "What does **macroeconomics** analyse?",
  "The whole economy: **economic growth**, **inflation**, **unemployment**, **inequality**, **fiscal** and **monetary policy**.")
c(U1, S, "mi-t1-micro-macro-link", "Are micro and macro independent?",
  "No – they are **linked**. Models of consumers' and firms' behaviour (micro) are the **base** for macro models; the fields differ in **focus**.")
c(U1, S, "mi-t1-econometrics", "What is **econometrics**?",
  "The application of **statistical methods** to economic analysis.")
c(U1, S, "mi-t1-micro-or-macro", "Micro or macro? (a) A €4 tariff – does the consumer price rise by €4 or less? (b) Do higher interest rates reduce inflation and growth?",
  "(a) **Micro** (one market, tax incidence). (b) **Macro** (monetary policy, aggregate inflation/growth).")

S = "03. Opportunity cost & PPF"
c(U1, S, "mi-t1-oc-def", "Define **opportunity cost**. (asked in BOTH past midterms)",
  "The **value of the next-best alternative** given up when a decision is made – **what we give up** by taking a certain decision.", tags=["past-exam"])
c(U1, S, "mi-t1-taxi", "Adam: taxi driver 2,000 h × €20; licence + car cost €100,000 (could earn **4%**); alternative job pays €37,000. Opportunity cost of being a taxi driver? Rational?",
  "OC = **€37,000** salary + **€4,000** interest = **€41,000**. Taxi earns **€40,000** < €41,000 → **not rational** (economic loss of €1,000).", tags=["calc"],
  explain="Opportunity cost includes *all* forgone alternatives: the best alternative salary AND the interest the €100,000 could have earned in the bank. If interest rates rise, the forgone interest rises, so becoming a taxi driver becomes **even less** attractive.")
c(U1, S, "mi-t1-taxi-interest", "In the taxi example, if interest rates **increase**, is Adam more or less likely to become a taxi driver?",
  "**Less likely** – the forgone interest on the €100,000 rises, so the **opportunity cost increases**.")
c(U1, S, "mi-t1-oc-college", "Youth unemployment falls and young unskilled wages rise. What happens to the opportunity cost of going to university? (Midterm 2023)",
  "It **increases**: lower unemployment → higher **expected wages without a degree** → more **forgone earnings** during the years at college.", tags=["past-exam"])
c(U1, S, "mi-t1-oc-tourism-education", "Paper: \"Tourism growth, education decline\" (China). Most likely explanation?",
  "Tourism creates jobs → **raises the opportunity cost of attending college** (forgone wages) → fewer students.")
c(U1, S, "mi-t1-oc-interest-realestate", "ECB raises interest rates. Effect on the opportunity cost of real-estate investors? (Midterm 2025 + Seminar 1)",
  "**Increases**: bonds/bank deposits become more attractive (higher forgone return) **and** borrowing costs rise.", tags=["past-exam"])
c(U1, S, "mi-t1-oc-lira", "Turkish lira depreciates vs the British pound. Effect on the opportunity cost of a British tourist going to **Spain**? (Midterm 2025)",
  "**Increases** – Turkey becomes cheaper, so the forgone alternative (holiday in Turkey) is more valuable → higher OC of visiting Spain.", tags=["past-exam"])
c(U1, S, "mi-t1-oc-wage-leisure", "Relationship between the hourly wage and time spent on leisure (opportunity cost view)?",
  "A higher wage **raises the opportunity cost of leisure** (each hour of leisure = more forgone income).")
c(U1, S, "mi-t1-ppf-def", "What does the **PPC/PPF** represent?",
  "The **maximum production** of two goods an economic system (country, firm…) can produce with its resources and technology.")
c(U1, S, "mi-t1-ppf-slope", "What does the **slope** of the PPF represent?",
  "The **opportunity cost**: how many units of the **vertical-axis** good we give up for **one more unit** of the **horizontal-axis** good.")
c(U1, S, "mi-t1-ppf-curved", "Why can a PPF be **curved (bowed out)**?",
  "**Increasing opportunity costs**: we start with the most efficient resources, so producing more of one good gets harder and harder.", tags=["mc"])
c(U1, S, "mi-t1-ppf-resources", "How do **more or fewer resources** show on the PPF? Do opportunity costs change?",
  "A **parallel shift** (out/in). OCs **do not change** (slope unchanged).",
  explain="Seminar 1, Q1d: the AI system loses 18 hours → frontier shifts inward in parallel from M + 4P = 40 to M + 4P = 34, OC(M) = 0.25P still.")
c(U1, S, "mi-t1-ppf-productivity", "How does a **productivity/technology change** in one good show on the PPF?",
  "The **slope changes** (the PPF pivots) → opportunity costs of **both** goods change.",
  explain="Seminar 1, Q1e: policy analysis now takes 9 h instead of 12. OC(P) falls from 4M to **3M**, and OC(M) rises from 0.25P to **1/3 P** – even though maths still takes 3 h. OCs are always reciprocals of each other.")
c(U1, S, "mi-t1-oc-reciprocal", "If the OC of 1 car = **6 motorbikes**, what is the OC of 1 motorbike?",
  "**1/6 car** – opportunity costs of the two goods are **reciprocals**.")
c(U1, S, "mi-t1-phones-laptops", "2,000 employees; each can make **20 phones or 4 laptops** a day. Max output and opportunity costs?",
  "Max **40,000 phones** or **8,000 laptops**. OC(phone) = **0.2 laptops**; OC(laptop) = **5 phones**.", tags=["calc"])

S = "03. Comparative advantage"
c(U1, S, "mi-t1-ca-def", "What is **comparative advantage**?",
  "Producing a good at a **lower opportunity cost** than others. Each country **specialises** in the good with the lower OC.")
c(U1, S, "mi-t1-ca-absolute", "Country A is better at producing **everything**. Can both A and B still gain from trade?",
  "**Yes** – as long as their **opportunity costs differ**, both gain by specialising according to **comparative** (not absolute) advantage.")
c(U1, S, "mi-t1-ca-price", "Where must the **international price** (terms of trade) lie for both countries to gain?",
  "**Between the two countries' opportunity costs.**")
c(U1, S, "mi-t1-ca-ab", "A: 1 labour unit → **5 laptops or 10 phones**; B: **1 laptop or 3 phones** (100 labour each). Who has the comparative advantage in what? Price range?",
  "OC(laptop): A = **2 phones**, B = **3 phones** → **A: laptops**, **B: phones**. Trade price: **2–3 phones per laptop**.", tags=["calc"],
  explain="A has an absolute advantage in both goods, but its OC of laptops is lower (2 < 3 phones), and B's OC of phones is lower (1/3 < 1/2 laptop). Merged country C: max 600 laptops or 1,300 phones; kink at (500 laptops, 300 phones) – A makes all laptops first.")
c(U1, S, "mi-t1-joint-ppf-rule", "How do you build a **joint PPF** of two producers?",
  "Start with **all output of one good**; switch to the other good first in the producer with the **lower opportunity cost** for it. Their full switch gives the **kink**; then the second producer switches.",
  img="joint-ppf.png", tags=["diagram"])

S = "04. Positive vs normative"
c(U1, S, "mi-t1-positive", "What is a **positive** statement?",
  "**Objective** – it can be **tested or verified** with data (may be true or false).")
c(U1, S, "mi-t1-normative", "What is a **normative** statement?",
  "Contains a **value judgement** (\"should\", \"better\", \"good for society\").")
c(U1, S, "mi-t1-pn-examples", "Positive or normative? (1) Minimum wages are associated with higher youth unemployment. (2) Progressive taxes are better than proportional. (3) More inequality is associated with higher crime.",
  "(1) **Positive** (2) **Normative** (3) **Positive**")
c(U1, S, "mi-t1-pn-inflation", "\"Inflation has reached a 20-year record. Lowering taxes is the best option to fight inflation.\" Positive or normative? (Midterm 2023)",
  "First part **positive** (verifiable). \"Best option\" = value judgement → the statement is **normative**.", tags=["past-exam"])
c(U1, S, "mi-t1-natural-exp", "What is a **natural experiment**, and what does it require?",
  "An event that splits people into **treatment** and **control groups** that are **comparable in all relevant characteristics** except exposure to the event.", tags=["mc"],
  explain="Classic slide example: **Card & Krueger** (Nobel 2021 with Angrist & Imbens). New Jersey raised its minimum wage in 1992 ($4.25 → $5.05); neighbouring eastern Pennsylvania did not. Fast-food employment in NJ did **not** fall.")
c(U1, S, "mi-t1-card-krueger", "What did **Card & Krueger** find about the New Jersey minimum wage increase?",
  "Comparing NJ (treatment) with eastern **Pennsylvania** (control): **employment was not affected** despite the higher minimum wage.")

S = "05. Market structures"
c(U1, S, "mi-t1-structures-order", "Order the four market structures from **least to most market power**.",
  "**Perfect competition** → **monopolistic competition** → **oligopoly** → **monopoly**.")
c(U1, S, "mi-t1-pc-structure", "Perfect competition: number of sellers, product, control over price, entry?",
  "**Very large** number · **standardized** product · **no** control over price · **no barriers**.")
c(U1, S, "mi-t1-mc-structure", "Monopolistic competition: number of sellers, product, control over price, entry?",
  "**Many** sellers · **differentiated** product · **slight** control over price · **no barriers** (→ long-run entry pushes profits down).", tags=["mc"])
c(U1, S, "mi-t1-oligo-structure", "Oligopoly: number of sellers, product, control over price, entry?",
  "**Few / two** sellers · **standardized or differentiated** · **considerable** control over price · **large barriers**.")
c(U1, S, "mi-t1-mono-structure", "Monopoly: number of sellers, product, control over price, entry?",
  "**One** seller · **unique** product · **huge** control over price (if not regulated) · **very large barriers**.")
c(U1, S, "mi-t1-chora", "4 hotels on a Greek island, differing in rating, beach distance and price. Market structure? Product type? (Seminar 1)",
  "**Oligopoly** (only 4 firms, strategic interdependence, high HHI) selling a **differentiated** product (rating, location, quality differ).")

S = "06. Market concentration (HHI)"
c(U1, S, "mi-t1-hhi-def", "Define the **Herfindahl-Hirschman Index** and give its formula.",
  "A measure of **market concentration**: **HHI = Σ sᵢ²** – the sum of the **squared market shares** (in %) of all firms.", tags=["past-exam"])
c(U1, S, "mi-t1-hhi-range", "Range of the HHI in general?",
  "From **close to 0** (many tiny firms) to **10,000** (monopoly: 100²).")
c(U1, S, "mi-t1-hhi-min-n", "Minimum HHI with **n** firms? Give values for 3 and 4 firms.",
  "Minimum when shares are **equal**: **10,000 / n**. 3 firms → **3,333.3**; 4 firms → **2,500**.", tags=["past-exam", "calc"],
  explain="With 4 firms with positive shares the HHI ranges from 2,500 (25% each) to values arbitrarily close to, **but below**, 10,000 (it can never reach 10,000 while all four have a positive share).")
c(U1, S, "mi-t1-hhi-negative", "What is the negative impact of a **higher HHI**?",
  "Higher concentration → **less competition** → **collusion more likely** → **lower output** and **higher prices** (more market power).", tags=["past-exam"])
c(U1, S, "mi-t1-hhi-market1", "Shares 40, 20, 18, 12, 10. HHI? New HHI if C, D and E merge?",
  "HHI = 1,600 + 400 + 324 + 144 + 100 = **2,568**. After merger (40, 20, 40): **3,600**.", tags=["calc"])
c(U1, S, "mi-t1-hhi-france-italy", "France: 80/15/5. Italy: two firms, one with 55%. Which is more concentrated? (Midterm 2023)",
  "France = 6,400 + 225 + 25 = **6,650**; Italy = 55² + 45² = **5,050** → **France** is more concentrated.", tags=["past-exam", "calc"])
c(U1, S, "mi-t1-hhi-eu", "EU merger guidelines: when is the Commission unlikely to see competition concerns?",
  "Post-merger HHI **< 1,000**; HHI **1,000–2,000** with Δ **< 250**; HHI **> 2,000** with Δ **< 150**.")

S = "07. Perfect competition & information"
c(U1, S, "mi-t1-pc-conditions", "The **four conditions** of perfect competition?",
  "1. **Many sellers** of an **identical product**\n2. **Many buyers**\n3. **Symmetric and complete information**\n4. **Free entry and exit**")
c(U1, S, "mi-t1-price-takers", "Why are firms **price-takers** in perfect competition?",
  "**Identical product** → consumers buy the cheapest, so all sell at **one market price**; and **no firm is large enough** to lead the price.")
c(U1, S, "mi-t1-zero-profit", "What profit do firms make in the **long run** under perfect competition, and why?",
  "**Zero economic profit** – they earn their **opportunity cost**. Profits attract **entry**; losses cause **exit**.")
c(U1, S, "mi-t1-asym-examples", "Give two examples of **asymmetric information** from the slides.",
  "Job **candidates** know more about their skills than **employers**; **manufacturers** know more about quality than **consumers**.")
c(U1, S, "mi-t1-lemons", "What is **Akerlof's \"Market for Lemons\"** (1970) about?",
  "**Adverse selection**: sellers know quality, buyers don't → buyers' **WTP falls** → **good-quality sellers leave** → market share of bad quality rises (market may **collapse**).",
  explain="Used-car market: a 'lemon' is a defective car. Because buyers can't tell good from bad cars, they only pay an average price; owners of good cars won't sell at that price, so the average quality falls further. Nobel 2001.")
c(U1, S, "mi-t1-reduce-asym", "How can asymmetric information be reduced? (slides)",
  "**Ratings and reviews** (e.g. booking platforms, Michelin stars), certifications, guarantees – signals of quality.")

# ───────────────────────── TOPIC 2 ─────────────────────────
S = "01. Demand, supply, equilibrium"
c(U2, S, "mi-t2-law-demand", "State the **law of demand** and the **law of supply**.",
  "Demand: price ↑ → **quantity demanded ↓** (negative slope). Supply: price ↑ → **quantity supplied ↑** (positive slope).")
c(U2, S, "mi-t2-equilibrium", "What is **market equilibrium** and how do you find it from equations?",
  "Where **Qd = Qs**. Set the two equations equal, solve for **p\\***, then plug p\\* into either equation for **Q\\***.", tags=["calc"])
c(U2, S, "mi-t2-ped-shift-supply", "Demand shifts right. When is the **price** effect big and when is the **quantity** effect big?",
  "Depends on supply responsiveness: **inelastic supply** → mostly **price ↑**; **elastic supply** → mostly **quantity ↑**.")
c(U2, S, "mi-t2-supply-shift-demand", "Supply shifts. What determines whether price or quantity changes more?",
  "**Demand elasticity**: inelastic demand → big **price** change; elastic demand → big **quantity** change.")

S = "02. Demand and its drivers"
c(U2, S, "mi-t2-demand-function", "Write the general demand function and list its drivers.",
  "**Qd = f(P, P_subst, P_compl, income, tastes…)** – own price, price of **substitutes**, price of **complements**, **income**, **preferences**.")
c(U2, S, "mi-t2-move-vs-shift", "Movement **along** the demand curve vs **shift** of the curve?",
  "Change in **price (variable)** → movement **along** (change in quantity demanded). Change in a **parameter** (income, preferences, related prices) → **shift** of the whole curve (change in demand).")
c(U2, S, "mi-t2-substitute", "Price of a **substitute** rises (Pepsi ↑). Effect on demand for Coke?",
  "Demand for Coke **increases** (shifts right).")
c(U2, S, "mi-t2-complement", "Price of a **complement** rises (flights BCN–NY ↑). Effect on hotel rooms in NY?",
  "Demand for hotel rooms **decreases** (shifts left).")
c(U2, S, "mi-t2-normal-inferior", "Income rises. Effect on a **normal** vs an **inferior** good?",
  "Normal good: demand **↑**. Inferior good: demand **↓**.",
  explain="Slide study: fast-food restaurants were *normal* goods for below-average incomes but *inferior* for above-average incomes; full-service restaurants were normal at virtually all income levels.")
c(U2, S, "mi-t2-demand-increase", "List what causes an **increase in demand** (shift right).",
  "- Income ↑ (normal) / income ↓ (inferior)\n- Price of **substitute ↑**\n- Price of **complement ↓**\n- Preferences ↑\n- More **population** interested")
c(U2, S, "mi-t2-utility", "What does the **utility function** measure?",
  "How consumers **feel** (satisfaction) given a certain **basket of products**. Demand depends on preferences and **budget constraints** (time/money).")
c(U2, S, "mi-t2-giffen", "What is a **Giffen good**? Example?",
  "A good whose demand **rises when its price rises** (violates the law of demand) – the income effect dominates. Example: **potatoes in 19th-century Ireland**.")
c(U2, S, "mi-t2-market-demand", "How do you get **market demand** from individual demands?",
  "**Horizontal sum**: at each price, **add the quantities** (× number of consumers). Only add groups whose quantity is ≥ 0 → kinked demand.", tags=["calc"],
  explain="Seminar 2 Q5: 50 business travellers Qd = 100 − 4p and 100 leisure travellers Qd = 100 − 2p.\n- p ≤ 25: Q = 5,000 − 200p + 10,000 − 200p = **15,000 − 400p**\n- 25 < p ≤ 50: only leisure → **Q = 10,000 − 200p**\n- p > 50: Q = 0. Kink at (5,000, 25).")

S = "03. Supply and its drivers"
c(U2, S, "mi-t2-supply-drivers", "What does quantity supplied depend on?",
  "**Technology/productivity**, **number of firms**, **own price**, **price of related products** (that the firm could switch to), **cost structure** (marginal costs).")
c(U2, S, "mi-t2-fixed-cost", "Do **fixed costs** affect the supply curve?",
  "**No** – only **marginal (variable) costs** affect supply. A fixed cost has no consequence on supply.")
c(U2, S, "mi-t2-min-price-unit", "TFC = €200; TVC = 50, 110, 200 for Q = 1, 2, 3. Minimum price to sell each additional unit?",
  "MC = **€50, €60, €90**. The minimum price for an extra unit = its **marginal cost** (not average total cost – profit is a different question).", tags=["calc"])
c(U2, S, "mi-t2-supply-shift", "List what **increases supply** (shift right) and what **decreases** it.",
  "Increase: **more firms**, **productivity ↑**, **wages ↓**, other variable costs ↓, **technological change**.\nDecrease: fewer firms, **wages ↑**, variable costs ↑, **shortage of production factors**.")
c(U2, S, "mi-t2-linear-supply", "Linear supply Qs = β₀ + βₓPₓ + β_W·W + β_r·P_r: expected signs?",
  "**βₓ > 0** (law of supply); **β_W < 0** (input price ↑ → supply ↓); **β_r > 0** for complements in production.")

S = "Market dynamics (shifts)"
c(U2, S, "mi-t2-double-shift-rule", "Both curves shift at once. What can you say?",
  "Only **one** variable is certain; the other is **ambiguous (?)** – it depends on which shift is larger.\n- D↑ S↑ → **Q↑, P?**\n- D↑ S↓ → **P↑, Q?**\n- D↓ S↑ → **P↓, Q?**\n- D↓ S↓ → **Q↓, P?**",
  img="double-shifts.png", tags=["diagram"])
c(U2, S, "mi-t2-consulting-ai", "AI raises consulting productivity; fear of recession makes clients reluctant to start projects. New equilibrium? (Midterm 2025)",
  "Supply **↑** (right) and demand **↓** (left) → **P ↓**, **Q uncertain**.", tags=["past-exam", "diagram"])
c(U2, S, "mi-t2-mallorca", "Mallorca clubs: tourists spend more on hotels (less on nightlife) + rising operational costs. Effect? (Midterm 2025)",
  "Demand **↓** and supply **↓** → **Q ↓**, **price uncertain**.", tags=["past-exam", "diagram"])
c(U2, S, "mi-t2-opec", "Oil: demand keeps growing + Saudi Arabia cuts production. Effect? (Midterm 2023)",
  "Demand **↑** and supply **↓** → **P ↑**, **Q uncertain**.", tags=["past-exam", "diagram"])
c(U2, S, "mi-t2-banksy", "Rumour that Banksy will retire; number of works fixed in the short run. Effect?",
  "Demand **↑** with **vertical (perfectly inelastic) supply** → **P ↑, Q unchanged**.", tags=["diagram"])
c(U2, S, "mi-t2-nyc-hotels", "NYC heavily restricts short-term rentals. Effect on the hotel market? With fixed capacity of 120,000 rooms?",
  "Short-term rentals are **substitutes** → hotel demand **↑** → **P ↑, Q ↑**. With capacity reached, supply becomes **vertical** → P ↑, Q ↑ **at most 120,000**.", tags=["diagram"])
c(U2, S, "mi-t2-turkey", "Lira loses 18% vs the euro. Turkish tourism market (prices in lira)?",
  "Turkey becomes cheaper for foreigners → **demand ↑** → **P (in TRY) ↑, Q ↑**.", tags=["diagram"])
c(U2, S, "mi-t2-maple", "50% US tariff on Canadian maple syrup + US consumers boycott Canadian products?",
  "Supply **↓** (tariff) and demand **↓** → **Q ↓, P ?**", tags=["diagram"])
c(U2, S, "mi-t2-london-housing", "London: public land for new flats + higher variable mortgage rates?",
  "Supply **↑** and demand **↓** → **P ↓, Q ?**", tags=["diagram"])

S = "04. Elasticities"
c(U2, S, "mi-t2-elasticity-def", "What does **elasticity** measure? Name the three demand elasticities.",
  "How **sensitive** quantity demanded is to a change in a variable: **price elasticity (PED)**, **cross-price elasticity (XED)**, **income elasticity (YED)**.")
c(U2, S, "mi-t2-ped-formula", "Formula for the **price elasticity of demand**?",
  "**ε = %ΔQ / %ΔP = (ΔQ/Q₀)/(ΔP/P₀) = (ΔQ/ΔP)·(P₀/Q₀)**; point form **ε = Q'(p)·p/Q(p)**. Use **initial values** for the %.", tags=["calc"])
c(U2, S, "mi-t2-ped-sign", "What sign does PED have?",
  "**Negative** (law of demand), except when it is **zero**.")
c(U2, S, "mi-t2-ped-ranges", "Value ranges: elastic, unit, inelastic, perfectly inelastic, perfectly elastic.",
  "- **−∞ < ε < −1**: elastic\n- **ε = −1**: unit elastic\n- **−1 < ε < 0**: inelastic\n- **ε = 0**: perfectly inelastic (vertical D)\n- **ε = −∞**: perfectly elastic (horizontal D)")
c(U2, S, "mi-t2-slope-vs-ped", "Is the slope of a linear demand the same as its PED?",
  "**No.** Slope is **constant**, but PED **changes along the line**: **elastic at high prices** (small Q → big % changes), **inelastic at low prices**.",
  img="linear-demand-elasticity.png", tags=["past-exam", "diagram"],
  explain="ε = (dQ/dp)·(p/Q). dQ/dp is constant, but p/Q rises as price rises (p up, Q down). So demand becomes **more elastic as price increases**.")
c(U2, S, "mi-t2-ped-linear-formula", "For linear demand **Q = a − bp**, what is the PED and the revenue-maximising price?",
  "**ε = −bp/(a − bp)**. Revenue is max where **ε = −1** → **p = a/(2b)** (the midpoint).", tags=["calc", "past-exam"])
c(U2, S, "mi-t2-tr-test", "Total revenue test: price ↑ with **inelastic** vs **elastic** demand?",
  "Inelastic: price ↑ → **revenue ↑** (price ↓ → revenue ↓).\nElastic: price ↑ → **revenue ↓** (price ↓ → revenue ↑).\nUnit elastic: revenue **unchanged**.",
  img="revenue-rectangles.png", tags=["diagram"])
c(U2, S, "mi-t2-revenue-elastic-drop", "Explain with a diagram: prices drop in a market with **very elastic** demand. (Midterm 2025)",
  "Revenue **rises**: the loss rectangle (**ΔP × Q₁**) is smaller than the gain rectangle (**P₂ × ΔQ**) because Q rises by a larger %.", img="revenue-rectangles.png", tags=["past-exam", "diagram"])
c(U2, S, "mi-t2-max-rev-vs-profit", "Is maximum revenue the same as maximum profit?",
  "**No** – maximum revenue is at **ε = −1**; profit also needs the **cost structure**.")
c(U2, S, "mi-t2-ped-determinants", "Five determinants of PED (slides)?",
  "1. **Time**: more elastic in the **long run**\n2. **Necessity**: basic goods (food, housing, electricity) inelastic\n3. **Number of substitutes**: few → inelastic\n4. **Addictiveness**: alcohol, cigarettes, drugs inelastic\n5. **Share of budget**: big share → more elastic")
c(U2, S, "mi-t2-marijuana", "PED of marijuana ≈ −0.7. Is a tax that raises the price a good way to cut consumption?",
  "Demand is **inelastic** → a tax reduces quantity **only a little** (but raises a lot of tax revenue).")
c(U2, S, "mi-t2-ped-income", "Relationship between PED and income? (drug-price slide)",
  "**Lower income/education → more price-sensitive** (more elastic) – relevant for **social justice** of price policies.")
c(U2, S, "mi-t2-yed-def", "Define **income elasticity**; classify normal (luxury/necessity) and inferior goods.",
  "**ε_R = %ΔQ / %ΔIncome**. **> 1** luxury · **0–1** necessity (both **normal**, > 0) · **< 0** **inferior**.")
c(U2, S, "mi-t2-engel", "What is the **Engel curve**?",
  "Shows **quantity demanded** (horizontal axis) against **income** (vertical axis); bends backwards where the good becomes **inferior**.")
c(U2, S, "mi-t2-xed-def", "Define **cross-price elasticity**; what do its signs mean?",
  "**ε_XY = %ΔQ_X / %ΔP_Y**. **Positive** → **substitutes**; **negative** → **complements**. Close to 0 → weakly related.")
c(U2, S, "mi-t2-pes", "Define the **price elasticity of supply**. Sign?",
  "**ε_S = %ΔQs / %ΔP** – **positive** (upward-sloping supply); **0** if supply is perfectly inelastic (vertical).")

S = "05. Welfare analysis"
c(U2, S, "mi-t2-cs-def", "What is **consumer surplus**?",
  "Sum of **WTP − price** over all units bought; graphically the area **below demand and above the price**.", img="surplus-basic.png", tags=["diagram"])
c(U2, S, "mi-t2-ps-def", "What is **producer surplus**? Is it equal to profit?",
  "Sum of **P − MC** over all units sold = **revenues − variable costs**; area **above supply, below price**. **Not profit** (fixed costs excluded).")
c(U2, S, "mi-t2-cs-table", "WTP per unit: 15, 10, 8, 5, 3; price €6. Consumer surplus?",
  "Buys 3 units: (15−6) + (10−6) + (8−6) = **€15**.", tags=["calc"])
c(U2, S, "mi-t2-ps-table", "Price €12; MC per unit: 4, 7, 10, 13, 16. Producer surplus?",
  "Sells 3 units: 8 + 5 + 2 = **€15** (units 4–5 have MC > P).", tags=["calc"])
c(U2, S, "mi-t2-demand-wtp", "Why can the demand curve be read as **WTP**?",
  "Each point = WTP for that unit; **marginal utility decreases** as consumption increases → downward slope.")
c(U2, S, "mi-t2-welfare-purpose", "Purpose of welfare analysis?",
  "Measure the welfare of each stakeholder (**CS, PS**) to compare two market situations: **who wins, who loses**, and whether **total welfare** rises or falls (taxes, price controls…).")

# ───────────────────────── TOPIC 3 ─────────────────────────
S = "Intro: interventions & efficiency"
c(U3, S, "mi-t3-types", "List the types of government market intervention.",
  "**Maximum price** (ceiling), **minimum price** (floor), **production quotas**, **indirect taxes & subsidies**, **tariffs**, **import quotas** (+ regulation, public ownership).")
c(U3, S, "mi-t3-efficient", "What is an **efficient allocation** of resources?",
  "Resources in their **most efficient use**, all markets in **equilibrium (S = D)**, economy **on its PPC**, impossible to make someone better off without making someone worse off (**welfare maximised**).")
c(U3, S, "mi-t3-efficiency-conditions", "Market conditions required for efficiency?",
  "**Perfect competition**, **perfect information**, **perfect mobility**, **consumer sovereignty**, **no externalities or public goods** – plus clear **price signals**.")
c(U3, S, "mi-t3-gov-functions", "The **four functions** of government?",
  "1. **Legislative/regulatory** (legal framework, competition, externalities)\n2. **Allocative**\n3. **Distributive** (equity)\n4. **Stabilization**")

S = "Externalities"
c(U3, S, "mi-t3-ext-def", "Define an **externality**.",
  "When buying/selling decisions cause an **additional (external) cost or benefit on third parties**. **Social = private + external** costs/benefits.")
c(U3, S, "mi-t3-ext-types", "Give an example of each: +/− externality in production and consumption.",
  "+ production: **R&D** · − production: **nuclear energy/pollution** · + consumption: **culture, education** · − consumption: **alcohol, drugs**.")
c(U3, S, "mi-t3-ext-problem", "Why is the free market inefficient with externalities?",
  "Agents **ignore external costs/benefits** → **too many** transactions with **negative** externalities, **too few** with **positive** ones.")
c(U3, S, "mi-t3-battery", "Battery: Anna's WTP €5, Berta's cost €4, price €4.5, external cost €2. Should society allow the trade?",
  "Private surplus = **€1** < external cost **€2** → **inefficient**. Society could pay each **€0.75** not to trade and everyone is better off.", tags=["calc"])
c(U3, S, "mi-t3-first-aid", "First-aid course: Roger's WTP €100, cost €120, price €125, social benefit €30. Efficient?",
  "Total value 100 + 30 = **130 > 120** cost → he **should** attend; market fails (positive externality). E.g. Roger pays €98, society €27.", tags=["calc"])

S = "Maximum price (ceiling)"
c(U3, S, "mi-t3-ceiling-binding", "When is a **price ceiling** binding and what happens?",
  "Only if set **below equilibrium** → **Qd > Qs** → **shortage (excess demand)**; quantity traded = **Qs**.", img="price-ceiling.png", tags=["diagram"])
c(U3, S, "mi-t3-ceiling-consumers", "Are consumers better off with a ceiling?",
  "**Ambiguous**: + they pay a **lower price**, − **less quantity** is available. The **more elastic supply**, the worse for consumers.", tags=["past-exam"])
c(U3, S, "mi-t3-ceiling-producers", "Effect of a ceiling on producers?",
  "**Worse off**: lower price **and** lower quantity → industry less profitable → **less investment**.")
c(U3, S, "mi-t3-ceiling-elastic", "Is a price ceiling more likely to benefit consumers when supply is **elastic or inelastic**? (Midterm 2023)",
  "**Inelastic** supply – Qs falls **less**, so the quantity loss is small and the lower price dominates.", tags=["past-exam"])
c(U3, S, "mi-t3-rent-control", "Rent control: pros and cons?",
  "Pros: limits price of a **basic good**, more **affordable**. Cons: **lower supply**, **black markets**, **lower quality** of dwellings, less mobility, discrimination.",
  explain="Slides: Kholodilin review of 196 studies → mostly negative effects. Catalonia study (Jofre-Monseny et al.): rents fell **4–6%** with **no evidence of reduced supply** – so evidence is mixed.")
c(U3, S, "mi-t3-black-market", "Why can a **black market** emerge under a ceiling?",
  "At the restricted quantity Qs, the **marginal WTP is far above** the legal price → buyers would pay more illegally.")
c(U3, S, "mi-t3-ceiling-examples", "Real examples of maximum prices from the slides?",
  "**Energy** (Ofgem cap, Spanish gas cap), **payday loans** (UK FCA: 0.8%/day), **rent controls**, **surgical masks** (Spain, €0.60).")

S = "Minimum price (floor)"
c(U3, S, "mi-t3-floor-binding", "When is a **price floor** binding and what happens?",
  "Set **above equilibrium** → **Qs > Qd** → **excess supply (surplus)**; quantity traded = **Qd**. Sellers want to discount → hard to maintain.", img="price-floor.png", tags=["diagram"])
c(U3, S, "mi-t3-floor-welfare", "Who wins and loses with a price floor?",
  "Consumers **worse off** (pay more, buy less). Producers **ambiguous** – higher price but sell less; depends on **price elasticity of demand**.")
c(U3, S, "mi-t3-guaranteed", "What is a **guaranteed minimum price**? Problems?",
  "Government **buys the excess supply**. Producers clearly better off, but **expensive**, high **welfare loss**, **perverse incentives** to overproduce, and what to do with the stock (old EU CAP).")
c(U3, S, "mi-t3-floor-examples", "Examples of minimum prices?",
  "**Agriculture** (EU, India), **alcohol** (Scotland, Ireland), **carbon allowances**, and the **minimum wage**.")
c(U3, S, "mi-t3-minwage-effects", "Minimum wage: pros and cons?",
  "Pros: minimum income for **low-skilled**, more **equal** distribution, less **poverty**. Cons: higher labour cost → **unemployment** for some groups, firms substitute **capital** or **relocate**.")
c(U3, S, "mi-t3-minwage-diagram", "Minimum wage diagram: job destruction vs unemployment?",
  "**Job destruction** = Le − Ld (fall in employment). **Unemployment** = Ls − Ld (willing workers without jobs).", img="minimum-wage.png", tags=["diagram", "past-exam"])
c(U3, S, "mi-t3-minwage-elasticity", "Which elasticity limits **job destruction**? Which affects **unemployment**? (both midterms)",
  "**Inelastic labour demand** → little job destruction. Unemployment is larger the **more elastic** labour **demand and supply**.", tags=["past-exam"])
c(U3, S, "mi-t3-kaitz", "What is the **Kaitz index**?",
  "**Minimum wage / median (or average) wage × 100** – how 'high' a minimum wage is. Spain study: hit youth **16–19** most.")

S = "Production quotas"
c(U3, S, "mi-t3-quota-def", "What is a **production quota** and when does it bind?",
  "A **maximum quantity** that can be produced; binding only if set **below equilibrium Q**.", img="production-quota.png", tags=["diagram"])
c(U3, S, "mi-t3-quota-effects", "Effects of a production quota?",
  "Less exchanged + **higher price** → consumers **harmed**. Producers **indeterminate** (higher price, sell less). There is a **deadweight loss**.")
c(U3, S, "mi-t3-quota-elasticity", "When are producers better off under a quota?",
  "When demand is **inelastic** – the price rises a lot for a small cut in quantity, so revenue/PS rises.")
c(U3, S, "mi-t3-quota-examples", "Real examples of production quotas?",
  "**OPEC+** oil production cuts; **China rare-earth** quotas; EU agricultural quotas.")
c(U3, S, "mi-t3-summary", "Summary: aim and main problem of each price control?",
  "**Max price** favours consumers → problem: **shortage, black market, low quality**. **Min price** favours producers → **overproduction, cost**. **Guaranteed min price** → **expensive, perverse incentives**.")

# ───────────────────────── EXAM PRACTICE ─────────────────────────
S = "Seminar 1 – PPF & HHI"
c(U4, S, "mi-ex-hal-ppf", "HAL26: maths problem = 3 h, policy analysis = 12 h; 5 days 24/7. PPF?",
  "Hours = 5 × 24 = **120** → **3M + 12P = 120** → **M + 4P = 40**; intercepts **M = 40**, **P = 10**; **P = 10 − 0.25M**.", tags=["calc"])
c(U4, S, "mi-ex-hal-7", "HAL26 analyses 7 policies. How many maths problems?",
  "7 × 12 = 84 h → 36 h left → 36/3 = **12** problems.", tags=["calc"])
c(U4, S, "mi-ex-hal-oc", "HAL26 opportunity costs?",
  "OC(M) = 3/12 = **0.25 P**; OC(P) = 12/3 = **4 M**.", tags=["calc"])
c(U4, S, "mi-ex-factories", "Navojoa: 600 bars or 200 cups; Eldorado: 400 bars or 100 cups. OCs and comparative advantage?",
  "Navojoa: bar = **1/3 cup**, cup = **3 bars**. Eldorado: bar = **1/4 cup**, cup = **4 bars**. → **Eldorado: bars**; **Navojoa: ice cream**.", tags=["calc"])
c(U4, S, "mi-ex-factories-joint", "Joint company PPF (bars horizontal)?",
  "Start (0, 300). Eldorado switches to bars first → kink **(400, 200)** → end **(1,000, 0)**. I = 300 − B/4 (0–400), I = 200 − (B − 400)/3 (400–1,000).",
  img="joint-ppf.png", tags=["calc", "diagram"])
c(U4, S, "mi-ex-chora-hhi", "Chora hotels revenues: A €3.6m, B €4.5m, C €3.0m, D €2.0m. HHI? After B + C merge?",
  "Shares 27.48 / 34.35 / 22.90 / 15.27 → **HHI ≈ 2,693**. After merger (57.25%) → **≈ 4,266** (+1,573).", tags=["calc"])
c(U4, S, "mi-ex-motorbikes", "OC of 1 car = 6 motorbikes; max 120 motorbikes. Producing 48 motorbikes, how many cars?",
  "120 − 48 = 72 bikes' worth of resources → 72/6 = **12 cars**.", tags=["calc"])
c(U4, S, "mi-ex-emails", "Worker A: 20 emails or 5 memos per hour. Worker B's OC of an email = 0.4 memos. Who has the CA in emails?",
  "A's OC of an email = 5/20 = **0.25 memos** < 0.4 → **A** in emails (B in memos).", tags=["calc"])
c(U4, S, "mi-ex-daniela-sarah", "Daniela: 60 trousers/day, OC of trouser = 4 shirts. Sarah: 8 h × (10 trousers or 20 shirts). Joint PPF (trousers vertical)? (Midterm 2023)",
  "Daniela: 60 T or **240 S**; Sarah: **80 T** or **160 S**. Max **140 T**, **400 S**. Kink at **(240 shirts, 80 trousers)** – Daniela makes shirts first (OC of shirt 0.25 T < 0.5 T).", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-bulgaria", "Bulgaria: 1,000 resources × (10 cars or 5 trucks); Romania: 800 × (18 cars or 6 trucks). Comparative advantage? Joint PPC (cars vertical)? (Midterm 2025)",
  "OC(truck): BG = **2 cars**, RO = **3 cars** → **BG: trucks**, **RO: cars**. Max cars **24,400**, trucks **9,800**; kink at **(5,000 trucks, 14,400 cars)**.", tags=["calc", "past-exam"])

S = "Seminar 2 – Elasticity"
c(U4, S, "mi-ex-restaurant", "Restaurant: €120 → €150, customers 200 → 180. PED? Good for revenue?",
  "%ΔP = +25%, %ΔQ = −10% → **ε = −0.4** (inelastic). Revenue **€24,000 → €27,000** (+12.5%) → yes.", tags=["calc"])
c(U4, S, "mi-ex-negro-rojo", "Club: 120 people at €40, capacity 150, PED = −1.2. Price cut needed to fill it?",
  "%ΔQ = +25% → %ΔP = 25/(−1.2) = **−20.83%** → cut **€8.33** → new fee **€31.67**.", tags=["calc"])
c(U4, S, "mi-ex-linear-200", "Q = 200 − 4p: PED from €20→€25 and from €40→€45?",
  "20→25: Q 120→100 → −16.67%/25% = **−0.667** (inelastic). 40→45: Q 40→20 → −50%/12.5% = **−4** (elastic).", tags=["calc"])
c(U4, S, "mi-ex-kentucky", "Kentucky: PED(F&V) = −0.6; XED(fast food, P_F&V) = +0.05; subsidy cuts F&V price 10%. Effects?",
  "F&V: (−0.6)(−10%) = **+6%**. Fast food: (+0.05)(−10%) = **−0.5%**.", tags=["calc"])
c(U4, S, "mi-ex-montana", "Montana: PED(F&V) = −0.7, XED(F&V, P_FF) = +0.15; F&V price −10%. Fast-food price rise needed for +12% F&V?",
  "Own effect +7% → need +5% more → 5/0.15 = **+33.33%** fast-food price.", tags=["calc"])
c(U4, S, "mi-ex-subsidy-elastic", "Same subsidy in two states; demand more elastic in Montana. Compare.",
  "Supply shifts right in both: Montana (elastic D) → **bigger Q ↑, smaller P ↓**; Kentucky (inelastic D) → bigger P ↓, smaller Q ↑.")
c(U4, S, "mi-ex-coke", "PED of Coke = −0.5; 200 cokes/day at €3 → €3.5. New revenue? (Midterm 2025)",
  "%ΔP = +16.67% → %ΔQ = **−8.33%** → Q ≈ **183** → revenue 3.5 × 183 = **€640.5** (was €600).", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-rev-minus2", "Price +10% leads to revenue −2%. PED? (Midterm 2025)",
  "0.98 = 1.1 × Q₂/Q₁ → Q₂/Q₁ = 0.891 → %ΔQ = **−10.91%** → **ε = −1.09** (≈ −1.1).", tags=["calc", "past-exam"],
  explain="Trick: revenue = P × Q, so (1 + %ΔR) = (1 + %ΔP)(1 + %ΔQ). Solve for %ΔQ, then divide by %ΔP.")
c(U4, S, "mi-ex-500-5p", "Q = 500 − 5p: revenue-maximising price? (Midterm 2023)",
  "ε = −5p/(500 − 5p) = −1 → 10p = 500 → **p = 50** (= a/2b).", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-minus25", "PED = −2.5; 300 sales at €20; new price €10. Daily revenue? (Midterm 2023)",
  "%ΔP = −50% → %ΔQ = **+125%** → Q = **675** → revenue **€6,750** (was €6,000).", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-norway", "PED(EV) = −0.97; XED(EV, P_gasoline) = 0.36. Gasoline cars −10%, EV price +20%. ΔQ of EVs? (Midterm 2023)",
  "Cross: 0.36 × (−10%) = −3.6%. Own: −0.97 × 20% = −19.4%. Total **−23%**.", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-pes", "At equilibrium p = €20, Q = 500, PED = −1.5. Qd rises 30%. Price change? PES if excess demand = 250? (Midterm 2023)",
  "%ΔP = 30/(−1.5) = **−20%**. Qd = 650 → Qs = 400 → %ΔQs = −20% → **PES = +1**.", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-oil-rev", "Oil PED = −0.6, price +10%. % change in revenue? (Midterm 2023)",
  "%ΔQ = −6% → 1.1 × 0.94 = 1.034 → revenue **+3.4%**.", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-ev-car", "EV PED = −0.6; price €45,000, 2,000 units/month; price +€2,000. Revenue change?",
  "%ΔP = +4.44% → %ΔQ = −2.67% → Q ≈ 1,946.7 → revenue **€90.0m → €91.49m** (+€1.49m, +1.66%).", tags=["calc"])
c(U4, S, "mi-ex-discount", "PED = −1.5; 10% price discount. % change in revenue?",
  "%ΔQ = +15% → 0.9 × 1.15 = 1.035 → **+3.5%**.", tags=["calc"])

S = "Equilibrium & welfare calculations"
c(U4, S, "mi-ex-surplus-method", "Method: CS and PS with linear curves?",
  "1. Solve **p\\*, Q\\***\n2. Price-axis intercepts: set **Q = 0** in each equation\n3. **CS = ½ (p_max − p\\*) Q\\***\n4. **PS = ½ (p\\* − p_min) Q\\*** – if supply starts on the **Q-axis** (positive Q at p = 0), PS is a **trapezoid**", tags=["calc"])
c(U4, S, "mi-ex-120-2p", "Qd = 120 − 2p, Qs = 20 + 3p. Equilibrium, CS, PS?",
  "**p = 20, Q = 80**. CS = ½(60 − 20)(80) = **1,600**. PS = trapezoid ½(20 + 80)(20) = **1,000**. TS = **2,600**.", img="surplus-basic.png", tags=["calc"])
c(U4, S, "mi-ex-120-ceiling16", "Same market (Qd = 120 − 2p, Qs = 20 + 3p), max price €16. New welfare?",
  "Qs = **68**, Qd = 88 (shortage 20). WTP at 68 = **26**. CS = (26 − 16)·68 + ½(60 − 26)·68 = **1,836**. PS = ½(20 + 68)·16 = **704**. TS = **2,540** → DWL = **60**.", tags=["calc"])
c(U4, S, "mi-ex-300-2q", "p_d = 300 − 2Q, p_s = 100 + 3Q. Equilibrium and welfare?",
  "300 − 2Q = 100 + 3Q → **Q = 40, p = 220**. CS = ½(80)(40) = **1,600**; PS = ½(120)(40) = **2,400**; TS = **4,000**.", tags=["calc"])
c(U4, S, "mi-ex-duck", "Peking duck: Qd = 80 − 2p, Qs = −20 + 3p. Equilibrium and welfare?",
  "**p = 20, Q = 40**. CS = ½(40 − 20)(40) = **400**; PS = ½(20 − 6.67)(40) = **266.7**; TS = **666.7** (thousand CNY).", tags=["calc"])
c(U4, S, "mi-ex-duck-ceiling", "Peking duck with a ceiling of CNY 12: quantities, shortage, CS, PS, DWL?",
  "Qd = **56**, Qs = **16** → shortage **40**. WTP at 16 = 32. CS = 20·16 + ½·8·16 = **384**; PS = ½(12 − 6.67)·16 = **42.7**; DWL = **240**.", img="price-ceiling.png", tags=["calc", "diagram"])
c(U4, S, "mi-ex-500-2p", "Qd = 500 − 2p, Qs = −50 + 3p. Equilibrium and welfare? (Midterm 2025)",
  "**p = 110, Q = 280**. CS = ½(250 − 110)(280) = **19,600**; PS = ½(110 − 16.67)(280) = **13,066.7**.", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-600-4p", "Qd = 600 − 4p, Qs = 100 + 6p. Equilibrium and welfare? (Midterm 2023)",
  "**p = 50, Q = 400**. CS = ½(150 − 50)(400) = **20,000**; PS = trapezoid ½(100 + 400)(50) = **12,500**; TS = **32,500**.", tags=["calc", "past-exam"])
c(U4, S, "mi-ex-600-ceiling", "Same market (Qd = 600 − 4p, Qs = 100 + 6p) with max price €20: quantities and CS? Improved? (Midterm 2023)",
  "Qs = **220**, Qd = **520**. WTP at 220 = 95. CS = ½(130 + 75)(220) = **22,550** > 20,000 → consumers **better off** here.", tags=["calc", "past-exam"])

S = "Seminar 3 – Interventions (worked)"
c(U4, S, "mi-ex-s3-housing", "Housing: Qd = 60,000 − 20p, Qs = −20,000 + 30p. Equilibrium, CS, PS?",
  "**p = €1,600, Q = 28,000**. Choke price 3,000; supply starts at 666.67. CS = ½(1,400)(28,000) = **€19.6m**; PS = ½(933.3)(28,000) = **€13.07m**.", tags=["calc"],
  src="Seminar 3 – own worked solution (no official key)")
c(U4, S, "mi-ex-s3-housing-ceiling", "Housing with rent ceiling €1,000: CS, PS, DWL?",
  "Qs = **10,000**, Qd = 40,000 (shortage 30,000). WTP at 10,000 = 2,500. CS = 1,500·10,000 + ½·500·10,000 = **€17.5m** (↓!). PS = ½(333.3)(10,000) = **€1.67m**. DWL = **€13.5m**.", tags=["calc"],
  src="Seminar 3 – own worked solution (no official key)",
  explain="Here renters as a group are actually **worse off** (19.6m → 17.5m): supply is so elastic that the loss of 18,000 apartments outweighs the lower rent. With **more inelastic supply** fewer apartments would disappear and the ceiling would be more beneficial. Black market likely: the marginal renter would pay up to €2,500.")
c(U4, S, "mi-ex-s3-wage", "Platform workers: Ld = 6,000 − 4w, Ls = 2,000 + w. Equilibrium? Minimum wage €1,000 → unemployment?",
  "**w = €800, L = 5,200**. At €1,000: Ld = **2,000**, Ls = **3,000** → **unemployment 1,000**; job destruction 3,200.", img="minimum-wage.png", tags=["calc"],
  src="Seminar 3 – own worked solution (no official key)")
c(U4, S, "mi-ex-s3-wage-welfare", "Platform workers: are workers better or worse off with the €1,000 minimum wage?",
  "**Mixed**: the 2,000 who keep jobs earn more, 3,200 lose jobs. As a group worker surplus falls (≈ **€2.88m → €2.0m**); firms' surplus €1.82m → €0.5m.", tags=["calc"],
  src="Seminar 3 – own worked solution (no official key)",
  explain="Worker surplus = area above labour supply, below the wage. Supply hits L = 2,000 at w = 0, so before: trapezoid ½(2,000 + 5,200)·800 = 2.88m. After (assuming the 2,000 lowest-reservation-wage workers keep the jobs): 2,000 × 1,000 = 2.0m.")
c(U4, S, "mi-ex-s3-apples", "Apples: Qd = 200 − 2p, Qs = 3p. Equilibrium and welfare?",
  "**p = 40, Q = 120**. CS = ½(100 − 40)(120) = **3,600**; PS = ½(40)(120) = **2,400**; TS = **6,000**.", tags=["calc"],
  src="Seminar 3 – own worked solution (no official key)")
c(U4, S, "mi-ex-s3-quota", "Apples with a production quota of 80: price and producer surplus?",
  "Price from demand: 80 = 200 − 2p → **p = 60**. Supply price at 80 = 26.67. PS = 60·80 − ½·26.67·80 = **3,733** (↑ from 2,400). CS = **1,600**; DWL = **667**.",
  img="production-quota.png", tags=["calc", "diagram"], src="Seminar 3 – own worked solution (no official key)")


def build(unit_filter, zip_name):
    sel = [x for x in cards if x["unit"] in unit_filter]
    units = [{"name": n, "order": o} for n, o in UNITS if n in unit_filter]
    deck = {"format": "recall-v1", "subject": SUBJECT, "units": units, "cards": sel}
    tmp = f"/home/claude/out/build/{zip_name}"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp + "/images")
    used = {x["back_image"] for x in sel if x["back_image"]} | {x["front_image"] for x in sel if x["front_image"]}
    for u in used:
        shutil.copy("/home/claude/out/" + u, tmp + "/" + u)
    with open(tmp + "/cards.json", "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)
    zp = f"/home/claude/out/{zip_name}.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(tmp + "/cards.json", "cards.json")
        for u in sorted(used):
            z.write(tmp + "/" + u, u)
    return len(sel), len(used)

if __name__ == "__main__":
    ids = [x["id"] for x in cards]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for name, units in [("Micro_T1_Introduction", [U1]), ("Micro_T2_Market_Analysis", [U2]),
                        ("Micro_T3_Market_Interventions", [U3]), ("Micro_Exam_Practice", [U4]),
                        ("Micro_Midterm_ALL", [U1, U2, U3, U4])]:
        print(name, build(units, name))
