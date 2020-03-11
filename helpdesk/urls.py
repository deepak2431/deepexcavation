"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

urls.py - Mapping of URL's to our various views. Note we always used NAMED
          views for simplicity in linking later on.
"""

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from helpdesk import settings as helpdesk_settings
from helpdesk.views import feeds, staff, public, api, kb


class DirectTemplateView(TemplateView):
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        return context

urlpatterns = [
    # url(r'^dashboard/$',
    #     staff.dashboard,
    #     name='helpdesk_dashboard'),

    url(r'^tickets/$',
        staff.ticket_list,
        name='helpdesk_list'),

    url(r'^tickets/update/$',
        staff.mass_update,
        name='helpdesk_mass_update'),

    url(r'^tickets/submit/$',
        staff.create_ticket,
        name='helpdesk_submit'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/$',
        staff.view_ticket,
        name='helpdesk_view'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/followup_edit/(?P<followup_id>[0-9]+)/$',
        staff.followup_edit,
        name='helpdesk_followup_edit'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/followup_delete/(?P<followup_id>[0-9]+)/$',
        staff.followup_delete,
        name='helpdesk_followup_delete'),


    url(r'^tickets/(?P<ticket_id>[0-9]+)/update/$',
        staff.update_ticket,
        name='helpdesk_update'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/delete/$',
        staff.delete_ticket,
        name='helpdesk_delete'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/hold/$',
        staff.hold_ticket,
        name='helpdesk_hold'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/unhold/$',
        staff.unhold_ticket,
        name='helpdesk_unhold'),

    url(r'^tickets/(?P<ticket_id>[0-9]+)/attachment_delete/(?P<attachment_id>[0-9]+)/$',
        staff.attachment_del,
        name='helpdesk_attachment_del'),

    url(r'^raw/(?P<type>\w+)/$',
        staff.raw_details,
        name='helpdesk_raw'),

    # url(r'^rss/$',
    #     staff.rss_list,
    #     name='helpdesk_rss_index'),

    # url(r'^reports/$',
    #     staff.report_index,
    #     name='helpdesk_report_index'),

    # url(r'^reports/(?P<report>\w+)/$',
    #     staff.run_report,
    #     name='helpdesk_run_report'),
    #
    # url(r'^save_query/$',
    #     staff.save_query,
    #     name='helpdesk_savequery'),
    #
    # url(r'^delete_query/(?P<id>[0-9]+)/$',
    #     staff.delete_saved_query,
    #     name='helpdesk_delete_query'),

    url(r'^settings/$',
        staff.user_settings,
        name='helpdesk_user_settings'),

    url(r'^ignore/$',
        staff.email_ignore,
        name='helpdesk_email_ignore'),

    url(r'^ignore/add/$',
        staff.email_ignore_add,
        name='helpdesk_email_ignore_add'),

    url(r'^ignore/delete/(?P<id>[0-9]+)/$',
        staff.email_ignore_del,
        name='helpdesk_email_ignore_del'),
]

urlpatterns += [
    url(r'^$',
        public.homepage,
        name='helpdesk_home'),

    url(r'^view/$',
        public.view_ticket,
        name='helpdesk_public_view'),

    url(r'^change_language/$',
        public.change_language,
        name='helpdesk_public_change_language'),
]





if helpdesk_settings.HELPDESK_KB_ENABLED:
    urlpatterns += [
        url(r'^kb/$',
            kb.index,
            name='helpdesk_kb_index'),

        url(r'^kb/(?P<item>[0-9]+)/$',
            kb.item,
            name='helpdesk_kb_item'),

        url(r'^kb/(?P<item>[0-9]+)/vote/$',
            kb.vote,
            name='helpdesk_kb_vote'),

        url(r'^kb/(?P<slug>[A-Za-z0-9_-]+)/$',
            kb.category,
            name='helpdesk_kb_category'),
    ]

