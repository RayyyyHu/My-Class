from django.shortcuts import render
from .models import MySubject
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.

def subjects(request, subjectName):
    submenu = subjectName
    if subjectName == 'chinese':
        subjectName = '语文'
    if subjectName == 'math':
        subjectName = '数学'
    if subjectName == 'english':
        subjectName = '英语'
    if subjectName == 'physics':
        subjectName = '物理'
    if subjectName == 'chemistry':
        subjectName = '化学'
    if subjectName == 'biology':
        subjectName = '生物'
    if subjectName == 'geography':
        subjectName = '地理'
    if subjectName == '历史':
        subjectName = 'history'
    if subjectName == 'politics':
        subjectName = '政治'
    
    subjectList = MySubject.objects.all().filter(subjectType = subjectName).order_by('-publishDate')

    p = Paginator(subjectList, 9)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        subjectList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0: page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) (page - 3) if (page - 3) > 0 else 0: page - 1]
            right = page_range[page: page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page
        }
    
    return render(request, 'subjectList.html', {
        'active_menu': subjects,
        'sub_menu': submenu,
        'subjectName': subjectName,
        'subjectList': subjectList,
        'pageData': pageData,
    })

def subjectDetail(request, id):
    mysubject = get_object_or_404(MySubject, id = id)
    mysubject.views += 1
    mysubject.save()

    return render(request, 'subjectDetail.html', {
        'active_menu': 'subjectscenter',
        'mysubject': mysubject,
    })
