import streamlit as st
import time
from agents import (
    build_reader_agent,
    build_search_agent,
    get_writer_chain,
    get_critic_chain
)

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind · AI Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Session state init ────────────────────────────────────────────────────────
for key in ("results", "running", "done"):
    if key not in st.session_state:
        st.session_state[key] = {} if key == "results" else False


# ── UI Header ────────────────────────────────────────────────────────────────
st.title("🔬 ResearchMind")
st.caption("Multi-Agent AI Research System (Search → Read → Write → Critic)")


# ── Input Section ────────────────────────────────────────────────────────────
topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Latest advancements in AI agents"
)

run_btn = st.button("⚡ Run Research Pipeline")


# ── Trigger Pipeline ─────────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.rerun()


# ── Pipeline Execution ───────────────────────────────────────────────────────
if st.session_state.running and not st.session_state.done:

    results = {}
    topic_val = topic

    # 🔍 Step 1: Search
    with st.spinner("🔍 Searching for information..."):
        search_agent = build_search_agent()
        sr = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
        })
        results["search"] = sr["messages"][-1].content
        st.session_state.results = dict(results)

    # 🌐 Step 2: Reader
    with st.spinner("📄 Extracting detailed content..."):
        reader_agent = build_reader_agent()
        rr = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic_val}', "
                f"pick the most relevant URL and scrape it.\n\n"
                f"Search Results:\n{results['search'][:800]}"
            )]
        })
        results["reader"] = rr["messages"][-1].content
        st.session_state.results = dict(results)

    # ✍️ Step 3: Writer
    with st.spinner("✍️ Writing research report..."):
        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED CONTENT:\n{results['reader']}"
        )

        writer_chain = get_writer_chain()

        results["writer"] = writer_chain.invoke({
            "topic": topic_val,
            "research": research_combined
        })
        st.session_state.results = dict(results)

    # 🧐 Step 4: Critic
    with st.spinner("🧐 Reviewing report..."):
        critic_chain = get_critic_chain()

        results["critic"] = critic_chain.invoke({
            "report": results["writer"]
        })
        st.session_state.results = dict(results)

    st.session_state.running = False
    st.session_state.done = True
    st.rerun()


# ── Display Results ──────────────────────────────────────────────────────────
r = st.session_state.results

if r:

    st.divider()

    if "search" in r:
        with st.expander("🔍 Search Results"):
            st.write(r["search"])

    if "reader" in r:
        with st.expander("📄 Scraped Content"):
            st.write(r["reader"])

    if "writer" in r:
        st.subheader("📝 Final Research Report")
        st.markdown(r["writer"])

        st.download_button(
            label="⬇ Download Report",
            data=r["writer"],
            file_name=f"report_{int(time.time())}.md",
            mime="text/markdown",
        )

    if "critic" in r:
        st.subheader("🧐 Critic Feedback")
        st.markdown(r["critic"])
