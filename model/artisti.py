from dataclasses import dataclass


@dataclass
class Artist:
    ArtistId:int
    Name: str
    Popolarita: int

    def __hash__(self):
        return hash(self.ArtistId)

    def __str__(self):
        return self.Name

    def __eq__(self, other):
        return self.ArtistId == other.ArtistId