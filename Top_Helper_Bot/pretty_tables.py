from prettytable import PrettyTable


class PrettyView:
    def create_table(self, data):
        raise NotImplementedError

    def create_row(self, data):
        raise NotImplementedError


class ABview(PrettyView):
    def create_table(self, data):
        pt = PrettyTable()
        pt.field_names = ["Name", "Phone", "Birthday", "Email"]

        for row in data:
            pt.add_row(row)
        return pt

    def create_row(self, data):
        pt = PrettyTable()
        pt.field_names = ["Name", "Phone", "Birthday", "Email"]
        pt.add_row(data)
        return pt


class NotesView(PrettyView):
    def create_table(self, data):
        pt = PrettyTable()
        pt.field_names = ["Index", "Tags", "Note"]
        for row in data:
            pt.add_row(row)
        return pt

    def create_row(self, data):
        pt = PrettyTable()
        pt.field_names = ["Name", "Tags"]
        pt.add_row(data)
        return pt


class SortView(PrettyView):
    def create_row(self, data):
        pt = PrettyTable()
        pt.field_names = ["Known extensions", "Unknown extensions"]
        pt.add_row(data)
        return pt

    def create_table(self, data):
        pass
