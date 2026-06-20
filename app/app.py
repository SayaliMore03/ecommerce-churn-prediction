import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Churn Intelligence | E-Commerce",
    page_icon="🛒",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0F1117;
}

/* Header */
.hero-header {
    background: linear-gradient(135deg, #1a1f2e 0%, #16213e 50%, #0f3460 100%);
    border: 1px solid rgba(99, 179, 237, 0.15);
    border-radius: 16px;
    padding: 32px 40px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(99,179,237,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 6px 0;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    font-size: 14px;
    color: #8892a4;
    margin: 0;
    font-weight: 400;
}
.hero-badge {
    display: inline-block;
    background: rgba(99,179,237,0.12);
    border: 1px solid rgba(99,179,237,0.3);
    color: #63b3ed;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
            
/* Remove Streamlit top padding */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

section[data-testid="stSidebar"] { display: none; }
div[data-testid="stToolbar"] { display: none; }
div[data-testid="stDecoration"] { display: none; }
div[data-testid="stStatusWidget"] { display: none; }

/* Section labels */
.section-label {
    font-size: 11px;
    font-weight: 600;
    color: #63b3ed;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(99,179,237,0.15);
}

/* Cards */
.input-card {
    background: #1a1f2e;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
}

/* Result cards */
.result-card {
    background: #1a1f2e;
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.06);
}
.prob-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 56px;
    font-weight: 700;
    line-height: 1;
    margin: 8px 0;
}
.prob-label {
    font-size: 12px;
    color: #8892a4;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}
.risk-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 24px;
    font-size: 13px;
    font-weight: 600;
    margin-top: 12px;
}
.risk-high {
    background: rgba(245, 101, 101, 0.12);
    border: 1px solid rgba(245,101,101,0.3);
    color: #fc8181;
}
.risk-medium {
    background: rgba(237, 137, 54, 0.12);
    border: 1px solid rgba(237,137,54,0.3);
    color: #f6ad55;
}
.risk-low {
    background: rgba(72, 187, 120, 0.12);
    border: 1px solid rgba(72,187,120,0.3);
    color: #68d391;
}

/* Progress bar */
.progress-wrap {
    background: rgba(255,255,255,0.06);
    border-radius: 8px;
    height: 8px;
    margin: 20px 0;
    overflow: hidden;
}
.progress-fill-high { background: linear-gradient(90deg, #fc8181, #f56565); border-radius: 8px; height: 8px; }
.progress-fill-medium { background: linear-gradient(90deg, #f6ad55, #ed8936); border-radius: 8px; height: 8px; }
.progress-fill-low { background: linear-gradient(90deg, #68d391, #48bb78); border-radius: 8px; height: 8px; }

/* Recommendation box */
.rec-box {
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 8px;
    line-height: 1.6;
    font-size: 14px;
}
.rec-urgent {
    background: rgba(245,101,101,0.08);
    border-left: 3px solid #fc8181;
    color: #fed7d7;
}
.rec-warning {
    background: rgba(237,137,54,0.08);
    border-left: 3px solid #f6ad55;
    color: #feebc8;
}
.rec-success {
    background: rgba(72,187,120,0.08);
    border-left: 3px solid #68d391;
    color: #c6f6d5;
}

/* Metric tiles */
.metric-tile {
    background: #1a1f2e;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
    margin-bottom: 12px;
}
.metric-tile-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #63b3ed;
}
.metric-tile-label {
    font-size: 11px;
    color: #8892a4;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 4px;
}

/* Divider */
.divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin: 24px 0;
}

/* Override Streamlit elements */
div[data-testid="stSlider"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label {
    color: #a0aec0 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

.stButton button {
    background: linear-gradient(135deg, #3182ce, #2b6cb0) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 28px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
    transition: all 0.2s !important;
    letter-spacing: 0.3px !important;
}
.stButton button:hover {
    background: linear-gradient(135deg, #2b6cb0, #2c5282) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 25px rgba(49,130,206,0.35) !important;
}

footer { display: none !important; }
#MainMenu { display: none !important; }
header { display: none !important; }
.block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
div[data-testid="stToolbar"] { display: none !important; }
div[data-testid="stDecoration"] { display: none !important; }
div[data-testid="stStatusWidget"] { display: none !important; }
""", unsafe_allow_html=True)

# ── Load Artifacts ────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache_resource
def load_artifacts():
    model    = joblib.load(os.path.join(BASE_DIR, 'models', 'best_model.pkl'))
    scaler   = joblib.load(os.path.join(BASE_DIR, 'models', 'scaler.pkl'))
    features = joblib.load(os.path.join(BASE_DIR, 'models', 'feature_columns.pkl'))
    return model, scaler, features

model, scaler, feature_columns = load_artifacts()

# ── Hero Header ───────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <div class="hero-badge">🛒 E-Commerce Analytics</div>
    <div class="hero-title">Customer Churn Intelligence</div>
    <div class="hero-subtitle">Predict churn risk in real-time and get AI-powered retention recommendations</div>
</div>
""", unsafe_allow_html=True)

# ── Model Stats Bar ───────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="metric-tile"><div class="metric-tile-value">99.7%</div><div class="metric-tile-label">ROC-AUC Score</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-tile"><div class="metric-tile-value">93.7%</div><div class="metric-tile-label">F1 Score</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-tile"><div class="metric-tile-value">94.2%</div><div class="metric-tile-label">Recall</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="metric-tile"><div class="metric-tile-value">5,630</div><div class="metric-tile-label">Training Records</div></div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Input Form ────────────────────────────────────────────────
left_col, right_col = st.columns([1.2, 0.8], gap="large")

with left_col:
    st.markdown('<div class="section-label">Customer Profile</div>', unsafe_allow_html=True)

    r1c1, r1c2, r1c3 = st.columns(3)
    with r1c1:
        tenure = st.slider("Tenure (months)", 0, 61, 12)
    with r1c2:
        satisfaction = st.slider("Satisfaction Score", 1, 5, 3)
    with r1c3:
        days_since_order = st.slider("Days Since Last Order", 0, 30, 5)

    r2c1, r2c2, r2c3 = st.columns(3)
    with r2c1:
        order_count = st.number_input("Orders Last Month", 0, 16, 3)
    with r2c2:
        hour_on_app = st.number_input("Hours on App / Month", 0, 6, 2)
    with r2c3:
        cashback = st.number_input("Cashback Amount (₹)", 0.0, 500.0, 150.0)

    r3c1, r3c2, r3c3 = st.columns(3)
    with r3c1:
        coupon_used = st.number_input("Coupons Used", 0, 16, 2)
    with r3c2:
        num_address = st.number_input("Addresses Saved", 1, 22, 3)
    with r3c3:
        num_devices = st.number_input("Devices Registered", 1, 6, 2)

    st.markdown('<div class="section-label" style="margin-top:20px">Behaviour & Preferences</div>', unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3)
    with b1:
        complain = st.selectbox("Filed Complaint?", [0, 1],
                                format_func=lambda x: "Yes ⚠️" if x==1 else "No ✓")
        gender = st.selectbox("Gender", [0, 1],
                              format_func=lambda x: "Female" if x==0 else "Male")
    with b2:
        preferred_cat = st.selectbox("Preferred Category", [0,1,2,3,4],
                                     format_func=lambda x: ['Fashion','Grocery',
                                     'Laptop & Accessory','Mobile','Others'][x])
        marital_status = st.selectbox("Marital Status", [0,1,2],
                                      format_func=lambda x: ['Divorced','Married','Single'][x])
    with b3:
        login_device = st.selectbox("Login Device", [0, 1],
                                    format_func=lambda x: "Computer" if x==0 else "Mobile")
        city_tier = st.selectbox("City Tier", [1, 2, 3])

    b4, b5, b6 = st.columns(3)
    with b4:
        payment_mode = st.selectbox("Payment Mode", [0,1,2,3,4],
                                    format_func=lambda x: ['Cash on Delivery','Credit Card',
                                    'Debit Card','E wallet','UPI'][x])
    with b5:
        warehouse_dist = st.number_input("Warehouse Distance (km)", 5, 127, 15)
    with b6:
        order_hike = st.number_input("Order Hike YoY (%)", 11, 26, 15)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🔍  Analyse Churn Risk", use_container_width=True)

# ── Results Panel ─────────────────────────────────────────────
with right_col:
    st.markdown('<div class="section-label">Prediction Output</div>', unsafe_allow_html=True)

    if predict_btn:
        input_dict = {
            'Tenure': tenure, 'PreferredLoginDevice': login_device,
            'CityTier': city_tier, 'WarehouseToHome': warehouse_dist,
            'PreferredPaymentMode': payment_mode, 'Gender': gender,
            'HourSpendOnApp': hour_on_app, 'NumberOfDeviceRegistered': num_devices,
            'PreferredOrderCat': preferred_cat, 'SatisfactionScore': satisfaction,
            'MaritalStatus': marital_status, 'NumberOfAddress': num_address,
            'Complain': complain, 'OrderAmountHikeFromlastYear': order_hike,
            'CouponUsed': coupon_used, 'OrderCount': order_count,
            'DaySinceLastOrder': days_since_order, 'CashbackAmount': cashback,
        }

        input_df = pd.DataFrame([input_dict])
        input_df['EngagementScore'] = input_df['HourSpendOnApp']*0.4 + input_df['OrderCount']*0.4 + input_df['CouponUsed']*0.2
        input_df['IsInactive']      = (input_df['DaySinceLastOrder'] >= 7).astype(int)
        input_df['IsHighValue']     = (input_df['CashbackAmount'] >= 150).astype(int)
        input_df['ComplainLowSat']  = ((input_df['Complain']==1) & (input_df['SatisfactionScore']<=2)).astype(int)
        input_df     = input_df[feature_columns]
        input_scaled = scaler.transform(input_df)

        prob  = model.predict_proba(input_scaled)[0][1]
        label = 1 if prob >= 0.3 else 0
        pct   = prob * 100
        width = f"{pct:.0f}%"

        if prob >= 0.5:
            risk_label  = "🔴 HIGH RISK"
            badge_class = "risk-high"
            bar_class   = "progress-fill-high"
            color       = "#fc8181"
        elif prob >= 0.3:
            risk_label  = "🟠 MEDIUM RISK"
            badge_class = "risk-medium"
            bar_class   = "progress-fill-medium"
            color       = "#f6ad55"
        else:
            risk_label  = "🟢 LOW RISK"
            badge_class = "risk-low"
            bar_class   = "progress-fill-low"
            color       = "#68d391"

        st.markdown(f"""
        <div class="result-card">
            <div class="prob-label">Churn Probability</div>
            <div class="prob-number" style="color:{color}">{pct:.1f}%</div>
            <div class="progress-wrap">
                <div class="{bar_class}" style="width:{width}"></div>
            </div>
            <span class="risk-badge {badge_class}">{risk_label}</span>
        </div>
        """, unsafe_allow_html=True)

        # Key signals
        signals = []
        if tenure < 3:       signals.append(("⏱", "New customer (high-risk window)"))
        if complain == 1:    signals.append(("⚠️", "Complaint filed"))
        if satisfaction <= 2: signals.append(("😞", "Low satisfaction score"))
        if days_since_order >= 7: signals.append(("💤", "Inactive 7+ days"))
        if cashback < 100:   signals.append(("💰", "Low cashback earner"))
        if preferred_cat == 3: signals.append(("📱", "Mobile category buyer"))

        if signals:
            st.markdown('<div class="section-label" style="margin-top:8px">Risk Signals Detected</div>', unsafe_allow_html=True)
            for icon, text in signals:
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:10px;padding:8px 12px;
                background:rgba(255,255,255,0.03);border-radius:8px;margin-bottom:6px;
                font-size:13px;color:#a0aec0;border:1px solid rgba(255,255,255,0.05)">
                    <span>{icon}</span><span>{text}</span>
                </div>""", unsafe_allow_html=True)

        # Recommendation
        st.markdown('<div class="section-label" style="margin-top:16px">Retention Action</div>', unsafe_allow_html=True)

        if label == 1:
            if complain == 1 and satisfaction <= 2:
                rec_class = "rec-urgent"
                rec = "⚡ <strong>Urgent Action Required</strong><br>Complaint filed with low satisfaction — escalate to support team immediately. Offer a personalised discount or free delivery on next order to prevent churn."
            elif tenure < 3:
                rec_class = "rec-warning"
                rec = "🎁 <strong>New Customer at Risk</strong><br>Enroll in the 90-day onboarding loyalty program. Send a welcome coupon pack at day 7, 30, and 60 to build habit formation."
            elif days_since_order >= 7:
                rec_class = "rec-warning"
                rec = "📧 <strong>Re-engagement Campaign</strong><br>Customer has been inactive for 7+ days. Trigger a personalised 'We miss you' email with cashback offer on their preferred category."
            elif cashback < 100:
                rec_class = "rec-warning"
                rec = "💰 <strong>Upgrade Cashback Tier</strong><br>Low cashback earner showing churn signals. Auto-upgrade to next cashback tier and show potential savings on preferred category."
            else:
                rec_class = "rec-warning"
                rec = "🎯 <strong>Targeted Retention Offer</strong><br>Customer showing churn signals. Offer a limited-time exclusive deal on their preferred category to re-engage."
        else:
            rec_class = "rec-success"
            rec = "✅ <strong>Customer is Retained</strong><br>Low churn risk detected. Continue standard engagement. Consider upselling premium membership based on their order activity."

        st.markdown(f'<div class="rec-box {rec_class}">{rec}</div>', unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
            background:#1a1f2e;
            border:1px dashed rgba(99,179,237,0.2);
            border-radius:16px;
            padding:48px 32px;
            text-align:center;
            color:#4a5568;
        ">
            <div style="font-size:40px;margin-bottom:16px">🔍</div>
            <div style="font-size:15px;font-weight:500;color:#8892a4;margin-bottom:8px">
                No prediction yet
            </div>
            <div style="font-size:13px;color:#4a5568">
                Fill in the customer details on the left<br>and click Analyse Churn Risk
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;color:#4a5568;font-size:12px;padding:8px 0 16px">
    Model: Random Forest &nbsp;|&nbsp; Dataset: E-Commerce Churn (5,630 records) &nbsp;|&nbsp;
    Built by <span style="color:#63b3ed;font-weight:500">Sayali More</span>
</div>
""", unsafe_allow_html=True)