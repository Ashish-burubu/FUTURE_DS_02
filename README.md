# 🔄 RavenStack SaaS Customer Retention & Churn Analytics

## 🎯 Executive Summary
This project analyzes customer retention, churn drivers, and customer lifecycle metrics for **RavenStack**, a B2B SaaS platform. Analyzing **500 corporate accounts**, **5,000 subscriptions**, **600 churn events**, and **2,000 support tickets**, this study provides targeted strategies to mitigate revenue leakage and increase customer lifetime value (LTV).

---

## 📈 Key Retention & Churn Metrics
| Metric | Value |
| :--- | :--- |
| **Total Accounts Analyzed** | **500** |
| **Active / Retained Accounts** | **390 (78.00%)** |
| **Churned Accounts** | **110 (22.00%)** |
| **Median Days to Churn** | **42 Days** |
| **Highest Churn Industry** | **DevTools (30.97%)** |

---

## 🔍 Key Findings & Analysis

### 1. Industry Churn Variance
- **DevTools**: **30.97%** Churn Rate (35 / 113 accounts lost)
- **FinTech**: **22.32%** Churn Rate (25 / 112 accounts lost)
- **HealthTech**: **21.88%** Churn Rate (21 / 96 accounts lost)
- **EdTech**: **16.46%** Churn Rate (13 / 79 accounts lost)
- **Cybersecurity**: **16.00%** Churn Rate (16 / 100 accounts lost)

> ⚠️ **Key Risk:** DevTools accounts churn at nearly **1.5x the rate** of Cybersecurity or EdTech accounts due to specialized feature requirements.

### 2. High-Risk Customer Lifecycle Window
- **Early Churn Risk**: Over **50% of churned subscriptions cancel within 42 days** of starting.
- **Plan Tiers**: Churn rates remain uniform across Basic (22.02%), Pro (21.91%), and Enterprise (22.08%) tiers, indicating that churn is driven by onboarding/product-market fit issues rather than plan pricing alone.

### 3. Primary Root Causes of Churn
1. **Missing Features**: 114 churn events (19.0%)
2. **Customer Support Issues**: 104 churn events (17.3%)
3. **Budget / ROI Constraints**: 104 churn events (17.3%)
4. **Competitor Switching**: 92 churn events (15.3%)

---

## 💡 Strategic Business Recommendations
1. **Implement 30-Day Onboarding Workflows**: Launch automated onboarding sequences and dedicated Customer Success check-ins within the first 30 days to bypass the 42-day cancellation drop-off point.
2. **Product Roadmap Alignment for DevTools**: Prioritize key missing integrations requested by DevTools clients to lower their 30.97% churn rate.
3. **Proactive Support Resolution**: Streamline resolution workflows for high-priority support tickets to eliminate support friction as a churn trigger.

---

## 🛠️ Tools & Technologies Used
- **Python** (Pandas, Plotly)
- **Streamlit** (Interactive Dashboard Deployment)
- **Cohort Analysis & SaaS Metrics**

---
