from creational_patterns.factory import LogisticsFactory, RoadLogistics, SeaLogistics


def client_code(logistic_factory: LogisticsFactory) -> None:
    print(logistic_factory.operation())
    # transport = logistic_factory.create_transport()
    # print(transport.get_transport())


if __name__ == "__main__":
    print("App: Launched with the RoadLogistics.")
    client_code(RoadLogistics())
    print("\n")

    print("App: Launched with the SeaLogistics.")
    client_code(SeaLogistics())
