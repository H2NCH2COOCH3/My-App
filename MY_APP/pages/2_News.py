import streamlit as st
import feedparser

st.header("📰 Tin tức")

tabA, tabB, tabC = st.tabs([
    "💥 VnExpress",
    "💰 Giá vàng",
    "⚽ Thể thao"
])

with tabA:

        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")

        for entry in feed.entries[:5]:

            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

with tabB:

        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")

        gold_news = [
            entry for entry in feed.entries
            if "vàng" in entry.title.lower()
        ]

        if gold_news:
            for entry in gold_news[:5]:

                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)

        else:

            st.warning("Không tìm thấy tin giá vàng")

with tabC:

        feed = feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")

        for entry in feed.entries[:10]:

            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)