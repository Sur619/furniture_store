import keyword
from re import search

from django.db.models import Q
from goods.models import products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank



def q_search(query):
    if query.isdigit() and len(query) <=5:
        return products.objects.filter(id=int(query)) 
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    
    return products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")
    # return  products.objects.filter(descriptions__search=query)


    # keywords = [word for word in query.split() if len(word)> 2] 

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return products.objects.filter(q_objects)
        
