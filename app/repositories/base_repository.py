from abc import ABC,abstractmethod
import pandas as pd

class BaseRepository(ABC):


    """ Return places from the repository """
    @abstractmethod
    def get_places(self) -> pd.DataFrame:
        pass