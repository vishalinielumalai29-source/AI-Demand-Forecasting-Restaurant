import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="AI Restaurant Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3, h4, h5 {
    color: white;
}

.metric-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    text-align: center;
    color: white;
}

.hero-container {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        #FF4B4B,
        #7C3AED
    );
    color: white;
}

.small-text {
    color: #D1D5DB;
}

</style>
""", unsafe_allow_html=True)


# =========================================
# LOAD DATA
# =========================================

forecast_df = pd.read_csv(
    r"C:\Users\eluma\Desktop\restaurant-ai-project\results\forecast_results.csv"
)

inventory_df = pd.read_csv(
    r"C:\Users\eluma\Desktop\restaurant-ai-project\results\inventory_optimization_results.csv"
)


# =========================================
# LOAD IMAGE
# =========================================

hero_image = Image.open(
    r"C:\Users\eluma\Desktop\restaurant-ai-project\images\restaurant_ai.jpg"
)


# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "🏠 Overview",
        "📈 Forecast Analytics",
        "📦 Inventory Optimization",
        "💼 Business Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "AI-Powered Restaurant Intelligence System"
)

st.sidebar.info(
    """
    This platform uses:
    
    ✅ Machine Learning
    
    ✅ Demand Forecasting
    
    ✅ Inventory Optimization
    
    ✅ Service-Level Analytics
    """
)


# =========================================
# OVERVIEW PAGE
# =========================================

if page == "🏠 Overview":

    # HERO BANNER

    st.markdown("""
    <div class="hero-container">
        <h1>
        🍽️ AI Demand Forecasting & Inventory Optimization
        </h1>

        <h4>
        Smart Restaurant Inventory Intelligence Dashboard
        </h4>

        <p class="small-text">
        AI-powered forecasting and operational analytics platform
        for reducing stockout risk and improving service reliability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")


    # RESTAURANT IMAGE

    st.image(
        hero_image,
        caption="AI-Powered Restaurant Intelligence",
        use_container_width=True
    )

    st.write("")


    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>95.61%</h2>
            <p>Service Level</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>4.39%</h2>
            <p>Stockout Rate</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>50%</h2>
            <p>Risk Reduction</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>AI</h2>
            <p>Inventory Optimization</p>
        </div>
        """, unsafe_allow_html=True)


    st.write("")
    st.write("")


    # OVERVIEW CHART

    st.subheader("📈 Demand Forecast Overview")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=forecast_df['Actual_Orders'].values[:100],
            mode='lines',
            name='Actual Orders'
        )
    )

    fig.add_trace(
        go.Scatter(
            y=forecast_df['Predicted_Orders'].values[:100],
            mode='lines',
            name='Predicted Orders'
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # FORECAST TABLE

    st.subheader("📋 Forecast Data Preview")

    st.dataframe(
        forecast_df.head(10),
        use_container_width=True
    )


# =========================================
# FORECAST ANALYTICS
# =========================================

elif page == "📈 Forecast Analytics":

    st.title("📈 Forecast Analytics Dashboard")

    st.write(
        """
        Machine Learning models were used
        to forecast restaurant food demand.
        """
    )


    # FILTER

    top_n = st.slider(
        "Select Number of Samples",
        50,
        300,
        100
    )


    # FORECAST CHART

    fig = px.line(
        forecast_df.head(top_n),

        y=[
            'Actual_Orders',
            'Predicted_Orders'
        ],

        template='plotly_dark',

        title='Actual vs Predicted Orders'
    )

    fig.update_layout(
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # FORECAST ERROR

    forecast_df['Forecast_Error'] = (
        forecast_df['Actual_Orders']
        - forecast_df['Predicted_Orders']
    )

    fig2 = px.histogram(
        forecast_df,

        x='Forecast_Error',

        template='plotly_dark',

        title='Forecast Error Distribution'
    )

    fig2.update_layout(
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


    # DOWNLOAD BUTTON

    st.download_button(
        label="📥 Download Forecast Results",

        data=forecast_df.to_csv(
            index=False
        ),

        file_name="forecast_results.csv",

        mime="text/csv"
    )


# =========================================
# INVENTORY OPTIMIZATION
# =========================================

elif page == "📦 Inventory Optimization":

    st.title("📦 Inventory Optimization Dashboard")

    st.write(
        """
        AI-powered inventory optimization system
        using demand forecasting and safety stock logic.
        """
    )


    # KPI SECTION

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📈 Service Level",
            "95.61%"
        )

    with col2:
        st.metric(
            "⚠️ Stockout Rate",
            "4.39%"
        )

    with col3:
        st.metric(
            "🚀 Risk Reduction",
            "50%"
        )


    st.write("")


    # FILTER

    top_n = st.slider(
        "Select Number of Inventory Samples",
        50,
        300,
        100
    )


    # INVENTORY CHART

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=inventory_df['Actual_Orders'].values[:top_n],
            mode='lines',
            name='Actual Orders'
        )
    )

    fig.add_trace(
        go.Scatter(
            y=inventory_df['Predicted_Orders'].values[:top_n],
            mode='lines',
            name='Predicted Orders'
        )
    )

    fig.add_trace(
        go.Scatter(
            y=inventory_df['Recommended_Stock'].values[:top_n],
            mode='lines',
            name='Recommended Stock'
        )
    )

    fig.update_layout(
        template="plotly_dark",
        title="Inventory Recommendation System",
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # REORDER ALERTS

    st.subheader("🚨 Reorder Alerts")

    if 'Low_Stock_Alert' in inventory_df.columns:

        reorder_df = inventory_df[
            inventory_df['Low_Stock_Alert']
            == 'REORDER REQUIRED'
        ]

        if len(reorder_df) > 0:

            st.error(
                f"⚠️ {len(reorder_df)} inventory records require immediate reorder action."
            )

            st.dataframe(
                reorder_df.head(20),
                use_container_width=True
            )

        else:

            st.success(
                "✅ No immediate reorder actions required."
            )


    # DEMAND RISK DISTRIBUTION

    if 'Demand_Risk' in inventory_df.columns:

        st.subheader("📊 Demand Risk Distribution")

        risk_counts = inventory_df[
            'Demand_Risk'
        ].value_counts()

        fig2 = px.pie(
            names=risk_counts.index,
            values=risk_counts.values,

            template='plotly_dark',

            title='Demand Risk Categories'
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )


    # INVENTORY TABLE

    st.subheader("📋 Inventory Optimization Table")

    st.dataframe(
        inventory_df.head(25),
        use_container_width=True
    )


    # DOWNLOAD BUTTON

    st.download_button(
        label="📥 Download Inventory Report",

        data=inventory_df.to_csv(
            index=False
        ),

        file_name="inventory_optimization_results.csv",

        mime="text/csv"
    )


# =========================================
# BUSINESS INSIGHTS
# =========================================

elif page == "💼 Business Insights":

    st.title("💼 Business Insights Dashboard")

    st.write(
        """
        AI-assisted inventory optimization improves
        operational efficiency and reduces stockout risks.
        """
    )


    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📈 Service Level",
            "95.61%"
        )

    with col2:
        st.metric(
            "⚠️ Stockout Rate",
            "4.39%"
        )

    with col3:
        st.metric(
            "🚀 Risk Reduction",
            "50%"
        )

    with col4:
        st.metric(
            "🤖 AI Forecasting",
            "ACTIVE"
        )


    st.write("")


    # GAUGE CHART

    st.subheader("📈 Service Level Gauge")

    gauge_fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=95.61,

            title={'text': "Service Level %"},

            gauge={
                'axis': {'range': [0, 100]},

                'bar': {'color': "lime"},

                'steps': [
                    {'range': [0, 70], 'color': "red"},
                    {'range': [70, 90], 'color': "orange"},
                    {'range': [90, 100], 'color': "green"}
                ]
            }
        )
    )

    gauge_fig.update_layout(
        template="plotly_dark",
        height=400
    )

    st.plotly_chart(
        gauge_fig,
        use_container_width=True
    )


    # PERFORMANCE CHART

    performance_data = pd.DataFrame({
        "Metric": [
            "Service Level",
            "Stockout Reduction",
            "Forecast Reliability",
            "Inventory Optimization"
        ],

        "Score": [
            95.61,
            50,
            89,
            93
        ]
    })

    fig = px.bar(
        performance_data,

        x="Metric",

        y="Score",

        template="plotly_dark",

        title="Business Performance Metrics"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # AI RECOMMENDATIONS

    st.subheader("🤖 AI Recommendations")

    st.success(
        "✅ Maintain current safety stock strategy to sustain 95%+ service level."
    )

    st.info(
        "📈 Monitor high-demand meals during promotional periods."
    )

    st.warning(
        "⚠️ Reorder alerts should be prioritized for low-stock inventory items."
    )

    st.success(
        "🚀 AI-assisted forecasting reduced operational stockout risk significantly."
    )


    # EXECUTIVE SUMMARY

    st.subheader("📋 Executive Summary")

    st.write(
        """
        This AI-powered demand forecasting and inventory optimization system
        helps restaurants improve operational planning through:

        - Accurate demand forecasting
        - Inventory optimization
        - Stockout prevention
        - AI-driven reorder planning
        - Improved service reliability

        The system achieved a business-acceptable
        service level of 95.61% while reducing stockout
        risks significantly.
        """
    )


    # DOWNLOAD REPORT

    business_report = performance_data.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download Business Report",

        data=business_report,

        file_name="business_insights_report.csv",

        mime="text/csv"
    )


# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.caption(
    "Developed using Machine Learning, CatBoost Forecasting, and Inventory Optimization Analytics."
)