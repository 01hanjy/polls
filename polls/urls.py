from django.urls import path
from . import views

app_name = 'polls'

# urlpatterns=[
#     #ex: /polls/
#     path('', views.index, name='index'),
#     #ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     #ex: /polls/5/results.
#     path('<int:question_id>/results/', views.results, name='results'),
#     #ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

# path함수는 path(route, view, kwargs, name)형태로 호출
# route: 주소
# view: route의 주소로 접근했을 때 호출할 view
# kwargs: 뷰에 전달할 값들
# name: route의 이름, 원하는 곳에서 주소를 호출해 출력하거나 사용 가능

urlpatterns=[
    #ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    #ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view, name='results'),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]