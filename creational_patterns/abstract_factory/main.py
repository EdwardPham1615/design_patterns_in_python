from creational_patterns.abstract_factory import FurnitureFactory, ModernFurnitureFactory, VictorianFurnitureFactory


def client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.type())
    print(sofa.type())


if __name__ == "__main__":

    print("Client: Testing client code with the first factory type:")
    client_code(ModernFurnitureFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(VictorianFurnitureFactory())
