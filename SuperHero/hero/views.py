from pathlib import Path
from unicodedata import name
from django.views.generic import TemplateView
hero_info = {
    'hulk': {
        'name': 'Hulk',
        'identity': 'Bruce Banner',
        'image': 'hulk.jpg',
        'strength1':'Super Strength',
        'strength2':'Resistance to Radiation',
        'weakness1':'Anger Issues',
        'weakness2':'Cannot Control Strength'

    },
    'ironman': {
        'name': 'IronMan',
        'identity': 'Tony Stark',
        'image': 'iron_man.jpg',
        'strength1':'Intelligence',
        'strength2':'Wealthy',
        'weakness1':'Normal Human Body',
        'weakness2':'Arrogant'
    },'blackwidow': {
        'name': 'Black Widow',
        'identity': 'Natasha Romanoff',
        'image': 'black_widow.jpg',
        'strength1':'Super Reflexes',
        'strength2':'Good Spy',
        'weakness1':'Brain Washing',
        'weakness2':'Normal Human Body'
    },'spiderman': {
        'name': 'SpiderMan',
        'identity': 'Peter Parker',
        'image': 'spiderman.jpg',
        'strength1':'Super Strength',
        'strength2':'Spidey Sense',
        'weakness1':'High-Frequencies',
        'weakness2':'Radiation'
    },'Captain America': {
        'name': 'Captain America',
        'identity': 'Steve Rodgers',
        'image': 'captain_america.jpg',
        'strength1':'Super Strength',
        'strength2':'Super Reflexes',
        'weakness1':'No Ranged Attack',
        'weakness2':'Cannot rapidly heal'
    }

}

class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=["hulk","ironman","blackwidow","spiderman","Captain America"])


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        return hero_info[name]


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }
class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'IronMan',
            'id': 'Tony Stark',
            'image': '/static/images/iron_man.jpg'
        }
class BlackWidowView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'id': 'Natasha Romanoff',
            'image': '/static/images/black_widow.jpg'

        }
class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'SpiderMan',
            'id': 'Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }
        
class IndexView(TemplateView):
    template_name = 'heroes.html'