import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    # _component_func = components.declare_component(
    #     "my_component", url="http://localhost:3000"
    # )
    _component_hello_author_func = components.declare_component(
        "didof_hello_author", url="http://localhost:3000/"
    )
    _component_header_func = components.declare_component(
        "didof_header", url="http://localhost:3000/header"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "vue-components/build")
    _component_func = components.declare_component("my_component", path=build_dir)


def didof_hello_author(key=None):
    return _component_hello_author_func()


def didof_header(tabs, key=None):
    return _component_header_func(tabs=tabs, key=key, default=tabs[0])


if not _RELEASE:
    import streamlit as st

    didof_hello_author()

    selected_tab = didof_header(tabs=["home", "about"])
    st.write(selected_tab)
