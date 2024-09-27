# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
# Initialize these attributes in the constructor.
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name
    
    # Setter for category name
    def set_category_name(self, category_name):
        if isinstance(category_name, str) and category_name.strip():
            self.__category_name = category_name
        else:
            raise ValueError("Category name must be a non-empty string.")
        
    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if isinstance(allocated_budget, (int, float)) and allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")
        
    # Method to add expenses and adjust budget 
    def add_expense(self, expense_amount):
        if isinstance(expense_amount, (int, float)) and expense_amount > 0:
            if expense_amount <= self.__allocated_budget:
                self.__allocated_budget -= expense_amount
                print(f"Expense of {expense_amount} added to {self.__category_name}. Remaining budget: {self.__allocated_budget}")
            else:
                raise ValueError(f"Expense exceeds the available budget of {self.__allocated_budget}.")
        else:
            raise ValueError("Expense amount must be a positive number.")
        
    # Method to display budget details
    def display_budget_details(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__allocated_budget}")


# Example Usage
food_budget = BudgetCategory("Food", 500)
food_budget.add_expense(100)
food_budget.display_budget_details()