from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^brewing', views.brewing, name='brewing'),
    url(r'^coffee_cone', views.coffee_cone, name='coffee_cone'),
    url(r'^chemex', views.chemex, name='chemex'),
    url(r'^french_press', views.french_press, name='french_press'),
	url(r'^aeropress', views.aeropress, name='aeropress'),
    url(r'^stovetop_moka_pot', views.stovetop_moka_pot, name='stovetop_moka_pot'),
    url(r'^siphon', views.siphon, name='siphon'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^search', views.search, name='search'),
    url(r'^product/(?P<coffee_name_slug>[\w\-]+)/$', views.product, name='product'),
    url(r'^vendorsignup', views.vendor_signup, name='vendorsignup'),
    url(r'^load_api', views.load_api, name='load_api'),
    url(r'^product/[\w\-]+/get-cafes', views.get_beanstack_cafes, name="get_cafes"),
    url(r'^product/[\w\-]+/update-my-beanstack', views.update_my_beanstack, name="update_my_beanstack"),
    url(r'^my-beanstack', views.my_beanstack, name='my_beanstack'),
    url(r'^get-saved-coffees/', views.get_saved_coffees, name='get_saved_coffees'),
]


