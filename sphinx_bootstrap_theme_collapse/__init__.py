"""A .. collapse:: directive for sphinx-bootstrap-theme."""

import os.path as op
from docutils import nodes
from docutils.parsers.rst.directives import flag

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset

this_dir = op.dirname(__file__)


HEADER = """
<div class="panel panel-{class_}">
<div class="panel-heading"><h4 class="panel-title">
<a data-toggle="collapse" href="#collapse_{id_}">{title}</a>
</h4></div>
<div id="collapse_{id_}" class="panel-collapse collapse{extra}">
<div class="panel-body">
"""
FOOTER = "</div></div></div>"


class CollapseNode(nodes.General, nodes.Element):
    """Our class."""

    def __init__(self, title, id_, extra, class_):
        self.options = dict(title=title, id_=id_, extra=extra, class_=class_)
        super().__init__()

    @staticmethod
    def visit_node(self, node):
        """Visit the node."""
        self.body.append(HEADER.format(**node.options))

    @staticmethod
    def depart_node(self, node):
        """Depart the node."""
        self.body.append(FOOTER)


KNOWN_CLASSES = ('default', 'primary', 'success', 'info', 'warning', 'danger')


def _check_class(class_):
    if class_ not in KNOWN_CLASSES:
        raise ValueError(':class: option %r must be one of %s'
                         % (class_, KNOWN_CLASSES))
    return class_


class CollapseDirective(SphinxDirective):
    """Collapse directive."""

    final_argument_whitespace = True
    optional_arguments = 2
    option_spec = {'open': flag,
                   'class': _check_class}
    has_content = True

    def run(self):
        """Parse."""
        env = self.state.document.settings.env
        self.assert_has_content()
        extra = _(' in' if 'open' in self.options else '')
        title = _(self.arguments[0])
        class_ = self.options.get('class', 'default')
        print(class_)
        id_ = env.new_serialno('Collapse')
        collapse_node = CollapseNode(title, id_, extra, class_)
        self.add_name(collapse_node)
        self.state.nested_parse(
            self.content, self.content_offset, collapse_node)
        return [collapse_node]


def setup(app):
    """Set up for Sphinx app."""
    app.add_directive('collapse', CollapseDirective)
    try:
        app.add_css_file('collapse.css')
    except AttributeError:
        app.add_stylesheet('collapse.css')
    try:
        app.add_js_file('collapse.js')
    except AttributeError:
        app.add_javascript('collapse.js')
    app.connect('build-finished', copy_asset_files)
    app.add_node(CollapseNode,
                 html=(CollapseNode.visit_node, CollapseNode.depart_node),
                 latex=(CollapseNode.visit_node, CollapseNode.depart_node),
                 text=(CollapseNode.visit_node, CollapseNode.depart_node))
    return dict(version='0.1', parallel_read_safe=True,
                parallel_write_safe=True)


def copy_asset_files(app, exc):
    """Copy static assets."""
    asset_files = ['collapse.css', 'collapse.js']
    if exc is None:  # build succeeded
        for path in asset_files:
            copy_asset(op.join(this_dir, path),
                       op.join(app.outdir, '_static'))
