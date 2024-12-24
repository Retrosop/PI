class VendingMachine:
    def __init__(self):
        self.state = WaitingForSelection(self)
        self.selected_item = None
        self.balance = 0

    def select_item(self, item):
        self.state.select_item(item)

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def dispense(self):
        self.state.dispense()

class VendingMachineState:
    def __init__(self, machine):
        self.machine = machine

    def select_item(self, item):
        raise NotImplementedError

    def insert_money(self, amount):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError

class WaitingForSelection(VendingMachineState):
    def select_item(self, item):
        self.machine.selected_item = item
        print(f"You have selected: {item}. Please insert money.")
        self.machine.state = WaitingForPayment(self.machine)

class WaitingForPayment(VendingMachineState):
    def insert_money(self, amount):
        self.machine.balance += amount
        print(f"You have inserted: ${amount}. Current balance: ${self.machine.balance}.")
        # Assume each item costs $1 for simplicity
        if self.machine.balance >= 1:
            print("Sufficient funds. You can dispense your item now.")
            self.machine.state = Dispensing(self.machine)
        else:
            print("Insufficient funds. Please insert more money.")

class Dispensing(VendingMachineState):
    def dispense(self):
        if self.machine.selected_item:
            print(f"Dispensing: {self.machine.selected_item}")
            # Reset state
            self.machine.selected_item = None
            self.machine.balance = 0
            self.machine.state = WaitingForSelection(self.machine)
        else:
            print("No item selected to dispense.")

# Пример использования
if __name__ == "__main__":
    vm = VendingMachine()
    vm.select_item("Coke")
    vm.insert_money(0.5)
    vm.insert_money(0.5)
    vm.dispense()