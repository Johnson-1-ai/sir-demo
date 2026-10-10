import streamlit as st
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go
st.title("SIR 传染病模型交互模拟")
st.caption("拖动左侧参数，观察疫情曲线变化")

st.sidebar.title("the second-level title")
beta = st.sidebar.slider("β（感染率）", 0.0, 1.0, 0.3,0.01)
gamma = st.sidebar.slider("γ（恢复率）", 0.0, 1.0, 0.1,0.01)
N = st.sidebar.slider("N（总人口）", 100, 1000000, 10000)

st.write(beta,gamma,N)

def sir(y,t,beta,gamma,N):
    S,I,R =y

    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I

    return dS, dI, dR

I0 = 10
S0 = N - I0
R_init = 0
y0 = [S0, I0, R_init]

t = np.linspace(0,160,1600)
sol = odeint(sir,y0,t,args=(beta,gamma,N))




#画SIR
S = sol[:, 0]
I = sol[:, 1]
R = sol[:, 2]

fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=S, name="易感者 S", mode="lines"))
fig.add_trace(go.Scatter(x=t, y=I, name="感染者 I", mode="lines"))
fig.add_trace(go.Scatter(x=t, y=R, name="康复者 R", mode="lines"))

fig.update_layout(
    xaxis_title="天数",
    yaxis_title="人数",
    hovermode="x unified",
)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=S, y=I, mode="lines", name="S-I 相图"))
fig2.update_layout(
    xaxis_title="易感者 S",
    yaxis_title="感染者 I",
)

col1, col2 = st.columns([1.2,1])

with col1:
    st.subheader("SIR 曲线")
    st.plotly_chart(fig)

with col2:
    st.subheader("S-I 相图")
    st.plotly_chart(fig2)








R0 = beta / gamma
peak_I = I.max()
peak_t = t[I.argmax()]
col1, col2, col3 = st.columns(3)
col1.metric("基本传染数 R0", f"{R0:.2f}")
col2.metric("感染峰值", f"{peak_I:,.0f}")
col3.metric("峰值时间（天）", f"{peak_t:.1f}")


st.markdown("""
**SIR 模型**把总人口分成三类：

- **S（易感者）**：还没得病、可能被感染的人
- **I（感染者）**：已经得病、能传染别人的人
- **R（康复者）**：康复后不再参与传播的人

模型假设：

1. 总人口 N 不变，S + I + R = N
2. 感染者按 β 的比例传染易感者
3. 感染者按 γ 的比例康复

关键指标 **R0 = β / γ**：一个感染者平均能传染几个人。
R0 > 1 疫情扩散，R0 < 1 疫情消退。
""")


