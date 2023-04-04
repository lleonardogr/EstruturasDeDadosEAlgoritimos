class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()
        return self.children[path_part]


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts, handler):
        current_node = self.root
        for part in path_parts:
            current_node = current_node.insert(part)
        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        return current_node.handler

class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler or "404 Not Found"

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        path_parts = path.strip("/").split("/")
        return [part for part in path_parts if part]
    
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one