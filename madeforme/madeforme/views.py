from django.views.generic import TemplateView

# Homepage Views - Common views not covered in other apps

class HomepageView(TemplateView):
	template_name='homepage.html'