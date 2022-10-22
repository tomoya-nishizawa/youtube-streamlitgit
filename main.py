from asyncore import write
import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time



st.title('Streamlit 超入門')

#st.write('DataFrame')


st.write('プログレスバーの表示')
'Strat!!'

latest_iteration = st.empty()
bar = st.progress(0)
#progress(0)ここは0か0.0

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    #{i+1}iが0からどんどん1足されていく
    bar.progress(i + 1)
    #barの部分で進捗を表している
    time.sleep(0.1)
    #()の中の秒数でiに１ずつ足していく

'Done!!!!!!!!'


left_column, right_column = st.columns(2)
#button = left_column.button('右カラムに文字表示')
button = left_column.button('ゴリラの正式名称はなんでしょう')
#if button:
#    right_column.write('ここは右カラム')
#ゴリラの正式名称はなんでしょう これがクリックされたら右カラムを表示する（今回で言うと回答を表示させる）
if button:
    right_column.write('ゴリラゴリラゴリラ')



expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

#text = st..text_input('あなたの趣味を教えてください。')    
#condition = st..slider('あなたの今の調子は？', 0, 100, 50)
#0, 100, 50　→ 最小値、最大値、スタートのデフォルトの値
#
#'あなたの趣味：',text,
#'コンディション:', condition



#text = st.sidebar.text_input('あなたの趣味を教えてください。')    
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#0, 100, 50　→ 最小値、最大値、スタートのデフォルトの値
#
#'あなたの趣味：',text,
#'コンディション:', condition


#text = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味：',text, 
#    
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#0, 100, 50　→ 最小値、最大値、スタートのデフォルトの値
#'コンディション:', condition

#st.write('Display Image')

#option = st.selectbox(
#    'あなたが好きな数字を教えてください、',
#    list(range(1, 11))
#)
#
#'あなたの好きな数字は、', option, 'です。'


#チェックボックスがチェックされてる同亜kで画像を表示するか決める
#if st.checkbox('Show Image'):
#    img = Image.open('sample.jpeg')
#    st.image(img, caption='kamakieri', use_column_width=True)

#img = Image.open('sample.jpeg')
#st.image(img, caption='kamakieri', use_column_width=True)


#マップの描画
#lat 緯度
#lon 軽度
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)
#st.map(df)

#グラフの描画
#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c'])
#
#st.area_chart(df)


#表の描画
#df = pd.DataFrame({
    #'1列目': [1, 2, 3, 4],
    #'2列目': [10, 20, 30, 40]
#})

 

# bst.table(df.style.highlight_max(axis=0))

#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```

#"""


