# Personalized Discount A/B Testing for Fashion E-commerce

## Business Problem

Fashion e-commerce platforms often use discounts to influence customer purchasing decisions. However, offering higher discounts does not necessarily mean higher business value.

This project evaluates whether personalized discounts can improve customer conversion enough to justify the additional discount offered.

The project uses a simulated fashion e-commerce dataset designed as a Myntra-like business use case.

---

## Objective

The main objective is to determine whether personalized discounts improve purchase conversion compared with a standard discount strategy.

### Key Business Question

> Does personalized discounting significantly improve customer conversion while generating enough additional revenue to justify the discount cost?

---

## Experiment Design

The dataset contains **2,000 simulated customers** divided into two groups:

| Group | Customers | Discount |
|---|---:|---|
| Control | 1,000 | 10% standard discount |
| Test | 1,000 | Personalized 15%, 20% or 25% discount |

Each customer represents one observation in the experiment.

The customer journey considered in the analysis is:

**Viewed → Added to Cart → Purchased → Order → Return**

---

## Key Metrics

The analysis focuses on:

- Conversion Rate
- Conversion Lift
- Average Order Value (AOV)
- Revenue per Customer
- Average Discount
- Cart Activity
- Return Rate
- Statistical Significance

---

## Tools & Technologies

- **Python**
- **Pandas**
- **SQL**
- **Excel**
- **Power BI**
- **DAX**
- **Power Query**
- **Statistical Hypothesis Testing**

---

## Analysis Process

### 1. Data Preparation

A simulated customer-level dataset was created containing information about:

- Customer demographics
- Product category
- Original price
- Discount percentage
- Final price
- Product views
- Cart additions
- Purchases
- Order value
- Delivery time
- Returns

### 2. Data Analysis

Python and Pandas were used to calculate:

- Conversion rates
- Conversion lift
- Average Order Value
- Revenue per customer
- Average discount

### 3. Statistical Testing

A Chi-Square test was used to determine whether the difference in purchase conversion between the Control and Test groups was statistically significant.

The hypothesis was:

**H₀:** Personalized discounts do not significantly affect conversion.

**H₁:** Personalized discounts significantly affect conversion.

A significance level of **5% (α = 0.05)** was used.

### 4. Dashboard

The results were visualized using Power BI to make the experiment easier to interpret from a business perspective.

---

## Key Findings

Based on the simulated experiment:

- The Test group showed a higher conversion rate than the Control group.
- The observed conversion lift was approximately **4.17%**.
- However, the Chi-Square test produced a **p-value of approximately 0.72**.
- Since the p-value is greater than 0.05, the difference was **not statistically significant**.
- The Control group had a higher Average Order Value than the Test group.
- Revenue per customer was also higher for the Control group in this simulation.

### Business Interpretation

Although personalized discounts produced a small observed improvement in conversion, the experiment does not provide sufficient statistical evidence that the improvement was caused by the discount strategy.

Therefore, the personalized discount strategy should **not be rolled out broadly based on this experiment alone**.

A larger or longer experiment could be conducted before making a final business decision.

---

## Business Recommendation

The recommended approach is:

1. Do not roll out the higher personalized discounts immediately.
2. Run the experiment with a larger sample size or longer duration.
3. Compare different discount levels separately.
4. Monitor conversion together with revenue per customer and discount cost.
5. Use personalized discounts selectively where the incremental revenue justifies the discount.

The key takeaway is:

> **Higher conversion does not automatically mean higher business value.**

A discount strategy should improve conversion while also maintaining healthy revenue economics.

---

## Dashboard

The Power BI dashboard provides an interactive view of:

- Control vs Test performance
- Conversion Rate
- Conversion Lift
- Average Order Value
- Revenue per Customer
- Discount comparison
- Customer purchase behavior
- Business conclusion

Dashboard screenshots are available in the `screenshots` folder.

---

## Project Structure

```text
Myntra-Personalized-Discount-AB-Testing/
│
├── README.md
│
├── data/
│   └── Myntra_AB_Testing_Dataset.xlsx
│
├── analysis/
│   └── code.py
│
├── dashboard/
│   └── Myntra_AB_Testing_Dashboard.pbix
│
└── screenshots/
    ├── dashboard_overview.png
    ├── conversion_analysis.png
    └── business_insights.png
