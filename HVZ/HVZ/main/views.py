from django.views.generic import TemplateView

from HVZ.feed.models import Meal
# Create your views here.


class LandingPage(TemplateView):
    template_name = "main/landing_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LandingPage, self).get_context_data(*args, **kwargs)

        context['is_landing_page'] = True
        context['latest_meals'] = Meal.objects.all()[:20]
        return context
