import streamlit as st

# config
# st.set_page_config(layout="wide")

# headings
title = "blog writer"
st.header(":book: blog prompt generator")
st.markdown("generate blog prompts for [chatgptplus](https://chat.openai.com/)")

# user inputs on sidebar
st.sidebar.title("設定")
roles = [
    '優秀なビジネスコンサルタント',
    '優秀なデータサイエンティスト',
    '優秀な弁護士',
    '優秀な公認会計士',
    '優秀な税理士'
    ]
role = st.sidebar.selectbox('role',roles)
theme = st.sidebar.text_area("テーマ",value="プロジェクトマネジメント",height=50)
title = st.sidebar.text_area("タイトル",value=f"{theme}の概要",height=50)
toc_sample = f'''\
- {theme}の概要
- {theme}の重要性
- {theme}の具体例
- 当社のサービス
'''
toc = st.sidebar.text_area("目次",value=toc_sample,height=200)

prompt = f'''あなたは{role}です。あなたの専門知識を活かして、プロフェッショナルな長文のブログ記事を書いて下さい。作成にあたっては、具体性を持って、読者に価値を提供することを心がけてください。

テーマは「{theme}」です。

タイトルは「{title}」です。

目次は以下のとおりです。

{toc}
'''

prompt_img = '''\
このブログ記事にふさわしいアイキャッチ画像を生成して下さい。
画像サイズは「600px」×「400px」で作成ください。
シンプルかつフラットで、ビジネスにふさわしい画風にしてください。
'''

# main body
with st.container():
    st.text_area('prompt',prompt,height=400)
    st.text_area('prompt_img',prompt_img,height=200)


# st.markdown("Powered by [LOGIT group](https://consulting.logit.jp/)")