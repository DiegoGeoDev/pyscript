from utils import toggleColors


result_py_el = Element("result-py").element
result_py_el.innerHTML = "PYTHON"

result_js_el = Element("result-js").element
result_js_el.innerHTML = "JAVASCRIPT"


def toggleColorsHandler(*args):
    toggleColors(result_py_el, result_js_el)
