from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings  # New Import
from django.conf.urls.static import static  # New Import
from django.conf import settings

# UNDERNEATH your urlpatterns definition, add the following two lines:

urlpatterns = patterns('',
                       url(r'^index', 'chef.views.index', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^chef/', include('chef.urls')),
                       url(r'^$', 'chef.views.mainpage', name='mainpage'),
                       url(r'^new_restaurant_user/', 'chef.views.new_restaurant_user', name='new_restaurant_user'),
                       url(r'^new_worker_user/', 'chef.views.new_worker_user', name='new_worker_user'),
                       url(r'^userprofilepage/(?P<user_id>\d+)', 'chef.views.userprofilepage', name='userprofilepage'),
                       url(r'^restaurantprofilepage/(?P<user_id>\d+)', 'chef.views.restaurantprofilepage',
                           name='restaurantprofilepage'),
                       url(r'^facts_page/', 'chef.views.facts_page', name='facts_page'),
                       url(r'^register/$', 'chef.views.register', name='register'),  # ADD NEW PATTERN!
                       url(r'^login/$', 'chef.views.user_login', name='login'),
                       url(r'^logout/$', 'chef.views.user_logout', name='logout'),
                       url(r'^restricted/', 'chef.views.restricted', name='restricted'),
                       url(r'^contact_us/', 'chef.views.contact_us', name='contact_us'),
                       url(r'^edit_settings_restaurant/', 'chef.views.edit_settings_restaurant',
                           name='edit_settings_restaurant'),
                       url(r'^edit_settings_user/', 'chef.views.edit_settings_user', name='edit_settings_user'),
                       url(r'^jobs_pending/', 'chef.views.jobs_pending', name='jobs_pending'),
                       url(r'^add_a_new_job/', 'chef.views.add_a_new_job', name='add_a_new_job'),
                       url(r'^buy_credit', 'chef.views.buy_credit', name='buy_credit'),
                       url(r'^previous_jobs/', 'chef.views.previous_jobs', name='previous_jobs'),
                       url(r'^edit_settings_user/(?P<poster_id>\d+)', 'chef.views.edit_settings_user', name='edit_settings_user'),
                       url(r'^apply_for_a_new_job/(?P<job_id>\d+)/', 'chef.views.apply_for_a_new_job',
                           name='apply_for_a_new_job'),
                       url(r'^buy_credit_user/', 'chef.views.buy_credit_user', name='buy_credit_user'),
                       url(r'^previous_jobs_user/', 'chef.views.previous_jobs_user', name='previous_jobs_user'),
                       url(r'^jobs_board/', 'chef.views.jobs_board', name='jobs_board'),
                       url(r'^jobs_pending_user/', 'chef.views.jobs_pending_user', name='jobs_pending_user'),
                       url(r'^inbox/', 'chef.views.inbox', name='inbox'),
                       url(r'^read_message/', 'chef.views.read_message', name='read_message'),
                       url(r'^send_message/', 'chef.views.send_message', name='send_message'),
                       url(r'^jobs_pending_user/', 'chef.views.jobs_pending_user', name='jobs_pending_user'),
                       url(r'^register_restaurant/', 'chef.views.register_restaurant', name='register_restaurant'),
                       url(r'^register_user/', 'chef.views.register_user', name='register_user'),
                       url(r'^restaurantprofilepageview/(?P<poster_id>\d+)', 'chef.views.restaurantprofilepageview',
                           name='restaurantprofilepageview'),
                       url(r'^userprofilepageview/(?P<poster_id>\d+)', 'chef.views.userprofilepageview', name='userprofilepageview'),
                       )

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )


