from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

import pandas as pd
import numpy as np
from django.shortcuts import render

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

# csv import
def my_view(request):
    df = pd.read_csv('../test_data.csv', encoding='euc-kr')
    arr = df.to_numpy()
    context = {'data': arr}
    return render(request, 'test_app/index.html', context)

# 결측치 처리
def setnull(request):
    df = pd.read_csv('../test_data.csv', encoding='euc-kr')
    df.fillna("NULL", inplace=True)
    arr = df.to_numpy()
    context = {'data': arr}
    return render(request, 'test_app/index.html', context)

# 평균 나이 알고리즘 구현
def avgage(request):
    df = pd.read_csv('../test_data.csv', encoding='euc-kr')
    avgage = df['나이'].mean()
    df['diff'] = abs(df['나이'] - avgage)
    topten = df.nsmallest(10, 'diff')
    data = topten.to_dict(orient='records')
    return JsonResponse(data, safe=False)