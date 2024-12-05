import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, time
import json

def main():
    st.sidebar.title("Streamlit学習アプリ")
    st.sidebar.markdown("""
    このアプリケーションは、Streamlitの主要な機能を学ぶためのチュートリアルです。
    左のメニューから学びたい機能を選択してください。
    """)
    
    page = st.sidebar.selectbox(
        "学習したい機能を選択してください",
        ["はじめに", "基本入力要素", "データ表示機能", "グラフ作成", "レイアウトオプション", "インタラクティブ機能"]
    )
    
    if page == "はじめに":
        show_introduction()
    elif page == "基本入力要素":
        show_basic_elements()
    elif page == "データ表示機能":
        show_data_display()
    elif page == "グラフ作成":
        show_graphs()
    elif page == "レイアウトオプション":
        show_layout_options()
    elif page == "インタラクティブ機能":
        show_interactive_features()

def show_introduction():
    st.title("Streamlitチュートリアル")
    
    st.markdown("""
    ### Streamlitとは？
    Streamlitは、データサイエンスのためのWebアプリケーションを簡単に作成できるPythonライブラリです。
    
    ### このチュートリアルの使い方
    1. 左サイドバーのメニューから学びたい機能を選択
    2. 各機能の説明を読み、実際に操作を試してみる
    3. サンプルコードを参考に、自分のアプリケーションを作成
    
    ### 主な機能カテゴリ
    1. **基本入力要素**: テキスト入力、数値入力、選択ボックスなど
    2. **データ表示機能**: テーブル、データフレーム、メトリクスの表示
    3. **グラフ作成**: 様々な種類のグラフ作成方法
    4. **レイアウトオプション**: 画面レイアウトのカスタマイズ
    5. **インタラクティブ機能**: フォーム、ファイルアップロードなど
    
    ### 準備するもの
    ```bash
    pip install streamlit pandas numpy plotly
    ```
    """)

def show_basic_elements():
    st.title("基本入力要素")
    
    with st.expander("基本入力要素について"):
        st.markdown("""
        基本入力要素は、ユーザーからの入力を受け取るための基本的なUIコンポーネントです。
        フォームやダッシュボードを作成する際の基礎となります。
        """)
    
    # テキスト入力
    st.header("1. テキスト入力")
    with st.expander("テキスト入力の説明"):
        st.markdown("""
        **使用方法**
        ```python
        text = st.text_input("ラベル", "デフォルト値")
        ```
        
        **主な用途**
        - ユーザー名の入力
        - 検索キーワードの入力
        - 短いテキストの入力
        """)
    
    text_input = st.text_input("あなたの名前を入力してください")
    if text_input:
        st.success(f"こんにちは、{text_input}さん！")
    
    # 数値入力
    st.header("2. 数値入力")
    with st.expander("数値入力の説明"):
        st.markdown("""
        **使用方法**
        ```python
        number = st.number_input("ラベル", min_value=最小値, max_value=最大値, value=デフォルト値)
        ```
        
        **主な用途**
        - 年齢の入力
        - 金額の入力
        - 数量の指定
        
        **実践例題**
        商品の個数と単価から合計金額を計算してみましょう。
        """)
    
    quantity = st.number_input("商品の個数", 1, 100, 1)
    price = st.number_input("単価（円）", 1, 10000, 100)
    total = quantity * price
    st.write(f"合計金額: {total:,}円")
    
    # スライダー
    st.header("3. スライダー")
    with st.expander("スライダーの説明"):
        st.markdown("""
        **使用方法**
        ```python
        value = st.slider("ラベル", min_value, max_value, default_value)
        ```
        
        **主な用途**
        - 範囲の選択
        - 値の調整
        - フィルタリング
        
        **実践例題**
        スライダーを使って、円の大きさを調整してみましょう。
        """)
    
    radius = st.slider("円の半径", 10, 100, 50)
    fig = go.Figure(go.Scatter(
        x=[0],
        y=[0],
        mode='markers',
        marker=dict(size=radius, color='blue')
    ))
    fig.update_layout(width=400, height=400)
    st.plotly_chart(fig)
    
    # 以下、他の基本要素も同様のパターンで実装
    # 各要素ごとに:
    # 1. 要素の説明
    # 2. コードサンプル
    # 3. 実践例題
    # 4. 実際の動作確認

