import unittest
from htmlnodes import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_a(self):
        node = HTMLNode('a',href='https://example.com',target='_blank')
        self.assertEqual(str(node),'''HTMLNode(a,None,None,{'href': 'https://example.com', 'target': '_blank'})''')
        self.assertEqual(node.props_to_html(),' href="https://example.com" target="_blank"')

    def test_div(self):
        node = HTMLNode('div',id='fu')
        self.assertEqual(str(node),'''HTMLNode(div,None,None,{'id': 'fu'})''')

    def test_empty_para(self):
        node = HTMLNode('p')
        self.assertEqual(str(node),'HTMLNode(p,None,None,{})')

    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

    def test_leaf_to_html_a(self):
        node = LeafNode('a','Click Here!',href='https://example.com')
        self.assertEqual(node.to_html(),'<a href="https://example.com">Click Here!</a>')

    def test_leaf_to_html_no_value(self):
        err = None
        try:
            node = LeafNode('p')
        except Exception as e:
            err = e
        self.assertIsInstance(err,ValueError)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )