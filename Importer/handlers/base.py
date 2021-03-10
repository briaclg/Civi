import io


class BaseDataFormat(object):

    @classmethod
    def parse(cls, data):
        """
        Returns a BytesIO object from data
        """
        return io.BytesIO(data)