def show_data_display():
    st.title("データ表示機能")
    
    with st.expander("データ表示機能について"):
        st.markdown("""
        データ表示機能は、データフレームやテーブル、メトリクスなどを表示するための機能群です。
        データ分析結果やダッシュボードの作成に欠かせません。
        """)
    
    # サンプルデータの作成
    df = pd.DataFrame({
        '商品名': ['商品A', '商品B', '商品C', '商品D'],
        '価格': [1000, 2000, 1500, 3000],
        '在庫': [50, 30, 40, 20],
        'カテゴリ': ['食品', '家電', '食品', '家電']
    })
    
    # データフレーム表示
    st.header("1. データフレーム表示")
    with st.expander("データフレーム表示の説明"):
        st.markdown("""
        **使用方法**
        ```python
        st.dataframe(df)  # インタラクティブな表示
        st.table(df)      # 静的な表示
        ```
        
        **主な特徴**
        - ソート機能
        - スクロール機能
        - 列幅の調整
        
        **実践例題**
        以下の商品データベースを操作してみましょう。
        - 列をクリックしてソート
        - スクロールして全データを確認
        """)
    
    st.dataframe(df)
    
    # メトリクス表示
    st.header("2. メトリクス表示")
    with st.expander("メトリクス表示の説明"):
        st.markdown("""
        **使用方法**
        ```python
        st.metric(label="ラベル", value="値", delta="変化量")
        ```
        
        **主な用途**
        - KPIの表示
        - 変化量の表示
        - 重要指標の強調
        
        **実践例題**
        商品の在庫状況をメトリクスで表示してみましょう。
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("総在庫数", f"{df['在庫'].sum()}個", "5")
    with col2:
        st.metric("平均価格", f"￥{df['価格'].mean():,.0f}", "-100")

def show_graphs():
    st.title("グラフ作成")
    
    with st.expander("グラフ作成について"):
        st.markdown("""
        Streamlitでは、Plotlyを使用して様々な種類のグラフを作成できます。
        データの可視化は、分析結果を効果的に伝えるために重要です。
        """)
    
    # サンプルデータの作成
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    sales = np.random.randint(100, 1000, size=len(dates))
    df = pd.DataFrame({
        '日付': dates,
        '売上': sales,
        '利益': sales * 0.3
    })
    
    # 折れ線グラフ
    st.header("1. 折れ線グラフ")
    with st.expander("折れ線グラフの説明"):
        st.markdown("""
        **使用方法**
        ```python
        fig = px.line(df, x='x軸', y='y軸')
        st.plotly_chart(fig)
        ```
        
        **主な用途**
        - 時系列データの表示
        - トレンドの可視化
        - 複数系列の比較
        
        **実践例題**
        月次の売上と利益の推移を表示してみましょう。
        """)
    
    fig_line = px.line(df, x='日付', y=['売上', '利益'], title='月次売上と利益の推移')
    st.plotly_chart(fig_line)
    
    # 以下、他のグラフタイプも同様に実装
    # 各グラフタイプごとに:
    # 1. 説明
    # 2. コードサンプル
    # 3. 実践例題
    # 4. 実際の動作確認

def show_layout_options():
    st.title("レイアウトオプション")
    
    with st.expander("レイアウトオプションについて"):
        st.markdown("""
        レイアウトオプションを使用することで、アプリケーションの見た目を整理し、
        ユーザーにとって使いやすいインターフェースを作成できます。
        """)
    
    # カラムレイアウト
    st.header("1. カラムレイアウト")
    with st.expander("カラムレイアウトの説明"):
        st.markdown("""
        **使用方法**
        ```python
        col1, col2 = st.columns(2)
        with col1:
            st.write("左カラムの内容")
        with col2:
            st.write("右カラムの内容")
        ```
        
        **主な用途**
        - 横並びのレイアウト
        - ダッシュボードの作成
        - 比較表示
        
        **実践例題**
        2つのグラフを横に並べて表示してみましょう。
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("左側のグラフ")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
        st.line_chart(chart_data)
    with col2:
        st.write("右側のグラフ")
        st.bar_chart(chart_data)

def show_interactive_features():
    st.title("インタラクティブ機能")
    
    with st.expander("インタラクティブ機能について"):
        st.markdown("""
        インタラクティブ機能を使用することで、ユーザーとのやり取りを実現し、
        動的なアプリケーションを作成できます。
        """)
    
    # フォーム
    st.header("1. フォーム")
    with st.expander("フォームの説明"):
        st.markdown("""
        **使用方法**
        ```python
        with st.form("form_name"):
            input_value = st.text_input("入力")
            submitted = st.form_submit_button("送信")
        ```
        
        **主な用途**
        - ユーザー登録
        - データ入力
        - 設定画面
        
        **実践例題**
        簡単な問い合わせフォームを作成してみましょう。
        """)
    
    with st.form("contact_form"):
        name = st.text_input("お名前")
        email = st.text_input("メールアドレス")
        message = st.text_area("メッセージ")
        submitted = st.form_submit_button("送信")
        if submitted:
            st.success("送信されました！")
            st.json({
                "name": name,
                "email": email,
                "message": message
            })

if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit学習アプリ",
        page_icon="📚",
        layout="wide"
    )
    main()