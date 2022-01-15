import os
import streamlit.components.v1 as components
import types

_RELEASE = False

VITE_URL = "http://localhost:3000"

config = {
    "hello_author": "/",
    "header": "/header",
}


def retrieve_components(base_url, config):
    res = []

    def make(component):
        def exec(**kwargs):
            return component(**kwargs, key=None)

        return exec

    for [name, path] in config.items():
        component = components.declare_component(
            name,
            url=base_url + path,
        )

        res.append(make(component))

    return res


if not _RELEASE:
    c = retrieve_components(VITE_URL, config)
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "vue-components/build")
    _component_func = components.declare_component("my_component", path=build_dir)


# def didof_hello_author(key=None):
#     return _component_hello_author_func()


# def didof_header(tabs, key=None):
#     return _component_header_func(tabs=tabs, key=key, default=tabs[0])


if not _RELEASE:
    import streamlit as st

    hello_author = c[0]
    header = c[1]

    hello_author()

    tabs = ["home", "about"]

    selected_tab = header(tabs=tabs, default=tabs[0])
    st.write(selected_tab)

    # didof_hello_author()

    # selected_tab = didof_header(tabs=["home", "about"])
    # st.write(selected_tab)
