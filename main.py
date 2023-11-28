import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトル
st.title('Streamlit チョー入門！')   


"# プログレス・バーの表示"

'## その１'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## テキストの表示!!!'


"マークダウンで書いてもOK！"

"""
**1. One**  
2. Two
3. *Three*
- Four
- Five

`テーブル形式`

|東京都|北区|豊島|
|--|--|--|
|東京都|港区|麻布|
|--|--|--|

"""   

'## その２'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## かわいいスタイルで。色文字、絵文字!!!'

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")   


'## その３'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## 動的なデータフレームや静的なテーブル!!!'

# データフレームを追加
st.write('DataFrame')

"## Data \n# Frame"

df = pd.DataFrame({
    '１列目': [1,2,3,4],
    '２列目': [10,20,30,40]
})

# st.write(df) #表のサイズ指定できない

# 縦横のサイズを指定できる！
#st.dataframe(df.style.highlight_max(axis=0)) # pandasのdfの機能

# Table:静的な表/何も動かせない
st.table(df.style.highlight_max(axis=0))


'## その４'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## さまざまなチャート!!!'


# グラフ用のデータ ランダム生成
df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)

# グラフ表示
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)


'## その５'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## マップ表示も!!!'

# マップ用のデータ ランダム生成
df_map = pd.DataFrame(
    np.random.rand(100,2) /[50,50] + [35.69, 139.70],
    columns = ['lat','lon']
)
if st.checkbox('地図を表示する'):
    st.map(df_map)


'## その６'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## イメージ表示も!!!'

# 画像を表示
st.write('Display Image')

if st.checkbox('画像を表示する'):
    img = Image.open('minami.webp')
    st.image(img, caption="浜辺美波のジョジョ加工",use_column_width=True)
    



'## その７'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## サイドバー、２カラム表示／エキスパンダー!!!'
# 「２カラム」にする

st.write("## Interactive Widgets")    
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


# エキスパンダー
expander = st.expander('お問い合わせ')
expander.write('問い合わせ内容を書く1')

expander1 = st.expander('お問い合わせ')
expander1.text_input("問い合わせ内容を書く2")



'## その８'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'## サイドバー!!!'


" ### セレクトボックス "
option = st.sidebar.selectbox(
    "あなたが好きな数字をおしえてください。",
    list(range(1,11))
)
st.write('あなたが好きな数字は、',option,'です。')


"### テキスト入力フォーム"
text = st.sidebar.text_input("あなたの趣味を教えてください。")
st.write('あなたの趣味は、',text,' です。')


"### スライダー"
condition = st.sidebar.slider('今の調子はどう？', 0,100,50)
st.write('ただいまのコンディションは ',condition,'くらいです。')
