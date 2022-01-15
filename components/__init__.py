import os
import streamlit.components.v1 as components

_RELEASE = False

VITE_URL = "http://localhost:3000"

# config = {
#     "hello_author": "/",
#     "layout": "/layout",
#     "view": "/layout/view",
# }

config = {
    "hello_author": "/",
}

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def retrieve_components_dev(base_url, config):
    output = {}

    def make(component):
        def exec(
            key=None,
            **kwargs,
        ):
            return component(**kwargs, key=key)

        return exec

    for [name, path] in config.items():
        component = components.declare_component(
            name,
            url=base_url + path,
        )

        output[name] = make(component)

    return dotdict(output)


def retrieve_components(config):
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "vue-components/dist")

    output = {}

    def make(component):
        def exec(
            key=None,
            **kwargs,
        ):
            return component(**kwargs, key=key)

        return exec

    for [name, path] in config.items():
        component = components.declare_component(
            name,
            path=build_dir + path,
        )

        output[name] = make(component)

    return dotdict(output)


if not _RELEASE:
    c = retrieve_components_dev(VITE_URL, config)
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "vue-components/build")
    _component_func = components.declare_component("my_component", path=build_dir)

if not _RELEASE:
    import streamlit as st

    c.hello_author()

    # selected_tab = c.layout(
    #     default="home",
    #     views=[c.view(name="home"), c.view(name="about", key=1)],
    # )

    # st.write(selected_tab)
