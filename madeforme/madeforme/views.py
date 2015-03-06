from django.views.generic import TemplateView

# Landing Page Views - Common views not covered in other apps on the platform

class HomepageView(TemplateView):
	template_name='homepage.html'