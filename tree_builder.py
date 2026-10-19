class EmployeeNode:
    """
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    """

    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    """

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Check if the team lead exists
        if self.root is None:
            print("No team lead exists yet.")
            return False

        # Check if the side is valid
        if side not in ("left", "right"):
            print("Please choose left or right.")
            return False

        # Start searching from the root
        if current_node is None:
            current_node = self.root

        # Check if we found the correct manager
        if current_node.name == manager_name:

            # Check if the requested side is available
            if getattr(current_node, side) is None:
                setattr(current_node, side, EmployeeNode(employee_name))

                print(
                    f"{employee_name} added to the "
                    f"{side.upper()} of {manager_name}"
                )
                return True

            else:
                print(
                    f"The {side} side of "
                    f"{manager_name} is already taken."
                )
                return False

        # Recursively search the left side
        if current_node.left is not None:
            if self.insert(
                manager_name,
                employee_name,
                side,
                current_node.left
            ):
                return True

        # Recursively search the right side
        if current_node.right is not None:
            if self.insert(
                manager_name,
                employee_name,
                side,
                current_node.right
            ):
                return True

        return False

    def print_tree(self, node=None, level=0):
        # Start at the root if no node is given
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        # Check if the directory is empty
        if node is None:
            print("The company directory is empty.")
            return

        # Print the employee with indentation
        print("  " * level + "- " + node.name)

        # Recursively print the left side
        if node.left is not None:
            self.print_tree(node.left, level + 1)

        # Recursively print the right side
        if node.right is not None:
            self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input(
                "Should this employee be on the LEFT or RIGHT "
                "of the manager? "
            )
            side = side.strip().lower()

            if tree.root is None:
                print("No team lead exists yet.")
            elif side not in ("left", "right"):
                print("Please choose left or right.")
            else:
                # Check whether the manager exists
                def manager_exists(node, name):
                    if node is None:
                        return False

                    if node.name == name:
                        return True

                    return (
                        manager_exists(node.left, name)
                        or manager_exists(node.right, name)
                    )

                if not manager_exists(tree.root, manager):
                    print(f"Manager '{manager}' was not found.")
                else:
                    tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Try again.")


# Test your code here
if __name__ == "__main__":
    company_directory()

"""
For this assignment, I made a Python program that uses a binary
tree to organize employees in a company. The program lets the
user add a team lead, add employees under managers, and prints
the team structure.

I used two classes called EmployeeNode and TeamTree.
EmployeeNode stores the employee's name and their left and
right subordinates. TeamTree handles adding employees and
printing the tree.

I had some problems with the constructors and indentation,
but I was able to fix them. I tested the program by adding
a team lead, adding employees, and printing the team structure.

Everything worked correctly after fixing the errors.
This assignment helped me better understand binary trees,
classes, and recursion in Python.
"""