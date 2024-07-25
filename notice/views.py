from django.shortcuts import render
from .models import MyNotice
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.

def notice(request):
    noticeList = MyNotice.objects.all().order_by('-publishDate')

    p = Paginator(noticeList, 9)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        noticeList = p.page(page)
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
    
    return render(request, 'noticeList.html', {
        'active_menu': notice,
        'noticeList': noticeList,
        'pageData': pageData,
    })

def noticeDetail(request, id):
    mynotice = get_object_or_404(MyNotice, id = id)
    mynotice.views += 1
    mynotice.save()

    return render(request, "noticeDetail.html", {
        'active_menu': notice,
        'mynotice': mynotice,
    })
