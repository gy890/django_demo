# coding=utf-8
"""
Created on 2018-06-10

@Filename: middleware
@Author: guiyu


"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


class BookMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('*' * 64)
        user = request.user
        print("BookMiddleware executed by {}".format(user))
        print(request.META.get('REMOTE_ADDR'), request.user.is_authenticated)
        if str(
                user) == 'gui' and '/admin/' not in request.path:  # 如果是管理员gui并且当前路径不是/admin/跳转到/admin/，不加requst.path 会循环重定向
            print(request.user, request.path)
            # return HttpResponseRedirect("https://cn.bing.com/")
            return HttpResponseRedirect("/admin/")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print('-' * 32)

        return response
