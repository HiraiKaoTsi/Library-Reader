import sqlite3

from Modules.Books import CreateBook

from Modules.DisplayingMessageBox import OpenNotificationDialog


class GettingInformationSQLBooks:
    def __init__(self, method_more_details, method_bookmark_add, method_bookmark_delete):
        self.Base = "Resources\\BaseDataLibrary.db"
        self.Table = "books"

        self.signal_more_details = method_more_details
        self.signal_bookmark_add = method_bookmark_add
        self.signal_bookmark_delete = method_bookmark_delete

    def OpeningTableAllBooks(self, bookmark: tuple = ()) -> tuple:
        print("book", bookmark)
        all_frame = []
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                request_information = cur.execute(f"SELECT * FROM {self.Table};")
            for row in request_information:
                books = CreateBook(row[0], row[1], row[2], row[3], row[17], row[15], row[14], row[13], bookmark,
                                   self.signal_more_details, self.signal_bookmark_add, self.signal_bookmark_delete)
                all_frame.append(books.frame_book)
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

        return tuple(all_frame)

    def SearchByAllCategoriesBooks(self, name_book: str, author: str, price_from: int, price_to: int, publisher: str,
                                   from_data: int, to_data: int, bookmark: tuple = ()) -> tuple:
        all_frame = []
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM books WHERE"
                            f"(({from_data} <= year_publication) AND (year_publication <= {to_data})) "
                            f"AND (({price_from} <= price) AND (price <= {price_to}));")
                request_information = cur.fetchall()
            for row in request_information:
                if (name_book in row[1].lower()) and (author in row[2].lower()) and (publisher in row[3].lower()):
                    books = CreateBook(row[0], row[1], row[2], row[3], row[17], row[15], row[14], row[13], bookmark,
                                       self.signal_more_details, self.signal_bookmark_add, self.signal_bookmark_delete)

                    all_frame.append(books.frame_book)
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

        return tuple(all_frame)

    def SearchByNameBook(self, name_book: str, bookmark: tuple = ()):
        all_frame = []
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                request_information = cur.execute(f"SELECT * FROM {self.Table};")
            for row in request_information:
                if name_book in row[1].lower():
                    books = CreateBook(row[0], row[1], row[2], row[3], row[17], row[15], row[14], row[13], bookmark,
                                       self.signal_more_details, self.signal_bookmark_add, self.signal_bookmark_delete)
                    all_frame.append(books.frame_book)
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

        return tuple(all_frame)

    def SearchInfoById(self, Id: int):
        request_information = ()
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Table} WHERE id == {Id};")
                request_information = cur.fetchone()
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

        return tuple(request_information)
