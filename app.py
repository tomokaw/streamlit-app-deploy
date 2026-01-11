import sys
import platform

try:
    import streamlit as st
except Exception as e:
    raise SystemExit("Streamlit is required to run this app: " + str(e))

try:
    from importlib.metadata import distributions
except Exception:
    distributions = None


st.title("env_practice Streamlit App")
st.write("Python:", sys.executable)
st.write("Platform:", platform.platform())

st.subheader("langchain status")
try:
    import langchain
    st.write("langchain", getattr(langchain, "__version__", "unknown"))
except Exception as e:
    st.write("langchain import error:", type(e).__name__, str(e))

st.subheader("Installed packages (top 50)")
if distributions is not None:
    dists = sorted(distributions(), key=lambda d: (d.metadata.get('Name') or '').lower())
    for d in dists[:50]:
        name = d.metadata.get('Name') or d.metadata.get('Summary') or str(d)
        st.write(f"{name} {d.version}")
else:
    try:
        import pkg_resources
        for i, dist in enumerate(sorted(pkg_resources.working_set, key=lambda d: d.project_name.lower())):
            if i >= 50:
                break
            st.write(f"{dist.project_name} {dist.version}")
    except Exception as e:
        st.write("Could not list packages:", e)
