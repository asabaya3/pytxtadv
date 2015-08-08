class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.contains_is_visible = False
        self.contains = []
        self.aliases = []

    def __repr__(self):
        return self.name + "(" + str(self.contains) + ")" if self.contains_is_visible else self.name

    def __eq__(self, other):
        if isinstance(other, Item):
            return super().__eq__(self, other)
        else:
            return any([other in name for name in self.aliases + [self.name] + self.contains])    

    def examine(self):
        print(self.description)
        if self.contains_is_visible:
            print(self.contains)

    def get(self, item_name)
        if any([item_name in item for item in self.aliases + [self.name]])
            return self
        elif self.contains_is_visible:
            for item in self.contains:
                result = item.get(item_name)
                if result:
                    return result
        return None

    def use(self, target):
        print(target.name + " can't use " + self.name)
        return False

    def equip(self, target):
        print(target.name + " can't equip " + self.name)
        return False

    def unequip(self, target):
        print(target.name + " can't unequip " + self.name)
        return False

    def wear(self, target):
        print(target.name + " can't wear " + self.name)
        return False

    def remove(self, target):
        print(target.name + " can't remove " + self.name)
        return False

    def take(self, target):
        print(target.name + " can't take " + self.name)
        return False

    def drop(self, target):
        print(target.name + " can't drop " + self.name)
        return False

    def open(self):
        print(self.name + " can't be opened")
        return False

    def close(self):
        print(self.name + " can't be closed")
        return False

class Takeable_Item(Item)
    def take(self, target):
        target.inventory.append(self)
        print(target.name + " takes " + self.name)
        return True
    def drop(self, target):
        target.inventory.remove(self)
        print(target.name + " drops " + self.name)
        return True

class Equipable_Item(Item)
    def equip(self, target):
        self.name = self.name + "(equipped)"
        print(target.name + " equips " + self.name)
        return True
    def unequip(self, target):
        self.name = self.name.replace("(equipped)",'')
        print(target.name + " unequips " + self.name)
        return True
        
class Container_Item(Item)
    def open(self):
        self.contains_is_visible = True
        print(self.name + " is opened")
        return True
    def close(self):
        self.contains_is_visible = False
        print(self.name + " is closed")
        return True