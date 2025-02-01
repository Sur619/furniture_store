from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
'title': "Home - catalog",
'goods': [{'image': 'deps/images/goods/set of tea table and three chairs.jpg',
         'name': 'Tea Table and Three Chairs',
         'description': 'A set of three chairs and a designer table for the living room.',
         'price': 150.00},

         {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
         'name': 'Tea Table and Two Chairs',
         'description': 'A set of a table and two chairs in a minimalist style.',
         'price': 93.00},

         {'image': 'deps/images/goods/double bed.jpg',
         'name': 'Double Bed',
         'description': 'A double bed with a headboard, highly orthopedic.',
         'price': 670.00},

         {'image': 'deps/images/goods/kitchen table.jpg',
         'name': 'Kitchen Table with Sink',
         'description': 'A kitchen dining table with a built-in sink and chairs.',
         'price': 365.00},

         {'image': 'deps/images/goods/kitchen table 2.jpg',
         'name': 'Kitchen Table with Built-in Features',
         'description': 'A kitchen table with a built-in stove and sink. Plenty of shelves and very stylish.',
         'price': 430.00},

         {'image': 'deps/images/goods/corner sofa.jpg',
         'name': 'Corner Sofa for Living Room',
         'description': 'A corner sofa that unfolds into a double bed—perfect for hosting guests!',
         'price': 610.00},

         {'image': 'deps/images/goods/bedside table.jpg',
         'name': 'Bedside Table',
         'description': 'A bedside table with two pull-out drawers (flower not included).',
         'price': 55.00},

         {'image': 'deps/images/goods/sofa.jpg',
         'name': 'Regular Sofa',
         'description': 'A sofa, also known as a regular couch—nothing special to describe.',
         'price': 190.00},

         {'image': 'deps/images/goods/office chair.jpg',
         'name': 'Office Chair',
         'description': 'A product description about how great it is, but it’s just a chair—what else to say...',
         'price': 30.00},

         {'image': 'deps/images/goods/plants.jpg',
         'name': 'Plant',
         'description': 'A plant to decorate your interior, adding freshness and tranquility to the atmosphere.',
         'price': 10.00},

         {'image': 'deps/images/goods/flower.jpg',
         'name': 'Stylized Flower',
         'description': 'A designer flower (possibly artificial) for interior decoration.',
         'price': 15.00},

         {'image': 'deps/images/goods/strange table.jpg',
         'name': 'Bedside Table',
         'description': 'A table that looks rather strange but fits well next to a bed.',
         'price': 25.00}]

    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")