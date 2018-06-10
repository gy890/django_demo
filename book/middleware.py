# coding=utf-8
"""
Created on 2018-06-10

@Filename: middleware
@Author: guiyu


"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


class BookMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('*' * 64)
        user = request.user
        print("BookMiddleware executed by {}".format(user))
        if str(user) == 'AnonymousUser':
            print('匿名用户')
            # return HttpResponseRedirect("https://cn.bing.com/")
            # return HttpResponseRedirect("/admin/")
            # return HttpResponse('FEETET')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print('-' * 32)

        return response
