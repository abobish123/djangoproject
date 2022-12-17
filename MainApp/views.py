from django.shortcuts import render, HttpResponse, Http404

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":3},
   {"id": 5, "name": "Кепка" ,"quantity":12},
]

def items_list(request):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    context = {
        "items":items
    }
    return render(request, "items.html", context)

def item_page(request,id):
    for item in items:
        if item['id'] == id:
            return render(request, "itempage.html", item)
    # item_str = f"товар {item['name']} количество{item['quantity']}"
    #         return render(request, "item"+str(id)+".html")
    # return HttpResponse(f"Товар с id = {id} не найден")
    raise Http404(f"Товар с id = {id} не найден")
