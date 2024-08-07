def perform_action(action):
     act_dict: dict = {"add": "Adding item", "delete": "Deleting item", "update": "Updating item"}
     return "Key is not valid!" if action not in act_dict.keys() else act_dict.get(action)

result = perform_action("add")
print(result)