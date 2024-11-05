import enum


class GenderEnum(str, enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class ProfessionEnum(str, enum.Enum):
    DEVELOPER = 'developer'
    DESIGNER = 'designer'
    MANAGER = 'manager'
    TEACHER = 'teacher'
    DOCTOR = 'doctor'
    WRITER = 'writer'
    ARTIST = 'artist'
    UNEMPLOYED = 'unemployed'


class StatusPost(str, enum.Enum):
    PUBLISHED = 'published'
    DELETED = 'deleted'
    UNDER_MODERATION = 'under moderation'
    DRAFT = 'draft'
    SCHEDULED = 'scheduled'


class RatingEnum(int, enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
