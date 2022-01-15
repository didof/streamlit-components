import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component", url="http://localhost:3000"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "vue-components/build")
    _component_func = components.declare_component("my_component", path=build_dir)


def my_component(tabs, height, key=None):
    component_value = _component_func(
        tabs=tabs, height=height, key=key, default=tabs[0]
    )
    return component_value


if not _RELEASE:
    import streamlit as st

    selected_tab = my_component(tabs=["home", "about"], height=3)

    st.write(selected_tab)
