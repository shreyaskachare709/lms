from django.shortcuts import render,redirect
from book.models import BookTable

# Create your views here.

def adddata(request):
        if (request.method=='POST'):
            book_name_=request.POST['book_name']
            author_name_=request.POST['author_name']
            price_=request.POST['price']
            typeofbook_=request.POST['typeofbook']
            
            insert_data=BookTable.CustomManager.create(book_name=book_name_ , author_name=author_name_ , price=price_ , typeofbook=typeofbook_)
            insert_data.save()
            return redirect('/')
        return render(request,'book/adddata.html')



def displayalldata(request):
    content=BookTable.CustomManager.filter(is_deleted='n')
    data={'data':content}
    return render(request,'book/displayalldata.html',data)

def harddelete(request,tid):
    record_to_be_deleted=BookTable.CustomManager.filter(id=tid)
    record_to_be_deleted.delete()
    return redirect('/')

def softdelete(request,tid):
    record_to_be_deleted=BookTable.CustomManager.filter(id=tid)
    record_to_be_deleted.update(is_deleted='y')
    return redirect('/')

def update(request,tid):
    if (request.method=='POST'):
        book_name_=request.POST['book_name']
        author_name_=request.POST['author_name']
        price_=request.POST['price']
      
        record_to_be_updated=BookTable.CustomManager.filter(id=tid)
        record_to_be_updated.update(book_name=book_name_ , author_name=author_name_ , price=price_  )
        return redirect('/')
    else:
        content={}
        content['data']=BookTable.CustomManager.get(id=tid)
        return render(request,'book/update.html',content)
def ltoh(request):
    content={}
    content['data']=BookTable.CustomManager.all_book_in_desc_price()
    return render(request,'book/displayalldata.html',content)

def htol(request):
    content={}
    content['data']=BookTable.CustomManager.all_book_in_asc_price()
    return render(request,'book/displayalldata.html',content)



def all_data_include_soft_deleted(request):
    content={}
    content['data']=BookTable.CustomManager.all()
    return render(request,'book/displayalldata.html',content)
