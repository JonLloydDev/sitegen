# Core modules
import unittest
import traceback

# Local modules
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node,node2)

    def test_neq1(self):
        node  = TextNode('Test text', TextType.NORMAL)
        node2 = TextNode('Test text', TextType.BOLD)
        self.assertNotEqual(node,node2)

    def testneq2(self):
        node  = TextNode('Test text', TextType.NORMAL)
        node2 = TextNode('Test test', TextType.NORMAL)
        self.assertNotEqual(node,node2)

    def test_text(self):
        node_text = str(TextNode('Test text', TextType.LINK,'https://example.com'))
        text      = 'TextNode(Test text,TextType.LINK,https://example.com)'
        self.assertEqual(node_text,text)

    def test_text_err(self):
        err = None
        try:
            node = TextNode(4,TextType.NORMAL)
        except Exception as e:
            err = e
        self.assertIsInstance(err,TypeError)
        self.assertEqual(str(err),'Expected str; got int')

    def test_type_err(self):
        err = None
        try:
            node = TextNode('Text test','NORMAL')
        except Exception as e:
            err = e
        self.assertIsInstance(err,TypeError)
        self.assertEqual(str(err),'Expected TextType; got str')

    def test_url_err(self):
        err = None
        try:
            node = TextNode('Text test',TextType.LINK,4)
        except Exception as e:
            err = e
        self.assertIsInstance(err,TypeError)
        self.assertEqual(str(err),'Expected str or None; got int')

    def test_link_html(self):
        node = TextNode('Click here!',TextType.LINK,'https://example.com')
        self.assertEqual(node.to_html(),'<a href="https://example.com">Click here!</a>')

    def test_text_html(self):
        node = TextNode('Regular text goes here',TextType.NORMAL)
        self.assertEqual(node.to_html(),'Regular text goes here')

    def test_image_html(self):
        node = TextNode("I'm an image!",TextType.IMAGE,'https://example.com/example.png')
        self.assertEqual(node.to_html(),'''<img src="https://example.com/example.png" alt="I'm an image!"></img>''')

    def test_bold_html(self):
        node = TextNode('BOLD TEXT',TextType.BOLD)
        self.assertEqual(node.to_html(),'<b>BOLD TEXT</b>')

    def text_italic_html(self):
        node = TextNode('/italic text/',TextType.ITALIC)
        self.assertEqual(node.to_html(),r'<i>/italic text/</i>')
        

if __name__ == '__main__':
    unittest.main()