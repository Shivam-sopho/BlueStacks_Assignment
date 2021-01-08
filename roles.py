class Roles:
    def __init__(self, roles):
        self._roles = ['role1', 'role2', 'role3']
        self._roles_resource_access = {'role1': [
            {'resource': 'R1', 'action': "write"}, {'resource': 'R2', 'action': 'read'}],
            'role2': [
            {'resource': 'R3', 'action': "delete"}, {'resource': 'R4', 'action': 'write'}]}

#    def define_roles_access(roles):
