from django.views.generic import TemplateView

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