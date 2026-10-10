# SIR 传染病模型交互可视化

基于 Streamlit + Plotly 的 SIR 模型交互 demo。

## 功能

- 调节感染率 β、恢复率 γ、总人口 N
- 实时 SIR 曲线图
- S-I 相图
- 显示 R0、感染峰值、峰值时间

## 运行方法

pip install -r requirements.txt
streamlit run app.py

## 模型说明

SIR 模型把总人口分成三类：
- S：易感者
- I：感染者
- R：康复者

基本传染数 R0 = β / γ。
R0 > 1 疫情扩散，R0 < 1 疫情消退。
