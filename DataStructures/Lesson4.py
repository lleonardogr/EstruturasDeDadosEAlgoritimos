class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None:
        return None
    
    if user in group.get_users():
        return True

    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Normal Test Case
user1 = "User 1"
user2 = "User 2"
user3 = "User 3"

group1 = Group("Group 1")
group2 = Group("Group 2")
group3 = Group("Group 3")

group1.add_user(user1)
group2.add_user(user2)
group3.add_user(user3)

group1.add_group(group2)

assert is_user_in_group(user1, group1) == True
assert is_user_in_group(user2, group1) == True 
assert is_user_in_group(user3, group1) == False  # Deve retornar False

# Test Case 2
# Null Test Case
user_null = None
assert is_user_in_group(user_null, group1) == False

# Test Case 3
# many groups and users
def create_groups_and_users(num_groups):
    groups = [Group(f"Group {i}") for i in range(num_groups)]

    for i in range(num_groups - 1):
        groups[i].add_subgroup(groups[i + 1])

    return groups

def test_large_user_and_many_groups():
    large_user = "x" * 1000  # Um usuário grande com 1000 caracteres
    num_groups = 100  # Criando 100 grupos aninhados
    groups = create_groups_and_users(num_groups)

    groups[0].add_user(large_user)  # Adicionando o usuário grande ao primeiro grupo

    # Verificando se o usuário grande está no primeiro grupo e nos subgrupos
    for i in range(num_groups):
        assert is_user_in_group(large_user, groups[i]) == True, f"O usuário grande deve estar no grupo {i}"

    # Verificando se um usuário inexistente não está nos grupos
    non_existent_user = "non_existent_user"
    for i in range(num_groups):
        assert is_user_in_group(non_existent_user, groups[i]) == False, f"O usuário inexistente não deve estar no grupo {i}"

test_large_user_and_many_groups()