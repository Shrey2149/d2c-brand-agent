# d2c-brand-agent

### Problem

A D2C brand’s data is scattered across many places:

- Reviews on the website, Amazon, Myntra and Instagram comments
- Sales and returns in Shopify or an internal dashboard
- Product details in a catalog sheet
- Competitor prices on other brands’ websites

When someone has a business question, they jump between all of these, export to Excel, read hundreds of reviews by hand, and put a slide together. That can take hours or days, for questions like:
- “Returns on our joggers went up this month. Why?”
- “What are customers complaining about most in winter wear?”
- “Are we priced too high compared to similar brands?”
- “Which products should we restock, and which should we discount?”

### Who uses it

- Brand and category managers, who own a product line and need answers fast
- Growth and marketing teams, who want to know what customers love so they can use it in ads
- Founders and leadership, who want a quick weekly summary without opening five dashboards

## Architecture

```mermaid
flowchart TD
    U["User question<br/>e.g. Why are joggers returned so much?"] --> A["Agent loop<br/>(Python)"]
    A <-->|"sends context, gets next step"| L["LLM<br/>(Claude / GPT / Gemini)"]

    A -->|"runs tool"| T1["get_product_info"]
    A -->|"runs tool"| T2["search_reviews"]
    A -->|"runs tool"| T3["get_sales"]
    A -->|"runs tool"| T4["compare_prices"]

    T1 --> D1[("products.csv")]
    T2 --> D2[("reviews.csv")]
    T3 --> D3[("sales.csv")]
    T4 --> D4[("competitors.csv")]

    T1 & T2 & T3 & T4 -.->|"result goes back"| A
    A -->|"when LLM says done"| R["Report<br/>answer + chart"]
```
