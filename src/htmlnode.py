# class HTMLNode:
#     def __init__(self, tag=None, value=None, children=None, props=None):
#         self.tag = tag
#         self.value = value
#         self.children = children
#         self.props = props
    
#     def to_html(self):
#         raise NotImplementedError("error")
    
#     def props_to_html(self):
#         props_str = ""
#         if self.props:
#             for key, value in self.props.items():
#                 props_str += f' {key}="{value}"'
#         return props_str
    
#     def __repr__(self):
#         return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

# class LeafNode(HTMLNode):
#     def __init__(self, tag=None, value=None, props=None):
#         if value is None:
#             raise ValueError("LeafNode must have a value")
#         super().__init__(tag, value, None, props)
#     def to_html(self):
#         if self.value is None: 
#             raise ValueError("LeafNode must have a value")
        
#         if self.tag is None:
#             return self.value
#         else:
#             props_string = self.props_to_html()
#             return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
