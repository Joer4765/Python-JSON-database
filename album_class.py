from abc import ABC, abstractmethod


# Abstract class for MusicProduct
class MusicProduct(ABC):
    def __init__(self, title, group_name, genre, release_year, distributor):
        self.title = title
        self.group_name = group_name
        self.genre = genre
        self.release_year = release_year
        self.distributor = distributor

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value):
        self._release_year = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    # Abstract method for displaying information about the record
    @abstractmethod
    def __str__(self):
        pass



class Album(MusicProduct):
    def __init__(self, title, group_name, genre, release_year, distributor, songs_count, songs_names):
        super().__init__(title, group_name, genre, release_year, distributor)
        self.songs_count = songs_count
        self.songs_names = songs_names


    @property
    def songs_count(self):
        return self._songs_count

    @songs_count.setter
    def songs_count(self, value):
        self._songs_count = value

    @property
    def songs_names(self):
        return self._songs_names

    @songs_names.setter
    def songs_names(self, value):
        self._songs_names = value

    def __str__(self):
        s = f'Title: {self.title}\n'
        s += f'Group: {self.group_name}\n'
        s += f'Genre: {self.genre}\n'
        s += f'Release year: {self.release_year}\n'
        s += f'Distributor: {self.distributor}\n'
        s += f'Songs count: {self.songs_count}\n'
        s += f'Songs names: {", ".join(self.songs_names)}\n'
        return s

    def __del__(self):
        pass
        # messagebox.showinfo('', f"Викликано деструктор для {self.__class__.__name__} - {self.title}")
