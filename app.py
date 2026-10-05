import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="RavenStack SaaS Customer Retention & Churn Dashboard",
    page_icon="🔄",
    layout="wide",
)


# Load & Clean Data
@st.cache_data
def load_data():
    accounts = pd.read_csv("ravenstack_accounts.csv")
    churn_events = pd.read_csv("ravenstack_churn_events.csv")
    feature_usage = pd.read_csv("ravenstack_feature_usage.csv")
    subscriptions = pd.read_csv("ravenstack_subscriptions.csv")
    tickets = pd.read_csv("ravenstack_support_tickets.csv")

    accounts["signup_date"] = pd.to_datetime(accounts["signup_date"])
    subscriptions["start_date"] = pd.to_datetime(subscriptions["start_date"])
    subscriptions["end_date"] = pd.to_datetime(subscriptions["end_date"])

    # Calculate tenure for churned subscriptions
    subscriptions["tenure_days"] = (
        subscriptions["end_date"] - subscriptions["start_date"]
    ).dt.days

    return accounts, churn_events, feature_usage, subscriptions, tickets


(
    accounts,
    churn_events,
    feature_usage,
    subscriptions,
    tickets,
) = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_industry = st.sidebar.multiselect(
    "Select Industry:",
    options=accounts["industry"].unique(),
    default=accounts["industry"].unique(),
)
selected_plan = st.sidebar.multiselect(
    "Select Plan Tier:",
    options=accounts["plan_tier"].unique(),
    default=accounts["plan_tier"].unique(),
)

filtered_accounts = accounts[
    (accounts["industry"].isin(selected_industry))
    & (accounts["plan_tier"].isin(selected_plan))
]

# Dashboard Title
st.title("🔄 RavenStack SaaS Retention & Churn Analytics Dashboard")
st.markdown("---")

# Key Performance Indicators
total_acc = len(filtered_accounts)
churned_acc = filtered_accounts["churn_flag"].sum()
churn_rate = (churned_acc / total_acc * 100) if total_acc > 0 else 0
retained_acc = total_acc - churned_acc
retention_rate = 100 - churn_rate

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Accounts", f"{total_acc:,}")
col2.metric("Active / Retained", f"{retained_acc:,}")
col3.metric("Churned Accounts", f"{churned_acc:,}")
col4.metric("Account Churn Rate", f"{churn_rate:.2f}%")

st.markdown("---")

# Charts Section 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("Industry-wise Churn Rates")
    ind_churn = (
        filtered_accounts.groupby("industry")
        .agg(
            total=("account_id", "count"), churned=("churn_flag", "sum")
        )
        .reset_index()
    )
    ind_churn["churn_rate"] = (
        ind_churn["churned"] / ind_churn["total"]
    ) * 100
    fig_ind = px.bar(
        ind_churn.sort_values(by="churn_rate", ascending=False),
        x="industry",
        y="churn_rate",
        color="churn_rate",
        color_continuous_scale="Reds",
        labels={"churn_rate": "Churn Rate (%)", "industry": "Industry"},
        title="Churn Rate by Industry Segment",
    )
    st.plotly_chart(fig_ind, use_container_width=True)

with c2:
    st.subheader("Primary Customer Churn Reasons")
    filtered_churn_events = churn_events[
        churn_events["account_id"].isin(filtered_accounts["account_id"])
    ]
    reasons = (
        filtered_churn_events["reason_code"]
        .value_counts()
        .reset_index()
    )
    reasons.columns = ["reason_code", "count"]
    fig_reason = px.pie(
        reasons,
        values="count",
        names="reason_code",
        hole=0.4,
        title="Distribution of Stated Churn Reasons",
    )
    st.plotly_chart(fig_reason, use_container_width=True)

# Charts Section 2
c3, c4 = st.columns(2)

with c3:
    st.subheader("Churn Distribution by Plan Tier")
    plan_summary = (
        filtered_accounts.groupby(["plan_tier", "churn_flag"])
        .size()
        .reset_index(name="count")
    )
    plan_summary["Status"] = plan_summary["churn_flag"].map(
        {True: "Churned", False: "Retained"}
    )
    fig_plan = px.bar(
        plan_summary,
        x="plan_tier",
        y="count",
        color="Status",
        barmode="group",
        title="Account Retention Status across Plan Tiers",
    )
    st.plotly_chart(fig_plan, use_container_width=True)

with c4:
    st.subheader("Churned Subscription Tenure (Days)")
    churned_subs = subscriptions[subscriptions["churn_flag"] == True]
    fig_hist = px.histogram(
        churned_subs,
        x="tenure_days",
        nbins=20,
        title="Distribution of Active Days Before Churn",
        labels={"tenure_days": "Active Tenure (Days)"},
        color_discrete_sequence=["#EF553B"],
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("---")

# Business Action Plan & Insights
st.subheader("💡 Key Strategic Retention Insights")
st.markdown("""
- **Industry Vulnerability**: **DevTools** exhibits the highest churn rate at **30.97%**, significantly above the 22.00% benchmark.
- **Critical Drop-off Window**: The median time to churn for canceled subscriptions is **42 days**, with over 50% occurring within the first 45 days.
- **Top Cancellation Drivers**: **Missing Features** (114 events), **Customer Support Friction** (104 events), and **Budget Constraints** (104 events) account for the majority of churn events.
- **Actionable Growth Strategy**: Implement mandatory 30-day onboarding check-ins for DevTools accounts and address missing feature requests to boost year-1 retention.
""")
