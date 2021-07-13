from django.shortcuts import render, redirect
from django.forms import ModelForm

from items.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description']

def get_item(item_id):
    return Item.objects.get(id=item_id)

def item_list(request):
    items = Item.objects.all()
    data = {'all_items': items}
    return render(request, 'items/item_list.html', data)

def item_view(request, item_id):
    item = get_item(item_id)
    data = {'item': item}
    return render(request, 'items/item_detail.html', data)

def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('items:item_list')
    return render(request, 'items/item_form.html', {'form': form, 'new_or_edit': 'New'})

def item_update(request, item_id):
    item = get_item(item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('items:item_list')
    return render(request, 'items/item_form.html', {'form' :form, 'new_or_edit': 'Edit'})

def item_delete(request, item_id):
    item = get_item(item_id)
    if request.method=='POST':
        item.delete()
        return redirect('items:item_list')
    return render(request, 'items/item_confirm_delete.html', {'object':item})

