"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, c, *rest = each_wagons_id
    correct = c, *missing_wagons, *rest, a, b
    return list(correct)


def add_missing_stops(arg, **rgs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    dictionary = arg
    values_dict = rgs
    stops = []
    for key, value in values_dict.items():
        stops.append(value)
    stops_dict = {"stops": stops}
    combined_dictionary = {**dictionary, **stops_dict}
    return combined_dictionary


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    a, b, c = zip(*wagons_rows)
    return [list(a), list(b), list(c)]
