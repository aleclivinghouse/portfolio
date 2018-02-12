# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import contactForm
from django.conf import settings
from django.core.mail import send_mail
from .models import portPiece
from django.template.loader import get_template
from portfolio.utils import render_to_pdf
from django.views.generic import View

# Create your views here.
def home(request):
    form = contactForm(request.POST or None)
    posts = portPiece.objects.all();
    confirm_message = ""
    title =""
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from portfolio site'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        title="Thanks!"

    context = {"the_posts": posts, "form": form, "title": title, "confirm_message": confirm_message}
    template = "index.html"
    return render(request, template, context)







# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('resume.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('resume.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download");
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#                 response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")
