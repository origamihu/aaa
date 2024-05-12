import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
import warnings
import time
#streamlit run fenye.py
#pipreqs fenye./ --encoding=utf-8 --force


code_page1 = """

st.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;制冷热泵循环演示实验")
st.write(" ")
st.markdown("一、实验目的")
st.write("1．熟悉制冷和热泵循环系统工作原理，观察制冷工质的蒸发、冷凝过程和现象。")
st.write("2．熟悉制冷(热泵)循环系统的操作、调节方法。 ")
st.write("3．进行制冷、热泵循环系统粗略的热力计算。 ")
st.markdown("二、实验原理和步骤 ")
st.write("实验装置由全封闭压缩机、换热器 1、换热器 2、浮子节流阀、四通换向阀及管路等组成制冷（热泵）循环系统;由转子流量计及换热器内盘管等组成水系统；还设有温度、压力、电流、电压等测量仪表。 ")
#st.write("由转子流量计及换热器内盘管等组成水系统；还设有温度、压力、电流、电压等测量仪表。 ")
st.write("装置原理示意图如图 1 和图 2 所示。 ")
st.image('11.png')
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图 1 制冷（热泵）循环演示装置原理图 ")
st.image('22.png')
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图 2 制冷剂流向改变流程图 ")
st.write("当系统作制冷（热泵）循环时，换热器 1 为蒸发器（冷凝器），换热器 2 为冷凝器（蒸发器）。 ")
st.write(" ")
st.write("1．制冷循环 ")
st.write("1)将四通换向阀调至“制冷”位置，1，2 关闭，3，4 开。 ")
st.write("2)打开连接装置的供水阀门，利用转子流量计阀门适当凋节蒸发器凝器水流量。")
st.write("3)开启压缩机，观察工质的冷凝、蒸发过程及其现象。")
st.write("4)待系统运行稳定后，即可观察冷凝器和蒸发器的进，出口温度及水流量等参数。 ")
st.write(" ")
st.write("2．热泵循环 ")
st.write("1)将四通换向阀调至“热泵”位置，1，2 开，3，4 关闭。 ")
st.write("2)类似上述 2)、3)、4)步骤进行操作和记录。 ")
"""
code_page2 ="""
st.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;制冷热泵循环演示实验")
st.write('')
t0 = 20.0
Cp = 4.868
G1 = 1.0
V = float(220)
A = float(1)
x = []
inlet1 = []
inlet2 = []
outlet1 = []
outlet2 = []
a = 0.01
b = 0.1
run_time = 200
st.write('')

ii = st.empty()
ii.image('1.jpg', width=600)
start_button1 = st.button('电源开关')
start_button2 = st.button('转换阀门状态')

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=1.2)  # 调整子图之间的距离
line11, = ax1.plot([], [], label='inlet1')
line12, = ax1.plot([], [], label='outlet1')
line21, = ax2.plot([], [], label='inlet2')
line22, = ax2.plot([], [], label='outlet2')
ax1.set_title('heat exchanger 1')
ax1.set_xlabel('running time(s)')
ax1.set_ylabel('temperature variation(℃)')
ax1.legend()
ax2.set_title('heat exchanger 2')
ax2.set_xlabel('running time(s)')
ax2.set_ylabel('temperature variation(℃)')
ax2.legend()
chart = st.pyplot(fig)

annotation_inlet1 = ax1.annotate('', (0, 0), textcoords="offset points", xytext=(0, 10), ha='center')  # 创建一个空的注释
annotation_outlet1 = ax1.annotate('', (0, 0), textcoords="offset points", xytext=(0, 10), ha='center')  # 创建一个空的注释
annotation_inlet2 = ax2.annotate('', (0, 0), textcoords="offset points", xytext=(0, 10), ha='center')  # 创建一个空的注释
annotation_outlet2 = ax2.annotate('', (0, 0), textcoords="offset points", xytext=(0, 10), ha='center')  # 创建一个空的注释

if start_button1 and not start_button2:
    st.write('设备开始运行,记录换热器1和换热器2的出入口温度变化')
    t = 0

    while t < 200:

        ii.image('aaa.gif')
        Q1 = 1.5 * 0.98 * V * A / 1000
        y1 = t0 - Q1 / (G1 * Cp)        # 1出口温度
        Q2 = 2.5 * 0.98 * V * A / 1000
        y2 = t0 + Q2 / (G1 * Cp)        # 2出口温度
        yy = (y1 + y2) / 2 - 20              # 汇合温度与环境变化量

        inlet1_temp = t0 - 20
        inlet2_temp = t0 - 20
        outlet1_temp = y1 - 20
        outlet2_temp = y2 - 20
        x.append(t)
        inlet1.append(inlet1_temp)
        inlet2.append(inlet2_temp)
        outlet1.append(outlet1_temp)
        outlet2.append(outlet2_temp)
        t0 = 20 + (1-a * np.exp(b * yy)) * yy

        line11.set_data(x, inlet1)
        line12.set_data(x, outlet1)
        line21.set_data(x, inlet2)
        line22.set_data(x, outlet2)

        # 移除旧的注释并添加新的注释
        annotation_inlet1.remove()
        annotation_outlet1.remove()
        annotation_inlet2.remove()
        annotation_outlet2.remove()

        # 在创建注释时，根据当前的y值来决定注释的位置
        offset = 20  # 注释与曲线的垂直距离

        # 对于inlet1和outlet1
        if inlet1_temp < outlet1_temp:
            annotation_inlet1 = ax1.annotate(f'inlet1: {inlet1_temp:.2f}', (t, inlet1_temp), textcoords="offset points",
                                             xytext=(0, -offset), ha='center')
            annotation_outlet1 = ax1.annotate(f'outlet1: {outlet1_temp:.2f}', (t, outlet1_temp),
                                              textcoords="offset points", xytext=(0, offset), ha='center')
        else:
            annotation_inlet1 = ax1.annotate(f'inlet1: {inlet1_temp:.2f}', (t, inlet1_temp), textcoords="offset points",
                                             xytext=(0, offset), ha='center')
            annotation_outlet1 = ax1.annotate(f'outlet1: {outlet1_temp:.2f}', (t, outlet1_temp),
                                              textcoords="offset points", xytext=(0, -offset), ha='center')

        # 对于inlet2和outlet2
        if inlet2_temp < outlet2_temp:
            annotation_inlet2 = ax2.annotate(f'inlet2: {inlet2_temp:.2f}', (t, inlet2_temp), textcoords="offset points",
                                             xytext=(0, -offset), ha='center')
            annotation_outlet2 = ax2.annotate(f'outlet2: {outlet2_temp:.2f}', (t, outlet2_temp),
                                              textcoords="offset points", xytext=(0, offset), ha='center')
        else:
            annotation_inlet2 = ax2.annotate(f'inlet2: {inlet2_temp:.2f}', (t, inlet2_temp), textcoords="offset points",
                                             xytext=(0, offset), ha='center')
            annotation_outlet2 = ax2.annotate(f'outlet2: {outlet2_temp:.2f}', (t, outlet2_temp),
                                              textcoords="offset points", xytext=(0, -offset), ha='center')

        ax1.set_xlim(0, max(x))
        ax1.set_ylim(min(min(inlet1), min(outlet1)), max(max(inlet1), max(outlet1)))
        ax2.set_xlim(0, max(x))
        ax2.set_ylim(min(min(inlet2), min(outlet2)), max(max(inlet2), max(outlet2)))

        chart.pyplot(fig)

        t += 1
        time.sleep(1)
    ii.image('aaa.gif')
if start_button2:
    st.write('阀门状态已改变,继续记录换热器1和换热器2的出入口温度变化')
    t = 200
    t0 = 21.697749605077938
    x = []  # 重新初始化x列表
    inlet1 = []  # 重新初始化inlet1列表
    inlet2 = []  # 重新初始化inlet2列表
    outlet1 = []  # 重新初始化outlet1列表
    outlet2 = []  # 重新初始化outlet2列表
    while t < 400:
        ii.image('a.gif')
        Q1 = 2.5 * 0.98 * V * A / 1000
        y1 = t0 + Q1 / (G1 * Cp)  # 1出口温度
        Q2 = 1.5 * 0.98 * V * A / 1000
        y2 = t0 - Q2 / (G1 * Cp)  # 2出口温度
        yy = (y1 + y2) / 2 - 20  # 汇合温度与环境变化量
        inlet1_temp = t0 - 20
        inlet2_temp = t0 - 20
        outlet1_temp = y1 - 20
        outlet2_temp = y2 - 20
        x.append(t)
        inlet1.append(inlet1_temp)
        inlet2.append(inlet2_temp)
        outlet1.append(outlet1_temp)
        outlet2.append(outlet2_temp)
        t0 = 20 + (1 - a * np.exp(b * yy)) * yy

        line11.set_data(x, inlet1)
        line12.set_data(x, outlet1)
        line21.set_data(x, inlet2)
        line22.set_data(x, outlet2)
        # 移除旧的注释并添加新的注释
        annotation_inlet1.remove()
        annotation_outlet1.remove()
        annotation_inlet2.remove()
        annotation_outlet2.remove()

        # 在创建注释时，根据当前的y值来决定注释的位置
        offset = 20  # 注释与曲线的垂直距离

        # 对于inlet1和outlet1
        if inlet1_temp < outlet1_temp:
            annotation_inlet1 = ax1.annotate(f'inlet1: {inlet1_temp:.2f}', (t, inlet1_temp), textcoords="offset points",
                                             xytext=(0, -offset), ha='center')
            annotation_outlet1 = ax1.annotate(f'outlet1: {outlet1_temp:.2f}', (t, outlet1_temp),
                                              textcoords="offset points", xytext=(0, offset), ha='center')
        else:
            annotation_inlet1 = ax1.annotate(f'inlet1: {inlet1_temp:.2f}', (t, inlet1_temp), textcoords="offset points",
                                             xytext=(0, offset), ha='center')
            annotation_outlet1 = ax1.annotate(f'outlet1: {outlet1_temp:.2f}', (t, outlet1_temp),
                                              textcoords="offset points", xytext=(0, -offset), ha='center')

        # 对于inlet2和outlet2
        if inlet2_temp < outlet2_temp:
            annotation_inlet2 = ax2.annotate(f'inlet2: {inlet2_temp:.2f}', (t, inlet2_temp), textcoords="offset points",
                                             xytext=(0, -offset), ha='center')
            annotation_outlet2 = ax2.annotate(f'outlet2: {outlet2_temp:.2f}', (t, outlet2_temp),
                                              textcoords="offset points", xytext=(0, offset), ha='center')
        else:
            annotation_inlet2 = ax2.annotate(f'inlet2: {inlet2_temp:.2f}', (t, inlet2_temp), textcoords="offset points",
                                             xytext=(0, offset), ha='center')
            annotation_outlet2 = ax2.annotate(f'outlet2: {outlet2_temp:.2f}', (t, outlet2_temp),
                                              textcoords="offset points", xytext=(0, -offset), ha='center')

        ax1.set_xlim(200, t)  # 从200到当前的t
        ax1.set_ylim(min(inlet1), max(outlet1))
        ax2.set_xlim(200, t)  # 从200到当前的t
        ax2.set_ylim(min(outlet2), max(inlet2))

        chart.pyplot(fig)

        t += 1
        time.sleep(1)
"""
pages = {
    "实验原理": [code_page1],
    "实验仪器": [code_page2],
    #"": ["Content of Page 3"]
}
selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
exec(pages[selected_page][0])
