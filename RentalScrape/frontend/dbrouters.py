from .models import OfferList

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == OfferList:
            return 'resultsdatabase'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model == OfferList:
            return 'resultsdatabase'
        return None
