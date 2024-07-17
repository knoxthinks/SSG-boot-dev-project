import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        # Test case with multiple props
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
        # Test case with empty props
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')
        
        # Test case with a single prop
        node = HTMLNode(props={"class": "button"})
        self.assertEqual(node.props_to_html(), ' class="button"')
        
    # You might want to consider additional edge cases or different types of props

if __name__ == '__main__':
    unittest.main()