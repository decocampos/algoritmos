class Node:
    def __init__(self, username):
        self.username = username
        self.next = None
        self.prev = None

class UserList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_user(self, username):
        new_user = Node(username)
        if not self.head:
            self.head = new_user
            self.tail = new_user
        else:
            new_user.next = self.head
            self.head.prev = new_user
            self.head = new_user

    def move_to_top(self, node):
        if node == self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def remove_user(self, username):
        current = self.head
        while current:
            if current.username == username:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def find_user(self, username):
        current = self.head
        while current:
            if current.username == username:
                return current
            current = current.next
        return None

    def print_order(self):
        current = self.head
        while current:
            print(current.username)
            current = current.next

# Função principal
def main():
    user_list = UserList()

    while True:
        command = input().split()

        if command[0] == "Mark":
            if command[1] == "seguiu":
                user_list.add_user(command[2])
            elif command[1] == "curtiu":
                # Verifica se o usuário já está na lista antes de mover para o topo
                user_node = user_list.find_user(command[5])
                if user_node:
                    user_list.move_to_top(user_node)
                else:
                    user_list.add_user(command[5])
            elif command[1] == "comentou":
                # Verifica se o usuário já está na lista antes de mover para o topo
                user_node = user_list.find_user(command[5])
                if user_node:
                    user_list.move_to_top(user_node)
                else:
                    user_list.add_user(command[5])
            elif command[1] == "deixou":
                user_list.remove_user(command[4])
            elif command[1] == "fechou":
                user_list.print_order()
                break

if __name__ == "__main__":
    main()
