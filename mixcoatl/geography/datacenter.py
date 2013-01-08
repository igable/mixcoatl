from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class DataCenter(Resource):
    path = 'geography/DataCenter'
    collection_name = 'dataCenters'
    primary_key = 'data_center_id'

    def __init__(self, data_center_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__data_center_id = data_center_id

    @property
    def data_center_id(self):
        return self.__data_center_id

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def status(self):
        return self.__status

    @classmethod
    def all(cls,region_id):
        r = Resource(cls.path)
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            x = [cls(i['dataCenterId']) for i in c[cls.collection_name]]
            return x
        else:
            return r.last_error