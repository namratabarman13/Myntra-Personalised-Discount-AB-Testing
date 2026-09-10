import pandas as pd
from scipy.stats import chi2_contingency

# --------------------------------
# 1. Load Excel file
# --------------------------------
df = pd.read_excel("MYNTRA.xlsx")

# Keep only the 14 columns we created
df = df.iloc[:, :14]

# Give columns their correct names
df.columns = [
    "Customer_ID",
    "Group",
    "Age",
    "Gender",
    "Category",
    "Original_Price",
    "Discount_Percent",
    "Final_Price",
    "Viewed",
    "Added_to_Cart",
    "Purchased",
    "Order_Value",
    "Delivery_Days",
    "Return"
]

# --------------------------------
# 2. Conversion Rate
# --------------------------------
conversion = df.groupby("Group")["Purchased"].mean() * 100

control_rate = conversion["Control"]
test_rate = conversion["Test"]

lift = ((test_rate - control_rate) / control_rate) * 100

# --------------------------------
# 3. Average Order Value
# --------------------------------
aov = (
    df[df["Purchased"] == 1]
    .groupby("Group")["Order_Value"]
    .mean()
)

# --------------------------------
# 4. Revenue per Customer
# --------------------------------
revenue_per_customer = (
    df.groupby("Group")["Order_Value"]
    .mean()
)

# --------------------------------
# 5. Average Discount
# --------------------------------
discount = (
    df.groupby("Group")["Discount_Percent"]
    .mean()
)

# --------------------------------
# 6. Return Rate
# --------------------------------
return_rate = (
    df[df["Purchased"] == 1]
    .groupby("Group")["Return"]
    .mean() * 100
)

# --------------------------------
# 7. Chi-Square Test
# --------------------------------
table = pd.crosstab(df["Group"], df["Purchased"])

chi2, p_value, dof, expected = chi2_contingency(table)

if p_value < 0.05:
    significance = "Statistically Significant"
else:
    significance = "Not Statistically Significant"

# --------------------------------
# 8. Business Conclusion
# --------------------------------
if p_value < 0.05 and test_rate > control_rate:
    conclusion = "Personalized discounts significantly improved conversion. Consider rolling out the strategy."
else:
    conclusion = "Personalized discounts did not significantly improve conversion. Do not roll out the strategy yet."

# --------------------------------
# 9. Create Analysis Tables
# --------------------------------

conversion_df = conversion.reset_index()
conversion_df.columns = ["Group", "Conversion_Rate_%"]

aov_df = aov.reset_index()
aov_df.columns = ["Group", "Average_Order_Value"]

revenue_df = revenue_per_customer.reset_index()
revenue_df.columns = ["Group", "Revenue_Per_Customer"]

discount_df = discount.reset_index()
discount_df.columns = ["Group", "Average_Discount_%"]

return_df = return_rate.reset_index()
return_df.columns = ["Group", "Return_Rate_%"]

summary_df = pd.DataFrame({
    "Metric": [
        "Control Conversion Rate",
        "Test Conversion Rate",
        "Conversion Lift",
        "Control AOV",
        "Test AOV",
        "Control Revenue per Customer",
        "Test Revenue per Customer",
        "Control Average Discount",
        "Test Average Discount",
        "Control Return Rate",
        "Test Return Rate",
        "Chi-Square Statistic",
        "P-Value",
        "Statistical Result"
    ],
    "Value": [
        control_rate,
        test_rate,
        lift,
        aov["Control"],
        aov["Test"],
        revenue_per_customer["Control"],
        revenue_per_customer["Test"],
        discount["Control"],
        discount["Test"],
        return_rate["Control"],
        return_rate["Test"],
        chi2,
        p_value,
        significance
    ]
})

# --------------------------------
# 10. SAVE EVERYTHING TO EXCEL
# --------------------------------

with pd.ExcelWriter("Myntra_Analysis.xlsx", engine="openpyxl") as writer:

    df.to_excel(writer, sheet_name="Data", index=False)

    summary_df.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    conversion_df.to_excel(
        writer,
        sheet_name="Conversion",
        index=False
    )

    aov_df.to_excel(
        writer,
        sheet_name="AOV",
        index=False
    )

    revenue_df.to_excel(
        writer,
        sheet_name="Revenue",
        index=False
    )

    discount_df.to_excel(
        writer,
        sheet_name="Discount",
        index=False
    )

    return_df.to_excel(
        writer,
        sheet_name="Returns",
        index=False
    )

print("\n==============================")
print("MYNTRA A/B TESTING ANALYSIS")
print("==============================")

print("\nConversion Rate:")
print(conversion)

print("\nConversion Lift:", round(lift, 2), "%")

print("\nAverage Order Value:")
print(aov)

print("\nRevenue per Customer:")
print(revenue_per_customer)

print("\nAverage Discount:")
print(discount)

print("\nReturn Rate:")
print(return_rate)

print("\nChi-Square Test")
print("P-value:", p_value)

print("\nResult:", significance)

print("\nBusiness Conclusion:")
print(conclusion)

print("\n==============================")
print("Analysis saved as Myntra_Analysis.xlsx")
print("==============================")


# ==========================================
# FINAL BUSINESS ANALYSIS
# ==========================================

